# PySide6DOM
**Bring the simplicity of the Web DOM to Python PySide6 Desktop Applications.**

## Installation
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

### How to Download this Package
1. Click the green Code Button on this github page
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

