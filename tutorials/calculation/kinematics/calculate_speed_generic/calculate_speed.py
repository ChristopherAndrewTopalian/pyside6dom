# calculate_speed.py

from pyside6dom import *

def calculate_speed(distance, time):
    """
    Calculates velocity/speed given distance and time elapsed.
    Speed = Distance / Time
    """
    if time <= 0:
        raise ValueError("Time must be greater than zero.")
    return distance / time

####

init_window("Speed Calculator", 475, 420)

set_theme("""
    body { background-color: rgb(20, 20, 20); }
    input { 
        width: 400px;
        padding: 10px; 
        font-size: 20px; 
        font-weight: bold;
        border: 2px solid rgb(100, 100, 100); 
        border-radius: 5px; 
        margin-bottom: 12px;
        color: rgb(240, 240, 240);
        background-color: rgb(30, 30, 30);
    }
    input:focus { border: 2px solid rgb(0, 255, 255); }
""")

# Title
app_title = ce('h1')
app_title.textContent = "Speed & Velocity Engine"
app_title.style.fontSize = '26px'
app_title.style.fontWeight = 'bold'
app_title.style.marginBottom = '20px'
app_title.style.color = 'rgb(0, 255, 255)'
ba(app_title)

def update_result():
    d_text = ge('dist_val').value
    t_text = ge('time_val').value

    try:
        dist_num = float(d_text)
        time_num = float(t_text)

        speed = calculate_speed(dist_num, time_num)

        result_box = ge('result_label')
        result_box.textContent = f"Velocity: {speed:.2f} units/hr"
        result_box.style.color = 'rgb(0, 255, 255)'

    except ValueError:
        result_box = ge('result_label')
        if not d_text or not t_text:
            result_box.textContent = "Enter distance and time..."
            result_box.style.color = 'rgb(200, 200, 200)'
        else:
            result_box.textContent = "Time must be > 0"
            result_box.style.color = 'rgb(255, 80, 80)'

distance_label = ce('text')
distance_label.textContent = 'Distance'
ba(distance_label)

# Input: Distance
distance_input = ce('input')
distance_input.id = 'dist_val'
distance_input.placeholder = "Distance (e.g., 300 km or miles)"
distance_input.oninput = update_result
ba(distance_input)

time_label = ce('text')
time_label.textContent = 'Time'
ba(time_label)

# Input: Time
time_input = ce('input')
time_input.id = 'time_val'
time_input.placeholder = "Time elapsed (e.g., 4.5 hours)"
time_input.oninput = update_result
ba(time_input)

# Result Container
result_scroll_div = ce('scroll_div')
result_scroll_div.style.border = '1px solid rgb(80, 80, 80)'
result_scroll_div.style.borderRadius = '5px'
result_scroll_div.style.padding = '10px'
result_scroll_div.style.width = '400px'
ba(result_scroll_div)

# Result Display
result_display = ce('text')
result_display.id = 'result_label'
result_display.textContent = "Enter distance and time..."
#result_display.style.width = '300px'
result_display.style.border = 'none'
result_display.style.fontSize = '22px'
result_display.style.fontWeight = 'bold'
result_display.style.color = 'rgb(200, 200, 200)'
ba(result_display, result_scroll_div)

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

