# pyside6dom.py

import os
import sys
import re
import json      # For saving/loading data (like localStorage)
import math      # For advanced kinematics and geometry
import random    # For games and generative art
from pathlib import Path

from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QBoxLayout, QVBoxLayout, QHBoxLayout, 
    QGridLayout, QPushButton, QLineEdit, QLabel, QSlider, QScrollArea, 
    QCheckBox, QComboBox, QSizePolicy, QPlainTextEdit, QTextBrowser
)
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QImage, QPixmap, QIcon
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PySide6.QtMultimediaWidgets import QVideoWidget

def show_commands():
    """Returns and prints a helpful list of all available DOM engine commands."""
    lines = []
    lines.append("="*45)
    lines.append(" PYSIDE6DOM ENGINE - AVAILABLE COMMANDS")
    lines.append("="*45 + "\n")
    
    for name, obj in globals().items():
        if callable(obj) and getattr(obj, '__module__', '') == __name__ and not name.startswith('_'):
            description = obj.__doc__ if obj.__doc__ else "No description provided."
            lines.append(f" > {name}()")
            lines.append(f"   {description.strip()}\n")
            
    lines.append("="*45)
    final_text = "\n".join(lines)
    print(final_text)
    return final_text

# ========================================== #
#               LOGIC GATES
# ========================================== #

def TAU(a, b):
    if (a == 0 and b == 0) or (a == 0 and b == 1) or (a == 1 and b == 0) or (a == 1 and b == 1):
        return 1
    return 1

def CON(a, b):
    if (a == 0 and b == 0) or (a == 0 and b == 1) or (a == 1 and b == 0) or (a == 1 and b == 1):
        return 0
    return 0

def XOR(a, b):
    if (a == 1 and b == 0) or (a == 0 and b == 1):
        return 1
    return 0

def XNOR(a, b):
    if (a == 0 and b == 0) or (a == 1 and b == 1):
        return 1
    return 0

def AND(a, b):
    if a == 1 and b == 1:
        return 1
    return 0

def NAND(a, b):
    if a == 0 or b == 0:
        return 1
    return 0

def OR(a, b):
    if a == 1 or b == 1:
        return 1
    return 0

def NOR(a, b):
    if a == 0 and b == 0:
        return 1
    return 0

def MI(a, b):
    if a == 0 or b == 1:
        return 1
    return 0

def MNI(a, b):
    if a == 1 and b == 0:
        return 1
    return 0

def CI(a, b):
    if a == 1 or b == 0:
        return 1
    return 0

def CNI(a, b):
    if a == 0 and b == 1:
        return 1
    return 0

def LP(a, b):
    if a == 1:
        return 1
    return 0

def LC(a, b):
    if a == 0:
        return 1
    return 0

def RP(a, b):
    if (a == 0 and b == 1) or (a == 1 and b == 1):
        return 1
    return 0

def RC(a, b):
    if (a == 0 and b == 0) or (a == 1 and b == 0):
        return 1
    return 0

# ===
#  DATE & TIME HELPERS
# ===

def get_full_year():
    """Returns the current 4-digit year (e.g., 2026)."""
    return datetime.now().year

def get_month():
    '''returns 1-12'''
    return datetime.now().month

def get_date():
    '''The day of the month (1-31)'''
    return datetime.now().day

def get_day():
    ''' The day of the week. Python is 1(Mon) to 7(Sun).
    If you want it to perfectly match JS (0=Sun to 6=Sat), use this math:'''
    return int(datetime.now().strftime('%w'))

def get_hours():
    '''gets the hours'''
    return datetime.now().hour

def get_minutes():
    '''gets the minutes'''
    return datetime.now().minute

def get_seconds():
    '''gets the seconds'''
    return datetime.now().second

def is_target_date(target_string):
    '''Get today's date object and instantly convert it to a string'''
    today_str = str(datetime.date.today())

    # Now we can safely compare text to text
    if today_str == target_string:
        return True
    else:
        return False

# ========================================== #
#               CONSOLE ALIAS
# ========================================== #
def cl(*args):
    print(*args)

class console:
    log = cl

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
        sfx.setVolume(0.5) 
        _ui_audio_cache[file_path] = sfx
        
    _ui_audio_cache[file_path].play()

# ========================================== #
#             TIMER MANAGEMENT
# ========================================== #
_timers = {}
_timer_counter = 0

def set_interval(callback_func, ms):
    global _timer_counter
    _timer_counter += 1
    timer_id = f"timer_{_timer_counter}"
    
    t = QTimer()
    t.timeout.connect(callback_func)
    t.start(ms)
    
    _timers[timer_id] = t
    return timer_id

def clear_interval(timer_id):
    if timer_id in _timers:
        _timers[timer_id].stop()
        del _timers[timer_id]

setInterval = set_interval
clearInterval = clear_interval

# ========================================== #
#            WORLDWIDE REGISTRY
# ========================================== #
_dom_registry = {}
_app_instance = None
_root_window = None
_main_container = None
_pending_theme = None

# ========================================== #
#            DOM STYLE ENGINE
# ========================================== #
class DOMStyle:
    def __init__(self, element):
        object.__setattr__(self, '_element', element)
        object.__setattr__(self, '_styles', {})

    def __setattr__(self, key, value):
        # ABSOLUTE POSITIONING
        if key == 'position':
            self.__dict__['position'] = value
            return 

        if key in ('width', 'height'):
            val_str = str(value).replace('px', '').strip()
            try:
                num = int(float(val_str))
                if key == 'width': self._element.raw.setFixedWidth(num)
                elif key == 'height': self._element.raw.setFixedHeight(num)
                return
            except ValueError:
                pass

        if key in ('left', 'top', 'right', 'bottom'):
            self.__dict__[key] = value 
            
            # Allow instant movement if the element is already parented
            if key in ('left', 'top'):
                val_str = str(value).replace('px', '').strip()
                try:
                    num = int(float(val_str))
                    if key == 'left': self._element.raw.move(num, self._element.raw.y())
                    elif key == 'top': self._element.raw.move(self._element.raw.x(), num)
                    return
                except ValueError:
                    pass

        # CSS GRID ENGINE
        if key == 'display' and value == 'grid':
            if hasattr(self._element, 'layout') and self._element.layout is not None:
                QWidget().setLayout(self._element.layout) 
            
            grid = QGridLayout(self._element.raw)
            self._element.layout = grid
            
            self._element.layout._auto_row = 0
            self._element.layout._auto_col = 0
            self._element.layout._max_cols = 3 
            return
            
        if key == 'gridTemplateColumns':
            self.__dict__[key] = value
            if hasattr(self._element, 'layout') and isinstance(self._element.layout, QGridLayout):
                cols = len(str(value).split())
                match = re.search(r'repeat\((\d+)', str(value))
                if match: cols = int(match.group(1))
                self._element.layout._max_cols = max(1, cols)
            return

        if key in ('gridRow', 'gridColumn'):
            self.__dict__[key] = value
            return

        # FLEXBOX LAYOUT ENGINE
        if key == 'display' and value == 'flex':
            return 

        if key == 'flexDirection':
            if hasattr(self._element, 'layout') and isinstance(self._element.layout, QBoxLayout):
                if value == 'row':
                    self._element.layout.setDirection(QBoxLayout.Direction.LeftToRight)
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                elif value == 'column':
                    self._element.layout.setDirection(QBoxLayout.Direction.TopToBottom)
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignTop)
            return

        if key == 'alignItems':
            if hasattr(self._element, 'layout') and isinstance(self._element.layout, QBoxLayout):
                if value in ('flex-start', 'start'):
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                elif value == 'center':
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
                elif value in ('flex-end', 'end'):
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
                elif value == 'stretch':
                    self._element.layout.setAlignment(Qt.AlignmentFlag(0)) 
            return

        # INLINE TEXT ALIGNMENT
        if key == 'textAlign':
            # Hijack the key so the compiler below automatically turns it into 'qproperty-alignment'
            key = 'qpropertyAlignment' 
            
            if value == 'center': value = 'AlignCenter'
            elif value == 'right': value = 'AlignRight'
            elif value == 'left': value = 'AlignLeft'

        # CSS COMPILER
        css_property = ''.join(['-' + c.lower() if c.isupper() else c for c in key])
        self._styles[css_property] = value
        
        css_string = ""
        for prop, val in self._styles.items():
            css_string += f"{prop}: {val}; "
        self._element.raw.setStyleSheet(css_string)

    def __call__(self, css_string):
        self._element.set_style(css_string)

# ========================================== #
#           DOM ELEMENT WRAPPER
# ========================================== #
class DOMElement:
    def __init__(self, tag, qt_widget):
        self.tag = tag
        self.raw = qt_widget
        self._id = ""
        self._children = []
        self._dom_style = DOMStyle(self)

    @property
    def style(self): return self._dom_style

    @property
    def id(self): return self._id

    @id.setter
    def id(self, value):
        self._id = value
        _dom_registry[value] = self
        self.raw.setObjectName(str(value)) # Enables #id CSS styling
        
        # Force Qt to instantly refresh the CSS paint job when an ID is added!
        self.raw.style().unpolish(self.raw)
        self.raw.style().polish(self.raw)
        self.raw.update()

    # CLASS NAME SUPPORT
    @property
    def className(self): 
        return self.raw.property("class") or ""

    @className.setter
    def className(self, value):
        self.raw.setProperty("class", str(value))
        # Force Qt to instantly refresh the CSS paint job!
        self.raw.style().unpolish(self.raw)
        self.raw.style().polish(self.raw)
        self.raw.update()

    def append(self, child_element):
        """
        Mimics JavaScript's element.append(child)
        Because 'self' is the parent, we just pass both to your existing 'ba' function!
        """
        ba(child_element, self)

    def remove(self):
        """
        Mimics JavaScript's element.remove()
        Safely deletes the widget from the screen and clears it from memory.
        """
        self.raw.setParent(None)
        self.raw.deleteLater()

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
        elif isinstance(self.raw, QPlainTextEdit): return self.raw.toPlainText() 
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
    def src(self): return self._src if hasattr(self, "_src") else ""

    @src.setter
    def src(self, file_path):
        self._src = file_path
        if isinstance(self.raw, QLabel) and self.tag == "img":
            self.raw.setPixmap(QPixmap(str(file_path)))
        elif self.tag == "video" and hasattr(self, "player"):
            if str(file_path).startswith("http"):
                self.player.setSource(QUrl(file_path))
            else:
                self.player.setSource(QUrl.fromLocalFile(os.path.abspath(file_path)))

    @property
    def width(self): return self.raw.width()

    @width.setter
    def width(self, val):
        val = int(val)
        self.raw.setFixedWidth(val)
        if self.tag == "img" and self.raw.pixmap():
            orig_w = self.raw.pixmap().width()
            orig_h = self.raw.pixmap().height()
            if orig_w > 0: self.raw.setFixedHeight(int(val * (orig_h / orig_w)))

    @property
    def height(self): return self.raw.height()

    @height.setter
    def height(self, val):
        val = int(val)
        self.raw.setFixedHeight(val)
        if self.tag == "img" and self.raw.pixmap():
            orig_w = self.raw.pixmap().width()
            orig_h = self.raw.pixmap().height()
            if orig_h > 0: self.raw.setFixedWidth(int(val * (orig_w / orig_h)))

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

    @property
    def onmouseover(self): return None

    @onmouseover.setter
    def onmouseover(self, callback_func):
        self.raw.enterEvent = lambda event: callback_func()

    @property
    def onmouseout(self): return None

    @onmouseout.setter
    def onmouseout(self, callback_func):
        self.raw.leaveEvent = lambda event: callback_func()

    @property
    def onclick(self): return None

    @onclick.setter
    def onclick(self, callback_func):
        if hasattr(self.raw, "clicked"): 
            self.raw.clicked.connect(lambda checked=False: callback_func())

    @property
    def oninput(self): return getattr(self, '_oninput', None)

    @oninput.setter
    def oninput(self, callback_func):
        self._oninput = callback_func
        expected_args = callback_func.__code__.co_argcount
        
        def signal_router(*args):
            if expected_args == 0: callback_func()
            else:
                if len(args) > 0: callback_func(args[0])
                else: callback_func(self.value)

        if hasattr(self.raw, 'textChanged'): self.raw.textChanged.connect(signal_router)
        elif hasattr(self.raw, 'valueChanged'): self.raw.valueChanged.connect(signal_router)

    def set_style(self, css_string):
        css_string = css_string.replace("body", "QMainWindow, QWidget#central_widget")
        css_string = css_string.replace("font-color", "color")
        
        css_string = re.sub(r'\bscroll_div\b', 'QScrollArea', css_string)
        css_string = re.sub(r'\bdiv\b', 'QWidget', css_string)
        css_string = re.sub(r'\bbutton\b', 'QPushButton', css_string)
        css_string = re.sub(r'\binput\b', 'QLineEdit', css_string)
        css_string = re.sub(r'\btextarea\b', 'QPlainTextEdit', css_string)
        css_string = re.sub(r'\bselect\b', 'QComboBox', css_string)
        css_string = re.sub(r'\bdropdown\b', 'QComboBox', css_string)
        css_string = re.sub(r'\bcheckbox\b', 'QCheckBox', css_string)
        css_string = re.sub(r'\bslider\b', 'QSlider', css_string)
        css_string = re.sub(r'\btext\b', 'QLabel', css_string)
        css_string = re.sub(r'\bimg\b', 'QLabel', css_string)
        css_string = re.sub(r'\bh1\b', 'QLabel', css_string)
        css_string = re.sub(r'\bp\b', 'QLabel', css_string)
        css_string = re.sub(r'\bspan\b', 'QLabel', css_string)
        css_string = re.sub(r'\boption\b', 'QAbstractItemView', css_string)
        css_string = re.sub(r'\bvideo\b', 'QVideoWidget', css_string)
        css_string = re.sub(r'\btable_view\b', 'QTextBrowser', css_string)

        css_string = re.sub(r'(?<!-)\bwidth\s*:', 'max-width:', css_string)
        css_string = re.sub(r'(?<!-)\bheight\s*:', 'max-height:', css_string)

        if "{" in css_string:
            self.raw.setStyleSheet(css_string)
        else:
            obj_name = self.raw.objectName()
            if not obj_name:
                obj_name = f"dom_node_{id(self.raw)}"
                self.raw.setObjectName(obj_name)
            self.raw.setStyleSheet(f"#{obj_name} {{ {css_string} }}")

    def play(self):
        if self.tag == "video" and hasattr(self, "player"): self.player.play()

    def pause(self):
        if self.tag == "video" and hasattr(self, "player"): self.player.pause()

# ========================================== #
#               DOM PARSER (ce)
# ========================================== #
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
        heading_sizes = {"h1":"32px", "h2":"24px", "h3":"19px", "h4":"16px", "h5":"13px", "h6":"11px"}
        elem.style.fontWeight = 'bold'
        elem.style.fontSize = heading_sizes[tag]
        return elem
    elif tag == "p":
        w = QLabel()
        w.setWordWrap(True)
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        elem = DOMElement(tag, w)
        elem.style.fontSize = '16px'
        elem.style.fontWeight = 'normal'
        return elem
    elif tag in ("text", "span", "label"):
        w = QLabel()
        w.setWordWrap(False)
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
        w.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom, w)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(5, 5, 5, 5)
        elem = DOMElement(tag, w)
        elem.layout = layout
        return elem
    elif tag == "scroll_div":
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        content = QWidget()
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
        w.setLineWrapMode(QTextBrowser.LineWrapMode.NoWrap) 
        return DOMElement(tag, w)
    elif tag == "img":
        w = QLabel()
        w.setScaledContents(True) 
        w.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
    elif tag == "video":
        w = QVideoWidget()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        elem = DOMElement(tag, w)
        elem.player = QMediaPlayer()
        elem.audio = QAudioOutput()
        elem.player.setAudioOutput(elem.audio)
        elem.player.setVideoOutput(w)
        return elem
    raise ValueError(f"Unknown tag: {tag}")

# ========================================== #
#        LAYOUT & WINDOW MANAGEMENT
# ========================================== #
def ge(element_id):
    return _dom_registry.get(element_id, None)

def ba(child_elem, parent_elem=None):
    if parent_elem is None:
        parent_elem = _main_container
        
    if child_elem is None or parent_elem is None:
        return

    is_absolute = getattr(child_elem.style, 'position', '') == 'absolute'

    # --- ABSOLUTE POSITIONING LOGIC ---
    if is_absolute:
        target_widget = parent_elem.raw
        if isinstance(target_widget, QMainWindow) and target_widget.centralWidget():
            target_widget = target_widget.centralWidget()

        child_elem.raw.setParent(target_widget)
        
        parent_w = target_widget.width()
        parent_h = target_widget.height()
        
        child_elem.raw.adjustSize() 
        child_w = child_elem.raw.width()
        child_h = child_elem.raw.height()

        x, y = 0, 0

        if 'right' in child_elem.style.__dict__:
            right_val = int(float(str(child_elem.style.right).replace('px', '')))
            x = parent_w - child_w - right_val
        elif 'left' in child_elem.style.__dict__:
            x = int(float(str(child_elem.style.left).replace('px', '')))

        if 'bottom' in child_elem.style.__dict__:
            bottom_val = int(float(str(child_elem.style.bottom).replace('px', '')))
            y = parent_h - child_h - bottom_val
        elif 'top' in child_elem.style.__dict__:
            y = int(float(str(child_elem.style.top).replace('px', '')))
            
        child_elem.raw.move(x, y)
        child_elem.raw.show()
        child_elem.raw.raise_() 

    # --- GRID / FLEXBOX LOGIC ---
    else:
        if hasattr(parent_elem, 'layout') and parent_elem.layout is not None:
            if isinstance(parent_elem.layout, QGridLayout):
                grid = parent_elem.layout
                
                explicit_row = getattr(child_elem.style, 'gridRow', None)
                explicit_col = getattr(child_elem.style, 'gridColumn', None)
                
                r = (int(explicit_row) - 1) if explicit_row else grid._auto_row
                c = (int(explicit_col) - 1) if explicit_col else grid._auto_col
                
                print(f"[Grid Auto-Flow] Placing {child_elem.tag} at Row: {r}, Col: {c}")
                grid.addWidget(child_elem.raw, r, c)
                
                if not explicit_row and not explicit_col:
                    grid._auto_col += 1
                    if grid._auto_col >= grid._max_cols:
                        grid._auto_col = 0
                        grid._auto_row += 1
            else:
                parent_elem.layout.addWidget(child_elem.raw)
        else:
            child_elem.raw.setParent(parent_elem.raw)

def set_theme(css_string):
    global _pending_theme 
    css_string = css_string.replace("body", "QMainWindow, QWidget#central_widget")
    css_string = css_string.replace("font-color", "color")

    # Translate standard HTML text-align to Qt's native property
    css_string = re.sub(r'text-align\s*:\s*center', "qproperty-alignment: 'AlignCenter'", css_string)
    css_string = re.sub(r'text-align\s*:\s*right', "qproperty-alignment: 'AlignRight'", css_string)
    css_string = re.sub(r'text-align\s*:\s*left', "qproperty-alignment: 'AlignLeft'", css_string)
    css_string = re.sub(r'\bscroll_div\b', 'QScrollArea', css_string)
    css_string = re.sub(r'\bdiv\b', 'QWidget', css_string)
    css_string = re.sub(r'\bbutton\b', 'QPushButton', css_string)
    css_string = re.sub(r'\binput\b', 'QLineEdit', css_string)
    css_string = re.sub(r'\btextarea\b', 'QPlainTextEdit', css_string)
    css_string = re.sub(r'\bselect\b', 'QComboBox', css_string)
    css_string = re.sub(r'\bdropdown\b', 'QComboBox', css_string)
    css_string = re.sub(r'\bcheckbox\b', 'QCheckBox', css_string)
    css_string = re.sub(r'\bslider\b', 'QSlider', css_string)
    css_string = re.sub(r'\btext\b', 'QLabel', css_string)
    css_string = re.sub(r'\bimg\b', 'QLabel', css_string)
    css_string = re.sub(r'\bh1\b', 'QLabel', css_string)
    css_string = re.sub(r'\bp\b', 'QLabel', css_string)
    css_string = re.sub(r'\bspan\b', 'QLabel', css_string)
    css_string = re.sub(r'\boption\b', 'QAbstractItemView', css_string)
    css_string = re.sub(r'\bvideo\b', 'QVideoWidget', css_string)
    css_string = re.sub(r'\btable_view\b', 'QTextBrowser', css_string)

    # The (?<!\d) ensures we don't accidentally ruin decimal numbers like "0.5"
    css_string = re.sub(r'(?<!\d)\.([a-zA-Z_][a-zA-Z0-9_-]*)', r'*[class~="\1"]', css_string)
    
    css_string = re.sub(r'(?<!-)\bwidth\s*:', 'max-width:', css_string)
    css_string = re.sub(r'(?<!-)\bheight\s*:', 'max-height:', css_string)
    
    app = QApplication.instance()
    if app: app.setStyleSheet(css_string)
    else: _pending_theme = css_string

set_global_style = set_theme

def init_window(title="App Window", width=420, height=500, icon_path=None):
    global _app_instance, _root_window, _main_container, _pending_theme
    
    if os.name == 'nt':
        import ctypes
        myappid = 'CollegeOfScripting.PySide6DOM.App.1' 
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    _app_instance = QApplication.instance() or QApplication(sys.argv)
    _app_instance.setStyle("Fusion")

    if _pending_theme:
        _app_instance.setStyleSheet(_pending_theme)
        _pending_theme = None
    
    _root_window = QWidget()
    _root_window.setWindowTitle(title)
    _root_window.resize(width, height)
    
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
# College of Scripting Music & Science
#
# GitHub: https://github.com/ChristopherAndrewTopalian
#
# GitHub: https://github.com/ChristopherTopalian
# Google Sites: https://sites.google.com/view/CollegeOfScripting

