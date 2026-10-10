# pyside6dom.py

import os
import sys
import re
import json      # For saving/loading data (like localStorage)
import math      # For advanced kinematics and geometry
import random    # For games and generative art
import subprocess
from pathlib import Path

from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QBoxLayout, QVBoxLayout, QHBoxLayout, 
    QGridLayout, QPushButton, QLineEdit, QLabel, QSlider, QScrollArea, 
    QCheckBox, QComboBox, QSizePolicy, QPlainTextEdit, QTextBrowser
)
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QImage, QPixmap, QIcon, QDesktopServices
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

class dom:
    '''Namespace class for this engine's utility functions'''

    @staticmethod
    def get_year():
        """Returns the current 4-digit year (e.g., 2026)."""
        return datetime.today().year

    @staticmethod
    def get_month():
        """Returns the current month number (1-12)."""
        return datetime.today().month

    @staticmethod
    def get_day_of_month():
        """Returns the day of the month (1-31)."""
        return datetime.today().day

    @staticmethod
    def get_day_name():
        """Returns the full name of the day (e.g., 'Monday', 'Tuesday')."""
        return datetime.today().strftime("%A")

    @staticmethod
    def get_day_of_week():
        """Returns the day of the week as an integer (0-6).
        Matches JS DOM getDay(): 0=Sunday ... 6=Saturday."""
        return int(datetime.today().strftime('%w'))

    @staticmethod
    def get_day_of_week_iso():
        """Returns the day of the week as an integer (1-7).
        Matches ISO standard: 1=Monday ... 7=Sunday."""
        return datetime.today().isoweekday()

    @staticmethod
    def get_month_day_year():
        """Returns today's date formatted as MM-DD-YYYY."""
        return datetime.today().strftime("%m-%d-%Y")

    @staticmethod
    def get_year_month_day():
        """Returns today's date formatted as YYYY-MM-DD."""
        return datetime.today().strftime("%Y-%m-%d")

    # TIME FUNCTIONS

    @staticmethod
    def get_hours():
        """Returns the current hour in 24-hour format (0-23)."""
        return datetime.now().hour

    @staticmethod
    def get_minutes():
        """Returns the current minute (0-59)."""
        return datetime.now().minute

    @staticmethod
    def get_seconds():
        """Returns the current second (0-59)."""
        return datetime.now().second

    # UTILITY

    @staticmethod
    def is_target_date(target_string):
        ''' Compare today yy-mm-dd with target_string'''
        # Get today's date object and instantly convert it to a string
        today_str = str(datetime.today().strftime("%Y-%m-%d"))
        
        # Now we can safely compare text to text
        if today_str == target_string:
            return True
        else:
            return False

    # ===
    # FILE
    # ===

    @staticmethod
    def open_file(whichFilePath):
        '''Open the specified File'''
        if os.path.exists(whichFilePath):
            if sys.platform == 'win32':
                os.startfile(whichFilePath)
            elif sys.platform == 'darwin':
                subprocess.call(('open', whichFilePath))
            else:
                subprocess.call(('xdg-open', whichFilePath))
        else:
            print('File not found:', whichFilePath)

    @staticmethod
    def show_in_file_explorer(path):
        """Reveal a file, highlighted, in the OS file manager."""
        path = str(Path(path).resolve())

        if sys.platform == 'win32':
            subprocess.Popen(f'explorer /select,"{path}"')
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', '-R', path])
        else:
            # Most Linux file managers don't support "select this file" —
            # opening the containing folder is the reliable fallback
            subprocess.Popen(['xdg-open', str(Path(path).parent)])

####

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
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
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

        # ===
        # Flex Layout Spacing Translators
        # ===
        if key == 'padding':
            # If it's a layout container, set C++ margins
            if hasattr(self._element, 'layout') and self._element.layout:
                try:
                    val = int(str(value).replace('px', '').strip())
                    self._element.layout.setContentsMargins(val, val, val, val)
                except: pass
            # DO NOT RETURN! We let this fall through to the CSS Compiler
            # so that simple elements (like buttons) still get standard CSS padding!
                
        if key == 'gap':
            # Translate gap to C++ setSpacing
            if hasattr(self._element, 'layout') and self._element.layout:
                try:
                    val = int(str(value).replace('px', '').strip())
                    self._element.layout.setSpacing(val)
                except: pass
            return # Qt CSS doesn't understand 'gap', so we safely exit here.
        # ===

        # ===
        # INLINE TEXT DECORATION 
        # Bypasses the CSS Engine to prevent QLabel warnings!
        # ===
        if key == 'textDecoration':
            font = self._element.raw.font()
            if value == 'underline':
                font.setUnderline(True)
            elif value == 'line-through':
                font.setStrikeOut(True)
            elif value in ('none', ''):
                font.setUnderline(False)
                font.setStrikeOut(False)
            
            self._element.raw.setFont(font)
            return # Exit instantly so it doesn't hit the CSS compiler

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
            
        # Route it through your master compiler
        self._element.set_style(css_string)

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

    # ========================================== #
    # HTML DOM Standard: Title (Tooltip)
    # ========================================== #
    @property
    def title(self): 
        return getattr(self, "_title", "")

    @title.setter
    def title(self, text):
        self._title = str(text)
        self._update_tooltip()

    @property
    def titleFontSize(self): 
        return getattr(self, "_title_font_size", "14px") # Default is larger than HTML!

    @titleFontSize.setter
    def titleFontSize(self, size):
        # Safely handle if a user types 18 or "18px"
        val = str(size)
        if val.isdigit(): val += "px"
        
        self._title_font_size = val
        self._update_tooltip()
        
    def _update_tooltip(self):
        """Secretly wraps the tooltip in HTML so Qt renders it with a custom font size."""
        if not getattr(self, "_title", ""):
            self.raw.setToolTip("")
            return
            
        size = self.titleFontSize
        text = self._title
        
        # Qt natively parses this inline HTML!
        rich_tooltip = f'<span style="font-size: {size};">{text}</span>'
        self.raw.setToolTip(rich_tooltip)

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
        if hasattr(self.raw, "setText"): 
            self.raw.setText(str(value))
            
        elif self.tag in ("div", "scroll_div", "row_div"):
            # If the secret text node doesn't exist yet, create it!
            if not hasattr(self, "_secret_text_node"):
                self._secret_text_node = ce('text')
                # Force it to be perfectly transparent so it blends into the div
                self._secret_text_node.raw.setStyleSheet("background: transparent; border: none; margin: 0px; padding: 0px;")
                self.append(self._secret_text_node)
            
            # Update the existing secret text node
            self._secret_text_node.textContent = str(value)

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
                
        elif self.tag in ("div", "scroll_div", "row_div"):
            # Same safety check for innerHTML!
            if not hasattr(self, "_secret_text_node"):
                self._secret_text_node = ce('text')
                self._secret_text_node.raw.setStyleSheet("background: transparent; border: none; margin: 0px; padding: 0px;")
                self.append(self._secret_text_node)
                
            self._secret_text_node.innerHTML = str(value)

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

    # ===
    # HTML DOM Standard: Anchor Tags
    # ===
    @property
    def href(self): return getattr(self, "_href", "")

    @href.setter
    def href(self, url):
        self._href = url
        # The Magic: Override the mouse click to open the computer's real web browser!
        def open_link(event):
            QDesktopServices.openUrl(QUrl(str(url)))
        self.raw.mousePressEvent = open_link

    @property
    def target(self): return getattr(self, "_target", "")

    @target.setter
    def target(self, val):
        # QDesktopServices always opens in a new tab/window by default, 
        # but capturing 'target' here prevents your JS scripts from throwing an error!
        self._target = val

    @property
    def readOnly(self):
        if hasattr(self.raw, "isReadOnly"): return self.raw.isReadOnly()
        return False

    @readOnly.setter
    def readOnly(self, val):
        if hasattr(self.raw, "setReadOnly"): 
            self.raw.setReadOnly(bool(val))

    # Alias for lowercase 'readonly' to prevent typos
    @property
    def readonly(self): return self.readOnly

    @readonly.setter
    def readonly(self, val): self.readOnly = val

    @property
    def disabled(self):
        if hasattr(self.raw, "isEnabled"): return not self.raw.isEnabled()
        return False

    @disabled.setter
    def disabled(self, val):
        if hasattr(self.raw, "setEnabled"): 
            # In Qt, 'setEnabled(False)' is the equivalent of HTML 'disabled=True'
            self.raw.setEnabled(not bool(val))
    # ===

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
    def onclick(self): return getattr(self, '_onclick_callback', None)

    @onclick.setter
    def onclick(self, callback_func):
        if hasattr(self.raw, "clicked"): 
            self.raw.clicked.connect(lambda checked=False: callback_func())
        else:
            # If it's NOT a button, force it through the universal mouse router!
            self._onclick_callback = callback_func
            self._install_mouse_router()

    # ========================================== #
    # ADVANCED MOUSE ROUTER (Universal Clicks)
    # ========================================== #
    def _install_mouse_router(self):
        if hasattr(self, '_mouse_router_active'): return
        self._mouse_router_active = True
        
        def custom_mouse_press(event):
            # Universal Left Click (For Divs, Images, and Text!)
            if event.button() == Qt.MouseButton.LeftButton:
                if getattr(self, '_onclick_callback', None):
                    self._onclick_callback()
                    
            # Intercept Right Click (Context Menu)
            elif event.button() == Qt.MouseButton.RightButton:
                if getattr(self, '_oncontextmenu', None):
                    self._oncontextmenu()
                    
            # Intercept Middle Click
            elif event.button() == Qt.MouseButton.MiddleButton:
                if getattr(self, '_onauxclick', None):
                    self._onauxclick()
                    
            type(self.raw).mousePressEvent(self.raw, event)
            
        self.raw.mousePressEvent = custom_mouse_press

    @property
    def oncontextmenu(self): return getattr(self, '_oncontextmenu', None)

    @oncontextmenu.setter
    def oncontextmenu(self, callback_func):
        self._oncontextmenu = callback_func
        self._install_mouse_router()

    # The Custom Alias
    @property
    def onrightclick(self): return self.oncontextmenu

    @onrightclick.setter
    def onrightclick(self, callback_func): 
        self.oncontextmenu = callback_func

    @property
    def onauxclick(self): return getattr(self, '_onauxclick', None)

    @onauxclick.setter
    def onauxclick(self, callback_func):
        self._onauxclick = callback_func
        self._install_mouse_router()

    # The Middle Click Alias
    @property
    def onmiddleclick(self): return self.onauxclick

    @onmiddleclick.setter
    def onmiddleclick(self, callback_func): 
        self.onauxclick = callback_func

    # The Left Click Alias
    @property
    def onleftclick(self): return self.onclick

    @onleftclick.setter
    def onleftclick(self, callback_func): 
        self.onclick = callback_func

    # ===

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

    @property
    def onchange(self): return getattr(self, '_onchange', None)

    @onchange.setter
    def onchange(self, callback_func):
        self._onchange = callback_func
        # This Qt signal ONLY fires when the user releases the mouse
        if hasattr(self.raw, 'sliderReleased'):
            self.raw.sliderReleased.connect(lambda: callback_func(self.value))

    @property
    def onenter(self): return None

    @onenter.setter
    def onenter(self, callback_func):
        # QLineEdit has a built-in signal specifically for the Enter key
        if hasattr(self.raw, "returnPressed"):
            self.raw.returnPressed.connect(callback_func)

    def set_style(self, css_string):
        css_string = css_string.replace("body", "QMainWindow, QWidget#central_widget")
        css_string = css_string.replace("font-color", "color")

        # Translate standard HTML text-align to Qt's native property
        css_string = re.sub(r'text-align\s*:\s*center', "qproperty-alignment: 'AlignCenter'", css_string)
        css_string = re.sub(r'text-align\s*:\s*right', "qproperty-alignment: 'AlignRight'", css_string)
        css_string = re.sub(r'text-align\s*:\s*left', "qproperty-alignment: 'AlignLeft'", css_string)

        # Translate HTML :active state to Qt's native :pressed state
        css_string = css_string.replace(":active", ":pressed")
        
        css_string = re.sub(r'\bscroll_div\b', 'QScrollArea', css_string)
        css_string = re.sub(r'\brow_div\b', 'QWidget', css_string)
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

        # First, make sure it has a valid target block (e.g., #dom_node_123 { ... })
        if "{" not in css_string:
            obj_name = self.raw.objectName()
            if not obj_name:
                obj_name = f"dom_node_{id(self.raw)}"
                self.raw.setObjectName(obj_name)
            css_string = f"#{obj_name} {{ {css_string} }}"

        # Run the Text Compiler on inline styles too!
        blocks = re.findall(r'([^{]+)\{([^}]+)\}', css_string)
        compiled_css = ""
        text_properties = ('color', 'font-size', 'font-weight', 'font-family', 'qproperty-alignment', 'font-style')
        
        for selectors, rules in blocks:
            compiled_css += f"{selectors} {{ {rules} }}\n"
            extracted_text_rules = []
            for rule in rules.split(';'):
                if ':' in rule:
                    prop = rule.split(':')[0].strip().lower()
                    if prop in text_properties:
                        extracted_text_rules.append(rule.strip())
            
            if extracted_text_rules:
                lbl_selectors = [f"{sel.strip()} QLabel" for sel in selectors.split(',')]
                compiled_css += f"{', '.join(lbl_selectors)} {{ {'; '.join(extracted_text_rules)}; background: transparent; border: none; }}\n"
                
        # Apply the compiled string
        self.raw.setStyleSheet(compiled_css)

    def play(self):
        if self.tag == "video" and hasattr(self, "player"): self.player.play()

    def pause(self):
        if self.tag == "video" and hasattr(self, "player"): self.player.pause()

    def focus(self):
        """Mimics JavaScript's element.focus()"""
        if hasattr(self.raw, "setFocus"):
            self.raw.setFocus()

    def blur(self):
        """Mimics JavaScript's element.blur()"""
        if hasattr(self.raw, "clearFocus"):
            self.raw.clearFocus()

    def click(self):
        """Mimics JavaScript's element.click()"""
        if hasattr(self.raw, "click"):
            self.raw.click()

    # === 
    # THE ADD_EVENT_LISTENER SWITCHBOARD
    # ===
    def addEventListener(self, event_type, callback):
        """The Master Switchboard for Web Standard Events"""
        event_type = event_type.lower()
        
        if event_type in ('click', 'leftclick'):
            # Qt's .connect() automatically stacks, so this mimics JS
            if hasattr(self.raw, "clicked"): 
                self.raw.clicked.connect(lambda checked=False: callback())
                
        elif event_type == 'input':
            if hasattr(self.raw, 'textChanged'): 
                self.raw.textChanged.connect(lambda val: callback(val))
            elif hasattr(self.raw, 'valueChanged'):
                self.raw.valueChanged.connect(lambda val: callback(val))
                
        elif event_type in ('mouseenter', 'mouseover'):
            def custom_enter(event):
                callback()
                # Pass the event back to Qt so Tooltips and native styles still work!
                type(self.raw).enterEvent(self.raw, event)
            self.raw.enterEvent = custom_enter
            
        elif event_type in ('mouseleave', 'mouseout'):
            def custom_leave(event):
                callback()
                # Pass the event back to Qt!
                type(self.raw).leaveEvent(self.raw, event)
            self.raw.leaveEvent = custom_leave
            
        elif event_type == 'keydown':
            # ---
            # We create a fake JS Event object so event.key works!
            # ---
            def key_interceptor(event):
                key_name = event.text()
                # Normalize the C++ Enter key so it matches JS standard 'Enter'
                if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                    key_name = 'Enter'
                    
                # Build the fake JS object on the fly
                class JSEvent: pass
                js_evt = JSEvent()
                js_evt.key = key_name
                js_evt.preventDefault = lambda: event.accept()
                
                callback(js_evt)
                
                # IMPORTANT: Fire the original Qt event so inputs don't break when typing!
                type(self.raw).keyPressEvent(self.raw, event) 
                
            self.raw.keyPressEvent = key_interceptor
            
        elif event_type in ('contextmenu', 'rightclick'):
            self.oncontextmenu = callback
            
        elif event_type in ('auxclick', 'middleclick'):
            self.onauxclick = callback

        else:
            print(f"Warning: '{event_type}' is not yet mapped in PySide6DOM.")

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

    elif tag == "a":
        w = QLabel()
        w.setWordWrap(True)
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        # Instantly make the mouse look like a clickable web link!
        w.setCursor(Qt.CursorShape.PointingHandCursor) 
        return DOMElement(tag, w)
    
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
        
        # ===
        # THE HTML DOM FIX
        # Strip Qt's default desktop spacing to 0 so 
        # divs stack skin-to-skin just like the Web!
        # ===
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
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

    # Translate HTML :active state to Qt's native :pressed state
    css_string = css_string.replace(":active", ":pressed")
    
    css_string = re.sub(r'\bscroll_div\b', 'QScrollArea', css_string)
    css_string = re.sub(r'\brow_div\b', 'QWidget', css_string) # <--- ADDED!
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

    # ========================================== #
    # CSS TEXT INHERITANCE COMPILER
    # ========================================== #
    blocks = re.findall(r'([^{]+)\{([^}]+)\}', css_string)
    compiled_css = ""
    
    text_properties = ('color', 'font-size', 'font-weight', 'font-family', 'qproperty-alignment', 'font-style')
    
    for selectors, rules in blocks:
        compiled_css += f"{selectors} {{ {rules} }}\n"
        extracted_text_rules = []
        for rule in rules.split(';'):
            if ':' in rule:
                prop = rule.split(':')[0].strip().lower()
                if prop in text_properties:
                    extracted_text_rules.append(rule.strip())
        
        if extracted_text_rules:
            lbl_selectors = [f"{sel.strip()} QLabel" for sel in selectors.split(',')]
            compiled_css += f"{', '.join(lbl_selectors)} {{ {'; '.join(extracted_text_rules)}; background: transparent; border: none; }}\n"
            
    css_string = compiled_css
    # ========================================== #
    
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

# ===
# GLOBAL WINDOW EVENTS
# === #
class GlobalWindowTarget:
    """Mimics the browser's global 'window' object for game loops and global key captures."""
    def addEventListener(self, event_type, callback):
        event_type = event_type.lower()
        if event_type == 'keydown':
            if _root_window is None:
                print("Error: Call init_window() before adding window events.")
                return
                
            def global_key_interceptor(event):
                key_name = event.text()
                if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                    key_name = 'Enter'
                    
                class JSEvent: pass
                js_evt = JSEvent()
                js_evt.key = key_name
                js_evt.preventDefault = lambda: event.accept()
                
                callback(js_evt)
                type(_root_window).keyPressEvent(_root_window, event)
                
            _root_window.keyPressEvent = global_key_interceptor

# Instantiate the global 'window' variable so students can use it instantly!
window = GlobalWindowTarget()

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

