# PySide6DOM 0.1.0
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

### 📂 Repository Structure

This repository includes two learning paths:

* **`001_pyside6dom/` (Modular / Production Ready):** Separates the heavy GUI engine into a background module (`pyside6dom_modular.py`) so your main application script remains incredibly clean.
* **`002_pyside6dom_single_file/` (Training Wheels):** Contains everything in a single script, allowing you to see exactly how the DOM wrappers interact with the raw PySide6 classes under the hood.

---

### 🚀 The Code: Web Logic meets Python Power

Look how clean and intuitive building a native desktop app becomes. No complex classes, no confusing layout managers - just straightforward DOM logic.

```python
from pyside6dom import ce, ge, ba, init_window, run_app

# Initialize the Application
init_window("Telemetry Station", width=440, height=520)

# Create a Header (createElement)
header = ce("text")
header.id = "main_heading"
header.textContent = "Telemetry Link Online"
header.style("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
ba(header) # (appendChild)

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

// https://github.com/ChristopherTopalian  
// https://github.com/ChristopherAndrewTopalian  

// https://sites.google.com/view/CollegeOfScripting

