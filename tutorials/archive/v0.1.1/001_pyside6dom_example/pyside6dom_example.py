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

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

