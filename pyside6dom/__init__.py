# pyside6dom.py

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, 
    QLineEdit, QLabel, QSlider, QScrollArea, QCheckBox, 
    QComboBox, QSizePolicy, QPlainTextEdit
)
from PySide6.QtCore import Qt, QTimer

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
        if hasattr(self.raw, "clicked"): self.raw.clicked.connect(callback_func)

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

    def style(self, css_string):
        self.raw.setStyleSheet(css_string)


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

def set_global_style(css_string):
    """Applies a universal stylesheet to the entire application, just like a <style> block."""
    if _app_instance:
        _app_instance.setStyleSheet(css_string)

def init_window(title="App Window", width=420, height=500):
    global _app_instance, _root_window, _main_container
    _app_instance = QApplication(sys.argv)
    _app_instance.setStyle("Fusion")
    
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

