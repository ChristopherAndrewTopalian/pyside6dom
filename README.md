# PySide6DOM v0.1.5
**Bring the simplicity of the Web DOM to Python PySide6 Desktop Applications.**

# Installation
```bash
pip install pyside6dom
```

**PySide6DOM** bridges the gap between web development and systems programming. It wraps the raw power of the PySide6 (C++/Qt) rendering engine inside the familiar, intuitive Document Object Model (DOM) paradigm used by JavaScript and HTML.

If you know how to build a web page using `createElement`, `getElementById`, and `appendChild`, you already know how to build high-performance, standalone Python desktop applications.

### 🌟 Why Use PySide6DOM?

* **Zero HTML Parsing:** This is not a web view or a browser wrapper. It generates native C++/Qt desktop widgets using Python, ensuring maximum performance.
* **Familiar Syntax:** Uses lightweight helper functions modeled directly after the web DOM (`ce()` for create element, `ge()` for get element, `ba()` for body append).
* **Rapid Prototyping:** Build user interfaces in seconds without getting bogged down in complex object-oriented boilerplate.
* **Educational Bridge:** The perfect stepping stone for web developers transitioning into local hardware control, computer vision, and systems engineering.

---

### 🚀 The Code: Web Logic meets Python Power

Look how clean and intuitive building a native desktop app becomes. No complex classes, no confusing layout managers - just straightforward DOM logic.

```python
from pyside6dom import *

# Initialize the Application
init_window("Telemetry Station", width=440, height=520)

# Create a Header (createElement)
header = ce("text")
header.id = "main_heading"
header.textContent = "Telemetry Link Online"
header.style("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
ba(header) # (appendChild)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
ba(welcomeMessage)

# Create an Input Field
command_input = ce("input")
command_input.id = "user_input"
command_input.placeholder = "Enter station parameter..."
ba(command_input)

# Create an Interactive Button
submit_btn = ce("button")
submit_btn.textContent = "Transmit Command"

# Define what happens on click
def handle_click():
    txt = ge("user_input").value
    welcomeMessage.textContent = txt
    print(f"Transmitting Data: {txt}")

submit_btn.onclick = handle_click
ba(submit_btn)

# Launch the App
run_app()

```

---

### 🛠️ Core API Reference

| Function | Web Equivalent | Description |
| --- | --- | --- |
| `ce(tag)` | `document.createElement()` | Creates a new native widget. Supports: `"button"`, `"text"`, `"input"`, `"slider"`, `"div"`, `"scroll_div"`. |
| `ge(id)` | `document.getElementById()` | Retrieves a previously created element by its unique `.id` property. |
| `ba(element)` | `document.body.appendChild()` | Appends the element to the main application window (or a specific parent container). |

---

**Created by Christopher Andrew Topalian**

*College of Scripting Music & Science*

> *Disclaimer: This is an independent open-source educational project. "PySide" and "Qt" are registered trademarks of The Qt Company. This project is not affiliated with, endorsed by, or sponsored by The Qt Company.*

---

```python
# pyside6dom_example.py

# after we have installed pyside6dom using
# pip install pyside6dom

from pyside6dom import *

# Initialize the Application
init_window("PySide6DOM Feature Showcase", width=450, height=650)

# Worldwide Header
header = ce("h1")
header.textContent = "🚀 Mission Control"
header.style("font-size: 24px; color: #00ffcc; font-weight: bold; margin-bottom: 20px;")
ba(header)

# Text Input with Real-Time 'oninput' Event
pilot_input = ce("input")
pilot_input.id = "pilot_name"
pilot_input.placeholder = "Enter Pilot Name..."
pilot_input.style("padding: 10px; font-size: 14px; border: 2px solid #555; border-radius: 5px;")
ba(pilot_input)

# Live feedback label for the input
typing_echo = ce("text")
typing_echo.id = "echo_label"
typing_echo.textContent = "Awaiting pilot identification..."
typing_echo.style("color: #aaaaaa; font-style: italic; margin-bottom: 20px;")
ba(typing_echo)

def on_type(text):
    ge("echo_label").textContent = f"Live typing: {text}"
pilot_input.oninput = on_type

# Slider with Real-Time 'oninput' Event
throttle_label = ce("text")
throttle_label.id = "throttle_display"
throttle_label.textContent = "Engine Throttle: 0%"
throttle_label.style("font-size: 16px; font-weight: bold; margin-top: 10px;")
ba(throttle_label)

throttle_slider = ce("slider")
throttle_slider.id = "throttle"
# The slider scales 0-100 under the hood based on our ce() setup
def on_slide(val):
    # val comes in as a float from our parser, we multiply back for display
    ge("throttle_display").textContent = f"Engine Throttle: {int(val * 10)}%"
throttle_slider.oninput = on_slide
ba(throttle_slider)

# Nested Containers (Div) for layout grouping
action_panel = ce("div")
action_panel.style("background-color: #222; border-radius: 8px; padding: 15px; margin-top: 20px;")
ba(action_panel)

# Interactive Button with rich CSS pseudo-states inside the Div
submit_btn = ce("button")
submit_btn.textContent = "ENGAGE THRUSTERS"
submit_btn.style("""
    QPushButton { 
        background-color: #007acc; 
        color: white; 
        border-radius: 6px; 
        padding: 12px; 
        font-size: 16px; 
        font-weight: bold;
    }
    QPushButton:hover { background-color: #0099ff; }
    QPushButton:pressed { background-color: #005c99; }
""")
ba(submit_btn, action_panel) # Appended to action_panel, NOT the main window

# Scrolling Log Window (scroll_div) for dynamic output
log_title = ce("h1")
log_title.textContent = "System Logs:"
log_title.style("margin-top: 20px; font-size: 14px; color: #888;")
ba(log_title)

log_window = ce("scroll_div")
log_window.style("background-color: #0a0a0a; border: 1px solid #333; min-height: 150px;")
ba(log_window)

# Button Click Event (Gathering data via 'ge' and appending to scroll_div)
def handle_engage():
    # Grab values from the registry
    pilot = ge("pilot_name").value or "Unknown Pilot"
    throttle = ge("throttle").value * 10

    # Create a new dynamic log entry
    log_entry = ce("p")
    log_entry.textContent = f"> {pilot} engaged engines at {int(throttle)}%"
    log_entry.style("color: #00ff00; font-family: monospace; font-size: 13px; margin: 2px;")

    # Append the new text directly into the scrolling window
    ba(log_entry, log_window)

submit_btn.onclick = handle_engage

# Launch the App
run_app()
```
---

# pyside6dom 0.1.2

A pure, web-style Document Object Model (DOM) interface for building PySide6 desktop applications natively in Python. Write desktop GUIs using the web syntax you already know.

### Installation
```bash
pip install pyside6dom

```

---

## 📖 API Reference Key

**Core Functions:**

* `ce(tag)`: Create Element. Returns a new DOMElement.
* `ge(id)`: Get Element. Retrieves an element by its `.id`.
* `ba(child, parent=None)`: Append Child. Adds an element to the layout.
* `set_global_style(css)`: Applies a universal CSS stylesheet to the entire app.
* `init_window(title, width, height)`: Initializes the PySide6 application.
* `run_app()`: Starts the event loop.

**Supported Tags & Properties:**

* **`text`, `p`, `h1`, `span`**: `.textContent`
* **`button`**: `.textContent`, `.onclick`
* **`input`**: `.value`, `.placeholder`, `.oninput`
* **`slider`**: `.value`, `.oninput`
* **`checkbox`** *(New!)*: `.checked`, `.textContent`, `.oninput`
* **`select`, `dropdown**` *(New!)*: `.options` (list), `.value` (current text), `.oninput`
* **`div`**: Standard container for grouping elements.
* **`scroll_div`**: A vertically scrolling container for dynamic content.

*All elements support `.id` and inline `.style("css_string")`.*

---

## 🚀 Quickstart Example: Settings Panel

This example demonstrates global CSS styling, checkboxes, dropdowns, and real-time event handling using pure DOM syntax.

```python
from pyside6dom import *

# Initialize Window
init_window("Settings Panel", width=400, height=500)

# Global Stylesheet (CSS)
set_global_style("""
    QWidget {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    QLabel#title_heading {
        font-size: 22px;
        font-weight: bold;
        color: #00ffcc;
        margin-bottom: 10px;
    }
    QPushButton {
        background-color: #007acc;
        color: white;
        border-radius: 4px;
        padding: 10px;
        font-weight: bold;
        margin-top: 15px;
    }
    QPushButton:hover { background-color: #0099ff; }
    QPushButton:pressed { background-color: #005c99; }
    
    QComboBox {
        padding: 6px;
        background-color: #2b2b2b;
        border: 1px solid #555;
        border-radius: 3px;
    }
    QComboBox QAbstractItemView {
        background-color: #2b2b2b;
        selection-background-color: #007acc;
        selection-color: white;
    }
    QScrollArea {
        border: 1px solid #444;
        background-color: #111;
        margin-top: 10px;
    }
""")

# Build the UI
header = ce("h1")
header.id = "title_heading"
header.textContent = "⚙️ Settings Panel"
ba(header)

mode_label = ce("text")
mode_label.textContent = "Select Operating Mode:"
ba(mode_label)

mode_select = ce("select")
mode_select.id = "app_mode"
mode_select.options = ["Standard", "Advanced", "Developer"]
ba(mode_select)

debug_checkbox = ce("checkbox")
debug_checkbox.id = "debug_flag"
debug_checkbox.textContent = "Enable Debug Logging"
debug_checkbox.checked = True
ba(debug_checkbox)

apply_btn = ce("button")
apply_btn.textContent = "Apply Settings"
ba(apply_btn)

log_window = ce("scroll_div")
ba(log_window)

# Handle Events
def handle_apply():
    selected = ge("app_mode").value
    debug = ge("debug_flag").checked
    
    log = ce("p")
    log.textContent = f"> Mode: {selected} | Debug: {debug}"
    log.style("color: #00ff00; font-family: monospace;")
    ba(log, log_window)

apply_btn.onclick = handle_apply

# Launch
run_app()

```

---

## Here is another example:

```python
# pyside6dom_example.py

import sys
import os

from pyside6dom import *

init_window("Settings Panel", width=400, height=500)

# ===================================== #
#         WORLDWIDE STYLESHEET (CSS)
# ===================================== #
set_global_style("""
    QWidget {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    QLabel {
        padding-top: 5px;
    }
    QLabel#title_heading {
        font-size: 22px;
        font-weight: bold;
        color: #00ffcc;
        margin-bottom: 10px;
    }
    QPushButton {
        background-color: #007acc;
        color: white;
        border-radius: 4px;
        padding: 10px;
        font-weight: bold;
        margin-top: 15px;
    }
    QPushButton:hover { background-color: #0099ff; }
    QPushButton:pressed { background-color: #005c99; }
    
    QComboBox {
        padding: 6px;
        background-color: #2b2b2b;
        border: 1px solid #555;
        border-radius: 3px;
    }
    /* This fixes the missing hover highlight in dropdowns! */
    QComboBox QAbstractItemView {
        background-color: #2b2b2b;
        selection-background-color: #007acc;
        selection-color: white;
    }
    
    QScrollArea {
        border: 1px solid #444;
        background-color: #111;
        margin-top: 10px;
    }
""")

# ===================================== #
#               UI BUILDER
# ===================================== #

header = ce("h1")
header.id = "title_heading"
header.textContent = "⚙️ Settings Panel"
ba(header)

mode_label = ce("text")
mode_label.textContent = "Select Operating Mode:"
ba(mode_label)

mode_select = ce("select")
mode_select.id = "app_mode"
mode_select.options = ["Standard", "Advanced", "Developer"]
ba(mode_select)

debug_checkbox = ce("checkbox")
debug_checkbox.id = "debug_flag"
debug_checkbox.textContent = "Enable Debug Logging"
debug_checkbox.checked = True
ba(debug_checkbox)

apply_btn = ce("button")
apply_btn.textContent = "Apply Settings"
ba(apply_btn)

log_window = ce("scroll_div")
ba(log_window)

def handle_apply():
    selected = ge("app_mode").value
    debug = ge("debug_flag").checked
    
    log = ce("p")
    log.textContent = f"> Mode: {selected} | Debug: {debug}"
    log.style("color: #00ff00; font-family: monospace;") # Inline overrides still work!
    ba(log, log_window)

apply_btn.onclick = handle_apply

run_app()
```

---

## Easy Example: 

```python
# pyside6dom_easy_example.py

from pyside6dom import *

init_window("Our App", width = 600, height = 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
ba(welcomeMessage)

sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click
ba(sayHiBtn)

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click
ba(sayHowdyBtn)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'This'
def handle_click(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click('Hey Now')
ba(sayThisBtn)

run_app()
```

---

## Scrollable Div Example:

```python
# pyside6dom_scroll_box_example.py

from pyside6dom import *

init_window("Our App", width = 600, height = 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
welcomeMessage.style("font-size: 30px; font-weight: bold;")
ba(welcomeMessage)

# Create a specific scrollable container for the buttons
messageBtns_scroll_box = ce('scroll_div')
messageBtns_scroll_box.style("border: 2px solid #555; background-color: #1a1a1a; min-height: 200px;")
ba(messageBtns_scroll_box)

# Create buttons and append them TO the scroll box
sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click_hi():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click_hi
ba(sayHiBtn, messageBtns_scroll_box) # Notice the second argument

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click_howdy():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click_howdy
ba(sayHowdyBtn, messageBtns_scroll_box)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'This'
def handle_click_message(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click_message('Hey Now')
ba(sayThisBtn, messageBtns_scroll_box)

run_app()
```

---

COMMON COMMANDS:
### Install:
> pip install pyside6dom

### Upgrade: 
> pip install --upgrade pyside6dom

---

# MORE EXAMPLES:

```python
# pyside6dom_example.py

from pyside6dom import *

init_window("Round", 600, 400)

number_input = ce('input')
number_input.placeholder = 'Enter number'
ba(number_input)

enter_btn = ce('button')
enter_btn.textContent = 'Enter'
def handle_click():
    print(number_input.value)
    ge('result_label').textContent = number_input.value
enter_btn.onclick = handle_click
ba(enter_btn)

result_label = ce('text')
result_label.id = 'result_label'
result_label.textContent = 'Result'
result_label.style("font-size: 30px; font-weight: bold")
ba(result_label)

run_app()
```

---

```python
# pyside6dom_example.py

from pyside6dom import *

init_window("Area of Square Calculator", 600, 400)

area_label = ce('text')
area_label.textContent = 'Area of a Square Calculator'
area_label.style("font-size: 40px; font-weight: bold; color: rgb(0, 255, 255);")
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length'
ba(side_input)

enter_btn = ce('button')
enter_btn.textContent = 'Enter'
def handle_click():
    side = float(side_input.value)
    area = side * side
    ge('result_label').textContent = area
enter_btn.onclick = handle_click
ba(enter_btn)

result_label = ce('text')
result_label.id = 'result_label'
result_label.textContent = 'Result'
result_label.style("font-size: 40px; font-weight: bold")
ba(result_label)

run_app()
```

---

```python
# pyside6dom_example.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 450)

area_label = ce('h1')
area_label.textContent = 'Area of a Square'
area_label.style("font-size: 32px; font-weight: bold; color: rgb(0, 255, 255); margin-bottom: 10px;")
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length...'
ba(side_input)

enter_btn = ce('button')
enter_btn.textContent = 'Calculate Area'
def handle_click():
    # Grab and calculate
    side = float(side_input.value)
    area = side * side

    # Create a brand new element for this specific calculation
    history_entry = ce('p')
    history_entry.textContent = f"Side: {side}  →  Area: {area}"
    history_entry.style("font-size: 18px; color: rgb(0, 255, 255); font-family: Arial; border-bottom: 1px dashed rgb(255, 255, 255); padding-bottom: 5px;")

    # Append the new element directly into the scroll box
    ba(history_entry, result_scroll_box)

    # Clear the input box so it is ready for the next number
    side_input.value = ""

enter_btn.onclick = handle_click
ba(enter_btn)

# The container that will hold our history
result_scroll_box = ce('scroll_div')
result_scroll_box.style("min-height: 50px; border: 1px solid rgb(255, 255, 255); background-color: rgb(0, 0, 0); margin-top: 10px; padding: 5px;")
ba(result_scroll_box)

run_app()
```

---

https://github.com/ChristopherAndrewTopalian/pyside6dom

### How to Download the GitHub Repository
1. Click the green Code Button on the GitHub page
2. Choose Download ZIP
3. Save the Zip File
4. Extract All

---

Hapy Scripting :-)

---

//----//

// Dedicated to God the Father  

// Copyright (c) 2026-present Christopher Andrew Topalian  
   
// Apache License
   Version 2.0, January 2004
   http://www.apache.org/licenses/  

// GitHub: https://github.com/ChristopherAndrewTopalian/pyside6dom

// PyPI: https://pypi.org/project/pyside6dom/

// https://github.com/ChristopherAndrewTopalian  

// https://github.com/ChristopherTopalian  

// https://sites.google.com/view/CollegeOfScripting

