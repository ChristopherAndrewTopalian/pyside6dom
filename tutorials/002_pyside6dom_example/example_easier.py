# pyside6dom_example.py

from pyside6dom import *

init_window("Settings Panel", 400, 500)

# ===
#   WORLDWIDE STYLESHEET (CSS)
# ===
set_theme("""
    div {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    text {
        padding-top: 5px;
    }
    text#title_heading {
        font-size: 22px;
        font-weight: bold;
        color: #00ffcc;
        margin-bottom: 10px;
    }
    button {
        background-color: #007acc;
        color: white;
        border-radius: 4px;
        padding: 10px;
        font-weight: bold;
        margin-top: 15px;
    }
    button:hover { background-color: #0099ff; }
    button:pressed { background-color: #005c99; }
    
    select {
        padding: 6px;
        background-color: #2b2b2b;
        border: 1px solid #555;
        border-radius: 3px;
    }
    /* This fixes the missing hover highlight in dropdowns! */
    select option {
        background-color: #2b2b2b;
        selection-background-color: #007acc;
        selection-color: white;
    }
    
    scroll_div {
        border: 1px solid #444;
        background-color: #111;
        margin-top: 10px;
    }
""")

# ===
#  UI BUILDER
# ===

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
    log.style("color: #00ff00; font-family: monospace;") # Inline overrides still work
    ba(log, log_window)

apply_btn.onclick = handle_apply

run_app()

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

