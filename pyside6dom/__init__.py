# pyside6dom.py

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, 
    QLineEdit, QLabel, QSlider, QScrollArea, QCheckBox, 
    QComboBox, QSizePolicy, QPlainTextEdit
)
from PySide6.QtCore import Qt, QTimer

####

# shortcut for print, console.log
def cl(*args):
    print(*args)

# class to act as the 'console' namespace
class console:
    log = cl

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

# ========================================== #
#            DOM ELEMENT WRAPPER             #
# ========================================== 

class DOMElement:
    def __init__(self, tag, qt_widget):
        self.tag = tag
        self.raw = qt_widget
        self._id = ""
        self._children = []

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
    def onclick(self): return None

    @onclick.setter
    def onclick(self, callback_func):
        if hasattr(self.raw, "clicked"): 
            # We use a lambda to absorb Qt's sneaky boolean, then call the function cleanly
            self.raw.clicked.connect(lambda checked=False: callback_func())

    @property
    def oninput(self): return None

    @oninput.setter
    def oninput(self, callback_func):
        if isinstance(self.raw, QLineEdit):
            self.raw.textChanged.connect(lambda text: callback_func(text))
        elif isinstance(self.raw, QPlainTextEdit):
            self.raw.textChanged.connect(lambda: callback_func(self.raw.toPlainText()))
        elif isinstance(self.raw, QSlider):
            self.raw.valueChanged.connect(lambda val: callback_func(val / 10.0))
        elif isinstance(self.raw, QCheckBox):
            self.raw.toggled.connect(lambda val: callback_func(val))
        elif isinstance(self.raw, QComboBox):
            self.raw.currentTextChanged.connect(lambda text: callback_func(text))


    '''
    def style(self, css_string):
        # If the user put brackets in their string (like "QPushButton:hover { color: red }"), 
        # they are doing advanced Qt styling. Let it pass through untouched!
        if "{" in css_string:
            self.raw.setStyleSheet(css_string)
            
        # If there are no brackets, it's a web-style inline string ("border: 1px solid white").
        # We need to isolate it so it doesn't ruin child elements!
        else:
            # Grab the widget's ID, or create a totally unique one using its memory address
            obj_name = self.raw.objectName()
            if not obj_name:
                obj_name = f"dom_node_{id(self.raw)}"
                self.raw.setObjectName(obj_name)
            
            # Wrap the string in a strict ID selector (e.g., #dom_node_12345 { border: ... })
            scoped_css = f"#{obj_name} {{ {css_string} }}"
            self.raw.setStyleSheet(scoped_css)
    '''

    def style(self, css_string):
        # Fix CSS history here too! (The side door)
        css_string = css_string.replace("font-color", "color")
        
        # If the user put brackets in their string (like "QPushButton:hover { color: red }"), 
        # they are doing advanced Qt styling. Let it pass through untouched!
        if "{" in css_string:
            self.raw.setStyleSheet(css_string)
            
        # If there are no brackets, it's a web-style inline string ("border: 1px solid white").
        else:
            obj_name = self.raw.objectName()
            if not obj_name:
                obj_name = f"dom_node_{id(self.raw)}"
                self.raw.setObjectName(obj_name)
            
            # Wrap the string in a strict ID selector
            scoped_css = f"#{obj_name} {{ {css_string} }}"
            self.raw.setStyleSheet(scoped_css)

# ========================================== #
#               DOM PARSER (ce)              #
# ========================================== 

def ce(tag):
    tag = tag.lower()
    
    if tag == "button":
        w = QPushButton()
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
        
    elif tag in ("text", "p", "span", "h1"):
        w = QLabel()
        w.setWordWrap(True)
        # FIX: Never squish text vertically
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
        layout = QVBoxLayout(w)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(5, 5, 5, 5)
        elem = DOMElement(tag, w)
        elem.layout = layout
        return elem
        
    elif tag == "scroll_div":
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        # FIX: Kill the horizontal scrollbar
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(4)
        
        scroll.setWidget(content)
        elem = DOMElement(tag, scroll)
        elem.layout = layout
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

    css_string = css_string.replace("body", "QMainWindow, QWidget#central_widget")
    css_string = css_string.replace("button", "QPushButton")
    css_string = css_string.replace("input", "QLineEdit")
    css_string = css_string.replace("textarea", "QPlainTextEdit")
    css_string = css_string.replace("scroll_div", "QScrollArea")
    css_string = css_string.replace("text", "QLabel")
    css_string = css_string.replace("font-color", "color")
    
    # Try to apply immediately. If it fails, save it for later!
    app = QApplication.instance()
    if app:
        app.setStyleSheet(css_string)
    else:
        _pending_theme = css_string

# The Aliases (Keeps old scripts alive, allows preference)
set_global_style = set_theme

########

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

