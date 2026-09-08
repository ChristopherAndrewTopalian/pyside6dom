# pyside6dom_stopwatch.py

from pyside6dom import *

# worldwide CSS style

set_theme("""
    body {
        background-color: #1a1a1a;
    }
    text {
        color: rgb(0, 255, 255);
        qproperty-alignment: AlignCenter;
    }
    button {
        background-color: #333333;
        color: rgb(255, 255, 255);
        border: 1px solid rgb(0, 255, 255);
        border-radius: 5px;
        padding: 8px;
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
    }
    button:hover {
        background-color: rgb(0, 255, 255);
        color: rgb(0, 0, 0);
    }
""")

####

def start_clock():
    global timer_id, is_running
    # Only start if it isn't already running, to prevent runaway timers
    if not is_running:
        timer_id = setInterval(tick, 100) # Run every 100 milliseconds
        is_running = True

def format_time(t):
    minutes = t // 600
    seconds = (t // 10) % 60
    tenths = t % 10
    # The :02d forces numbers to have a leading zero (e.g., 05 instead of 5)
    return f"{minutes:02d}:{seconds:02d}:{tenths}"

def tick():
    global tenths_of_second
    tenths_of_second += 1
    time_display.textContent = format_time(tenths_of_second)

def stop_clock():
    global timer_id, is_running
    if is_running:
        clearInterval(timer_id)
        is_running = False

def reset_clock():
    global tenths_of_second
    stop_clock() # Stop the timer first
    tenths_of_second = 0 # Reset the math
    time_display.textContent = "00:00:0" # Reset the screen

####

init_window("Stopwatch", 350, 450)

# The User Interface
theTitle = ce('text')
theTitle.textContent = "Stopwatch"
theTitle.style("font-size: 28px; font-weight: bold; margin-top: 10px;")
ba(theTitle)

time_display = ce('text')
time_display.textContent = "00:00:0"
time_display.style("font-size: 55px; font-family: monospace; margin-top: 20px; margin-bottom: 20px;")
ba(time_display)

start_btn = ce('button')
start_btn.textContent = "Start"
start_btn.onclick = start_clock
ba(start_btn)

stop_btn = ce('button')
stop_btn.textContent = "Stop"
stop_btn.onclick = stop_clock
ba(stop_btn)

reset_btn = ce('button')
reset_btn.textContent = "Reset"
reset_btn.onclick = reset_clock
ba(reset_btn)

# The Application Logic
tenths_of_second = 0
timer_id = None
is_running = False

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
# GitHub: https://github.com/ChristopherAndrewTopalian/pyside6dom
#
# PyPI: https://pypi.org/project/pyside6dom/
#
# GitHub: https://github.com/ChristopherAndrewTopalian
#
# GitHub: https://github.com/ChristopherTopalian
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting

