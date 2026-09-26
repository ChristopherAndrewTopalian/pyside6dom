# pyside6dom.py

import os
import sys
import re
from PySide6.QtWidgets import (
    QApplication, QWidget, QBoxLayout, QVBoxLayout, QHBoxLayout, QPushButton, 
    QLineEdit, QLabel, QSlider, QScrollArea, QCheckBox, 
    QComboBox, QSizePolicy, QPlainTextEdit, QTextBrowser
)
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPixmap, QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import QUrl

####

# shortcut for print, console.log
def cl(*args):
    print(*args)

# class to act as the 'console' namespace
class console:
    log = cl

####

# ========================================== #
#             UI AUDIO MANAGER
# ========================================== #
_ui_audio_cache = {}

def play_sound(file_path):
    """Plays a local .wav file instantly for UI feedback."""
    if not os.path.exists(file_path):
        cl(f"[Audio Missing] Pretend you heard: {file_path}")
        return

    if file_path not in _ui_audio_cache:
        sfx = QSoundEffect()
        sfx.setSource(QUrl.fromLocalFile(os.path.abspath(file_path)))
        # Set volume from 0.0 to 1.0
        sfx.setVolume(0.5) 
        _ui_audio_cache[file_path] = sfx
        
    _ui_audio_cache[file_path].play()


####

# ========================================== #
#               TIMER MANAGEMENT             #
# ========================================== 

_timers = {}
_timer_counter = 0

def set_interval(callback_func, ms):
    """Executes a function repeatedly, calling it every X milliseconds."""
    global _timer_counter
    _timer_counter += 1
    timer_id = f"timer_{_timer_counter}"
    
    t = QTimer()
    t.timeout.connect(callback_func)
    t.start(ms)
    
    _timers[timer_id] = t
    return timer_id

def clear_interval(timer_id):
    """Stops and removes a timer by its ID."""
    if timer_id in _timers:
        _timers[timer_id].stop()
        del _timers[timer_id]

# THE ALIASES
setInterval = set_interval
clearInterval = clear_interval

# ========================================== #
#           WORLDWIDE REGISTRY
# ========================================== 

_dom_registry = {}
_app_instance = None
_root_window = None
_main_container = None
_pending_theme = None

##----------------------------------------
# DOMStyle allows element.style.color = 'white'
##----------------------------------------

class DOMStyle:
    def __init__(self, element):
        # Store a reference to the DOMElement wrapper
        object.__setattr__(self, '_element', element)
        object.__setattr__(self, '_styles', {})

    def __setattr__(self, key, value):
        # ABSOLUTE SIZING
        if key in ('width', 'height'):
            val_str = str(value).replace('px', '').strip()
            try:
                num = int(float(val_str))
                if key == 'width': self._element.width = num 
                elif key == 'height': self._element.height = num 
                return
            except ValueError:
                pass 
                
        # NEW: FLEXBOX LAYOUT ENGINE
        if key == 'display' and value == 'flex':
            # Qt layouts are inherently flex-like, so we can just absorb this
            return 
            
        if key == 'flexDirection':
            if hasattr(self._element, 'layout'):
                if value == 'row':
                    self._element.layout.setDirection(QBoxLayout.Direction.LeftToRight)
                    # Pack items tightly to the Left and Top (Matches web flex-start)
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                elif value == 'column':
                    self._element.layout.setDirection(QBoxLayout.Direction.TopToBottom)
                    # Pack items tightly to the Top
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            return

        # NEW: FLEXBOX ALIGN ITEMS (Stop Stretching)
        if key == 'alignItems':
            if hasattr(self._element, 'layout'):
                if value in ('flex-start', 'start'):
                    # Packs items tightly to the left/top (Stops stretching!)
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                elif value == 'center':
                    # Centers items without stretching
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
                elif value in ('flex-end', 'end'):
                    # Packs to the right
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
                elif value == 'stretch':
                    # Qt's default is to stretch. Sending 0 clears the alignment overrides!
                    self._element.layout.setAlignment(Qt.AlignmentFlag(0)) 
            return # Stop here so it doesn't get passed as raw CSS

        # Convert JavaScript camelCase to CSS kebab-case 
        css_property = re.sub(r'(?<!^)(=[A-Z])', r'-\1', key).lower()
        css_property = ''.join(['-' + c.lower() if c.isupper() else c for c in key])

        # Store the new style in our dictionary
        self._styles[css_property] = value

        # Build the complete CSS string from all stored styles
        css_string = ""
        for prop, val in self._styles.items():
            css_string += f"{prop}: {val}; "

        # Apply it to the underlying PySide6 widget
        self._element.raw.setStyleSheet(css_string)

    def __call__(self, css_string):
        self._element.set_style(css_string)

# ========================================== #
#            DOM ELEMENT WRAPPER             #
# ========================================== 

class DOMElement:
    def __init__(self, tag, qt_widget):
        self.tag = tag
        self.raw = qt_widget
        self._id = ""
        self._children = []
        # Instantiate the style engine in the background
        self._dom_style = DOMStyle(self)

    # This intercepts `.style` so Qt doesn't crash
    @property
    def style(self):
        return self._dom_style

    @property
    def id(self): return self._id

    @id.setter
    def id(self, value):
        self._id = value
        _dom_registry[value] = self

    @property
    def textContent(self):
        if hasattr(self.raw, "text"): return self.raw.text()
        return ""

    @textContent.setter
    def textContent(self, value):
        if hasattr(self.raw, "setText"): self.raw.setText(str(value))

    @property
    def innerHTML(self):
        if hasattr(self.raw, "text"): return self.raw.text()
        return ""

    @innerHTML.setter
    def innerHTML(self, value):
        if hasattr(self.raw, "setText"):
            # Update this line to include QTextBrowser!
            if isinstance(self.raw, (QLabel, QTextBrowser)):
                if isinstance(self.raw, QLabel):
                    self.raw.setTextFormat(Qt.TextFormat.RichText)

                html_str = str(value)

                if "<table" in html_str and "<style>" not in html_str:
                    default_table_css = """
                    <style>
                        table { border-collapse: collapse; margin-top: 10px; }
                        th, td { padding: 6px 12px; border: 1px solid #777; }
                        th { background-color: #333333; color: #00ffcc; font-weight: bold; }
                    </style>
                    """
                    html_str = default_table_css + html_str

                self.raw.setText(html_str)
            else:
                self.raw.setText(str(value))

    @property
    def value(self):
        if isinstance(self.raw, QLineEdit): return self.raw.text()
        elif isinstance(self.raw, QPlainTextEdit): return self.raw.toPlainText() #
        elif isinstance(self.raw, QSlider): return self.raw.value() / 10.0
        elif isinstance(self.raw, QComboBox): return self.raw.currentText()
        return None

    @value.setter
    def value(self, val):
        if isinstance(self.raw, QLineEdit): self.raw.setText(str(val))
        elif isinstance(self.raw, QPlainTextEdit): self.raw.setPlainText(str(val))
        elif isinstance(self.raw, QSlider): self.raw.setValue(int(float(val) * 10))
        elif isinstance(self.raw, QComboBox): self.raw.setCurrentText(str(val))

    @property
    def src(self):
        return self._src if hasattr(self, "_src") else ""

    @src.setter
    def src(self, file_path):
        self._src = file_path
        
        # Handle Images
        if isinstance(self.raw, QLabel) and self.tag == "img":
            pixmap = QPixmap(str(file_path))
            self.raw.setPixmap(pixmap)
            
        # Handle Video
        elif self.tag == "video" and hasattr(self, "player"):
            if str(file_path).startswith("http"):
                self.player.setSource(QUrl(file_path))
            else:
                self.player.setSource(QUrl.fromLocalFile(os.path.abspath(file_path)))


    @property
    def width(self):
        return self.raw.width()

    @width.setter
    def width(self, val):
        val = int(val)
        self.raw.setFixedWidth(val)
        
        # HTML Image Emulation: Auto-calculate proportional height
        if self.tag == "img" and self.raw.pixmap():
            orig_w = self.raw.pixmap().width()
            orig_h = self.raw.pixmap().height()
            if orig_w > 0:
                prop_h = int(val * (orig_h / orig_w))
                self.raw.setFixedHeight(prop_h)

    @property
    def height(self):
        return self.raw.height()

    @height.setter
    def height(self, val):
        val = int(val)
        self.raw.setFixedHeight(val)
        
        # HTML Image Emulation: Auto-calculate proportional width
        if self.tag == "img" and self.raw.pixmap():
            orig_w = self.raw.pixmap().width()
            orig_h = self.raw.pixmap().height()
            if orig_h > 0:
                prop_w = int(val * (orig_w / orig_h))
                self.raw.setFixedWidth(prop_w)

    @property
    def placeholder(self):
        return self.raw.placeholderText() if hasattr(self.raw, "placeholderText") else ""

    @placeholder.setter
    def placeholder(self, text):
        if hasattr(self.raw, "setPlaceholderText"): self.raw.setPlaceholderText(str(text))

    @property
    def checked(self):
        if isinstance(self.raw, QCheckBox): return self.raw.isChecked()
        return False

    @checked.setter
    def checked(self, val):
        if isinstance(self.raw, QCheckBox): self.raw.setChecked(bool(val))

    @property
    def options(self):
        if isinstance(self.raw, QComboBox):
            return [self.raw.itemText(i) for i in range(self.raw.count())]
        return []

    @options.setter
    def options(self, val_list):
        if isinstance(self.raw, QComboBox) and isinstance(val_list, list):
            self.raw.clear()
            self.raw.addItems([str(v) for v in val_list])

    ####

    @property
    def onmouseover(self): return None

    @onmouseover.setter
    def onmouseover(self, callback_func):
        # Qt's 'enterEvent' fires when the mouse enters the widget boundary
        self.raw.enterEvent = lambda event: callback_func()

    @property
    def onmouseout(self): return None

    @onmouseout.setter
    def onmouseout(self, callback_func):
        # Qt's 'leaveEvent' fires when the mouse leaves
        self.raw.leaveEvent = lambda event: callback_func()

    ####

    @property
    def onclick(self): return None

    @onclick.setter
    def onclick(self, callback_func):
        if hasattr(self.raw, "clicked"): 
            # We use a lambda to absorb Qt's sneaky boolean, then call the function cleanly
            self.raw.clicked.connect(lambda checked=False: callback_func())


    @property
    def oninput(self):
        return getattr(self, '_oninput', None)

    @oninput.setter
    def oninput(self, callback_func):
        self._oninput = callback_func
        expected_args = callback_func.__code__.co_argcount
        
        # A smart wrapper that absorbs any number of arguments (0, 1, or more)
        def signal_router(*args):
            if expected_args == 0:
                callback_func()
            else:
                # If PySide6 emitted an argument (like a normal input or slider)
                if len(args) > 0:
                    callback_func(args[0])
                # If PySide6 emitted NOTHING (like a textarea), grab the value manually
                else:
                    callback_func(self.value)

        # Connect Inputs & TextAreas
        if hasattr(self.raw, 'textChanged'):
            self.raw.textChanged.connect(signal_router)
                
        # Connect Sliders
        elif hasattr(self.raw, 'valueChanged'):
            self.raw.valueChanged.connect(signal_router)

    def set_style(self, css_string):
        # Run all the web-to-Qt translations first

        # WEB TO QT CSS TRANSLATOR
        css_string = css_string.replace("body", "QMainWindow, QWidget#central_widget")
        css_string = css_string.replace("font-color", "color")
        
        # Translate compound words FIRST
        css_string = re.sub(r'\bscroll_div\b', 'QScrollArea', css_string)
        
        # Translate base tags using \b (word boundaries) so it doesn't break CSS properties!
        css_string = re.sub(r'\bdiv\b', 'QWidget', css_string)
        css_string = re.sub(r'\bbutton\b', 'QPushButton', css_string)
        css_string = re.sub(r'\binput\b', 'QLineEdit', css_string)
        css_string = re.sub(r'\btextarea\b', 'QPlainTextEdit', css_string)
        css_string = re.sub(r'\bselect\b', 'QComboBox', css_string)
        css_string = re.sub(r'\bdropdown\b', 'QComboBox', css_string)
        css_string = re.sub(r'\bcheckbox\b', 'QCheckBox', css_string)
        css_string = re.sub(r'\bslider\b', 'QSlider', css_string)
        
        # Translate all text/image tags to QLabel
        css_string = re.sub(r'\btext\b', 'QLabel', css_string)
        css_string = re.sub(r'\bimg\b', 'QLabel', css_string)
        css_string = re.sub(r'\bh1\b', 'QLabel', css_string)
        css_string = re.sub(r'\bp\b', 'QLabel', css_string)
        css_string = re.sub(r'\bspan\b', 'QLabel', css_string)
        css_string = re.sub(r'\boption\b', 'QAbstractItemView', css_string)
        css_string = re.sub(r'\bvideo\b', 'QVideoWidget', css_string)
        css_string = re.sub(r'\btable_view\b', 'QTextBrowser', css_string)

        # NEW: STOP QT FROM STRETCHING WIDGETS
        # Translates "width:" to "max-width:" (but ignores if it is already "max-width")
        css_string = re.sub(r'(?<!-)\bwidth\s*:', 'max-width:', css_string)
        css_string = re.sub(r'(?<!-)\bheight\s*:', 'max-height:', css_string)

        # Advanced CSS with brackets (e.g., "button:hover { color: red; }")
        # because of the replacements above, "button:hover" is now "QPushButton:hover"
        if "{" in css_string:
            self.raw.setStyleSheet(css_string)

        # Inline web-style CSS (e.g., "border: 1px solid white;")
        else:
            obj_name = self.raw.objectName()
            if not obj_name:
                obj_name = f"dom_node_{id(self.raw)}"
                self.raw.setObjectName(obj_name)
            
            # Wrap the string in a strict ID selector
            scoped_css = f"#{obj_name} {{ {css_string} }}"
            self.raw.setStyleSheet(scoped_css)

    def play(self):
        if self.tag == "video" and hasattr(self, "player"):
            self.player.play()

    def pause(self):
        if self.tag == "video" and hasattr(self, "player"):
            self.player.pause()

# ========================================== #
#               DOM PARSER (ce)              #
# ========================================== 

def ce(tag):
    tag = tag.lower()
    
    if tag == "button":
        w = QPushButton()
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)

    elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        w = QLabel()
        w.setWordWrap(True)
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        elem = DOMElement(tag, w)
        
        # HTML browser-standard font sizes (based on a 16px root)
        heading_sizes = {
            "h1": "32px",  # 2.00em
            "h2": "24px",  # 1.50em
            "h3": "19px",  # 1.17em
            "h4": "16px",  # 1.00em
            "h5": "13px",  # 0.83em
            "h6": "11px"   # 0.67em
        }

        # Apply the default native HTML styling
        elem.style.fontWeight = 'bold'
        elem.style.fontSize = heading_sizes[tag]
        return elem

    elif tag == "p":
        w = QLabel()
        w.setWordWrap(True)  # Paragraphs must always wrap
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)

        elem = DOMElement(tag, w)

        # HTML browser-standard paragraph size
        elem.style.fontSize = '16px'
        elem.style.fontWeight = 'normal'
        return elem

    elif tag in ("text", "span", "label"):
        w = QLabel()
        w.setWordWrap(False) # Inline data strings do not wrap; they trigger horizontal scrollbars!
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
        
    elif tag == "input":
        w = QLineEdit()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)

    elif tag == "textarea":
        w = QPlainTextEdit()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return DOMElement(tag, w)
        
    elif tag == "slider":
        w = QSlider(Qt.Orientation.Horizontal)
        w.setMinimum(0)
        w.setMaximum(100)
        return DOMElement(tag, w)
        
    elif tag == "checkbox":
        w = QCheckBox()
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
        
    elif tag in ("select", "dropdown"):
        w = QComboBox()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
        
    elif tag == "div":
        w = QWidget()
        # we now use a dynamic QBoxLayout instead of a fixed QVBoxLayout
        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom, w)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(5, 5, 5, 5)
        elem = DOMElement(tag, w)
        elem.layout = layout
        return elem

    elif tag == "scroll_div":
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)

        # Act like HTML 'overflow: auto'
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        content = QWidget()
        
        # We keep the QBoxLayout so Flexbox features still work!
        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom, content)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(4)
        layout.setContentsMargins(0, 0, 0, 0)

        scroll.setWidget(content)
        elem = DOMElement(tag, scroll)
        elem.layout = layout
        return elem

    elif tag == "table_view":
        w = QTextBrowser()
        # This tells the browser NOT to squish the table, forcing the horizontal scrollbar!
        w.setLineWrapMode(QTextBrowser.LineWrapMode.NoWrap) 
        return DOMElement(tag, w)

    elif tag == "img":
        w = QLabel()
        w.setScaledContents(True) # Makes it behave like HTML CSS sizing
        w.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)

    elif tag == "video":
        w = QVideoWidget()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        elem = DOMElement(tag, w)
        
        # Create the invisible brain and speaker
        elem.player = QMediaPlayer()
        elem.audio = QAudioOutput()
        
        # Wire them together
        elem.player.setAudioOutput(elem.audio)
        elem.player.setVideoOutput(w)

        return elem

    raise ValueError(f"Unknown tag: {tag}")


# ========================================== #
#        LAYOUT & WINDOW MANAGEMENT          #
# ==========================================

def ge(element_id):
    return _dom_registry.get(element_id, None)

def ba(child, parent=None):
    target = parent if parent is not None else _main_container
    if hasattr(target, "layout") and target.layout is not None:
        target.layout.addWidget(child.raw)
    elif isinstance(target, QVBoxLayout):
        target.addWidget(child.raw)

def set_theme(css_string):
    """
    Translates standard HTML/CSS selectors into PySide6 QSS classes,
    allowing users to style the app using pure web syntax.
    """
    global _pending_theme  # <--- Bring in the buffer

    # WEB TO QT CSS TRANSLATOR
    css_string = css_string.replace("body", "QMainWindow, QWidget#central_widget")
    css_string = css_string.replace("font-color", "color")
    
    # Translate compound words FIRST
    css_string = re.sub(r'\bscroll_div\b', 'QScrollArea', css_string)
    
    # Translate base tags using \b (word boundaries) so it doesn't break CSS properties
    css_string = re.sub(r'\bdiv\b', 'QWidget', css_string)
    css_string = re.sub(r'\bbutton\b', 'QPushButton', css_string)
    css_string = re.sub(r'\binput\b', 'QLineEdit', css_string)
    css_string = re.sub(r'\btextarea\b', 'QPlainTextEdit', css_string)
    css_string = re.sub(r'\bselect\b', 'QComboBox', css_string)
    css_string = re.sub(r'\bdropdown\b', 'QComboBox', css_string)
    css_string = re.sub(r'\bcheckbox\b', 'QCheckBox', css_string)
    css_string = re.sub(r'\bslider\b', 'QSlider', css_string)
    
    # Translate all text/image tags to QLabel
    css_string = re.sub(r'\btext\b', 'QLabel', css_string)
    css_string = re.sub(r'\bimg\b', 'QLabel', css_string)
    css_string = re.sub(r'\bh1\b', 'QLabel', css_string)
    css_string = re.sub(r'\bp\b', 'QLabel', css_string)
    css_string = re.sub(r'\bspan\b', 'QLabel', css_string)
    css_string = re.sub(r'\boption\b', 'QAbstractItemView', css_string)
    css_string = re.sub(r'\bvideo\b', 'QVideoWidget', css_string)
    css_string = re.sub(r'\btable_view\b', 'QTextBrowser', css_string)

    # NEW: STOP QT FROM STRETCHING WIDGETS
    # Translates "width:" to "max-width:" (but ignores if it is already "max-width")
    css_string = re.sub(r'(?<!-)\bwidth\s*:', 'max-width:', css_string)
    css_string = re.sub(r'(?<!-)\bheight\s*:', 'max-height:', css_string)
    
    # Try to apply immediately. If it fails, save it for later!
    app = QApplication.instance()
    if app:
        app.setStyleSheet(css_string)
    else:
        _pending_theme = css_string

# The Aliases (Keeps old scripts alive, allows preference)
set_global_style = set_theme

########

'''
def init_window(title="App Window", width=420, height=500):
    global _app_instance, _root_window, _main_container, _pending_theme
    
    # Safely get or create the app
    _app_instance = QApplication.instance() or QApplication(sys.argv)
    _app_instance.setStyle("Fusion")

    # Catch the pending theme
    if _pending_theme:
        _app_instance.setStyleSheet(_pending_theme)
        _pending_theme = None
    
    _root_window = QWidget()
    _root_window.setWindowTitle(title)
    _root_window.resize(width, height)
    
    _main_layout = QVBoxLayout(_root_window)
    _main_container = ce("scroll_div")

    # Force the main window background to fill the screen
    _main_container.raw.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
    _main_layout.addWidget(_main_container.raw)
'''

def init_window(title="App Window", width=420, height=500, icon_path=None):
    global _app_instance, _root_window, _main_container, _pending_theme
    
    # THE CROSS-PLATFORM TASKBAR FIX
    # os.name == 'nt' ensures this ONLY runs on Windows.
    # Mac ('posix') and Linux ('posix') will completely ignore this block.
    if os.name == 'nt':
        import ctypes
        myappid = 'CollegeOfScripting.PySide6DOM.App.1' 
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    # Safely get or create the app
    _app_instance = QApplication.instance() or QApplication(sys.argv)
    _app_instance.setStyle("Fusion")

    # Catch the pending theme
    if _pending_theme:
        _app_instance.setStyleSheet(_pending_theme)
        _pending_theme = None
    
    _root_window = QWidget()
    _root_window.setWindowTitle(title)
    _root_window.resize(width, height)
    
    # APPLY THE ICON (This works natively on all platforms)
    if icon_path and os.path.exists(icon_path):
        _app_instance.setWindowIcon(QIcon(icon_path))
    
    _main_layout = QVBoxLayout(_root_window)
    _main_container = ce("scroll_div")
    _main_layout.addWidget(_main_container.raw)

def run_app():
    _root_window.show()
    sys.exit(_app_instance.exec())

####

# Dedicated to God the Father
# (c) Copyright 2026 Christopher Andrew Topalian
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# GitHub: https://github.com/ChristopherAndrewTopalian/pyside6dom
#
# PyPI: https://pypi.org/project/pyside6dom/
#
# GitHub: https://github.com/ChristopherAndrewTopalian
#
# GitHub: https://github.com/ChristopherTopalian
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting

