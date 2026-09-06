# pyside6dom.py

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, 
    QLineEdit, QLabel, QSlider, QScrollArea
)
from PySide6.QtCore import Qt

_dom_registry = {}
_app_instance = None
_root_window = None
_main_container = None

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
        elif isinstance(self.raw, QSlider): return self.raw.value() / 10.0
        return None

    @value.setter
    def value(self, val):
        if isinstance(self.raw, QLineEdit): self.raw.setText(str(val))
        elif isinstance(self.raw, QSlider): self.raw.setValue(int(float(val) * 10))

    @property
    def placeholder(self):
        return self.raw.placeholderText() if hasattr(self.raw, "placeholderText") else ""

    @placeholder.setter
    def placeholder(self, text):
        if hasattr(self.raw, "setPlaceholderText"): self.raw.setPlaceholderText(str(text))

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
        elif isinstance(self.raw, QSlider):
            self.raw.valueChanged.connect(lambda val: callback_func(val / 10.0))

    def style(self, css_string):
        self.raw.setStyleSheet(css_string)


def ce(tag):
    tag = tag.lower()
    if tag == "button":
        w = QPushButton()
        w.setStyleSheet("padding: 8px 14px; background-color: #2b2b2b; color: white; border-radius: 4px;")
        return DOMElement(tag, w)
    elif tag in ("text", "p", "span", "h1"):
        w = QLabel()
        w.setStyleSheet("color: #ffffff; font-size: 14px;")
        return DOMElement(tag, w)
    elif tag == "input":
        w = QLineEdit()
        w.setStyleSheet("padding: 6px; background-color: #1a1a1a; color: white; border: 1px solid #444;")
        return DOMElement(tag, w)
    elif tag == "slider":
        w = QSlider(Qt.Orientation.Horizontal)
        w.setMinimum(0)
        w.setMaximum(100)
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
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setWidget(content)
        elem = DOMElement(tag, scroll)
        elem.layout = layout
        return elem
    raise ValueError(f"Unknown tag: {tag}")

def ge(element_id):
    return _dom_registry.get(element_id, None)

def ba(child, parent=None):
    target = parent if parent is not None else _main_container
    if hasattr(target, "layout") and target.layout is not None:
        target.layout.addWidget(child.raw)
    elif isinstance(target, QVBoxLayout):
        target.addWidget(child.raw)

def init_window(title="App Window", width=420, height=500):
    global _app_instance, _root_window, _main_container
    _app_instance = QApplication(sys.argv)
    _app_instance.setStyle("Fusion")
    _root_window = QWidget()
    _root_window.setWindowTitle(title)
    _root_window.resize(width, height)
    _root_window.setStyleSheet("background-color: rgb(30, 30, 30);")
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

