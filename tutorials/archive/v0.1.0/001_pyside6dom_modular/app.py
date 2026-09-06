# app.py

# Import the custom DOM engine
from pyside6dom import ce, ge, ba, init_window, run_app

# Initialize the App
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

# Create a Float Slider
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

