# catopalian_py_pyside6_pyside6dom.py

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, 
    QLineEdit, QLabel, QSlider, QScrollArea
)
from PySide6.QtCore import Qt

# ----
# CORE DOM BRIDGE LAYER
# ----

_dom_registry = {}
_app_instance = None
_root_window = None
_main_container = None

class DOMElement:
    """Wrapper that translates standard DOM properties to PySide6 Qt methods."""
    def __init__(self, tag, qt_widget):
        self.tag = tag
        self.raw = qt_widget  # The underlying PySide6 widget
        self._id = ""
        self._children = []

    # Property: id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
        _dom_registry[value] = self

    # Property: textContent
    @property
    def textContent(self):
        if hasattr(self.raw, "text"):
            return self.raw.text()
        return ""

    @textContent.setter
    def textContent(self, value):
        if hasattr(self.raw, "setText"):
            self.raw.setText(str(value))

    # Property: value (for inputs and sliders)
    @property
    def value(self):
        if isinstance(self.raw, QLineEdit):
            return self.raw.text()
        elif isinstance(self.raw, QSlider):
            return self.raw.value() / 10.0  # Decimals supported
        return None

    @value.setter
    def value(self, val):
        if isinstance(self.raw, QLineEdit):
            self.raw.setText(str(val))
        elif isinstance(self.raw, QSlider):
            self.raw.setValue(int(float(val) * 10))

    # Property: placeholder
    @property
    def placeholder(self):
        return self.raw.placeholderText() if hasattr(self.raw, "placeholderText") else ""

    @placeholder.setter
    def placeholder(self, text):
        if hasattr(self.raw, "setPlaceholderText"):
            self.raw.setPlaceholderText(str(text))

    # Event: onclick
    @property
    def onclick(self):
        return None

    @onclick.setter
    def onclick(self, callback_func):
        if hasattr(self.raw, "clicked"):
            self.raw.clicked.connect(callback_func)

    # Event: onchange / oninput
    @property
    def oninput(self):
        return None

    @oninput.setter
    def oninput(self, callback_func):
        if isinstance(self.raw, QLineEdit):
            self.raw.textChanged.connect(lambda text: callback_func(text))
        elif isinstance(self.raw, QSlider):
            self.raw.valueChanged.connect(lambda val: callback_func(val / 10.0))

    # Method: style
    def style(self, css_string):
        self.raw.setStyleSheet(css_string)


# ----
# HELPER FUNCTIONS (ce, ge, ba)
# ----

def ce(tag):
    """Create Element: ce('button'), ce('div'), ce('input'), ce('slider'), ce('text')"""
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
        w.setMaximum(100) # 0.0 to 10.0
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
    """Get Element by ID: ge('my_button')"""
    return _dom_registry.get(element_id, None)


def ba(child, parent=None):
    """Body Append / Append Child: ba(child) or ba(child, parent)"""
    target = parent if parent is not None else _main_container
    
    if hasattr(target, "layout") and target.layout is not None:
        target.layout.addWidget(child.raw)
    elif isinstance(target, QVBoxLayout):
        target.addWidget(child.raw)


def init_window(title="App Window", width=420, height=500):
    """Initializes the base dark window and body layout."""
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
    """Starts the application loop."""
    _root_window.show()
    sys.exit(_app_instance.exec())


# ----
# MAIN APPLICATION
# ----

init_window("Command Center", width=440, height=520)

# Create a Header
header = ce("text")
header.id = "main_heading"
header.textContent = "Telemetry Link Online"
header.style("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
ba(header)

# Create an Input
command_input = ce("input")
command_input.id = "user_input"
command_input.placeholder = "Enter station parameter..."
ba(command_input)

# Create a Float Slider (0.0 to 10.0 with 0.1 increments)
frequency_slider = ce("slider")
frequency_slider.id = "freq_ctrl"
frequency_slider.value = 5.0

def handle_slider(val):
    target = ge("status_display")
    if target:
        target.textContent = f"Current Frequency: {val:.1f} MHz"

frequency_slider.oninput = handle_slider
ba(frequency_slider)

# Status Output Text
status_label = ce("text")
status_label.id = "status_display"
status_label.textContent = "Current Frequency: 5.0 MHz"
status_label.style("color: #76c7c0; margin-top: 5px;")
ba(status_label)

# Create a Button
submit_btn = ce("button")
submit_btn.id = "transmit_btn"
submit_btn.textContent = "Transmit Command"

def handle_click():
    txt = ge("user_input").value
    freq = ge("freq_ctrl").value
    ge("status_display").textContent = f"Transmitted: '{txt}' at {freq:.1f} MHz"

submit_btn.onclick = handle_click
ba(submit_btn)

# Launch
run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

