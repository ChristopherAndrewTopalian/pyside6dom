# calculate_distance_miles.pyw

from pyside6dom import *

def calculate_distance_miles(speed_mph, time_minutes):
    """
    Calculates Distance in Miles.
    Distance = Speed * Time
    Automatically converts minutes into hours!
    """
    if time_minutes < 0:
        raise ValueError("Time cannot be negative.")
    
    # Convert minutes to hours
    time_hours = time_minutes / 60.0 
    
    return speed_mph * time_hours

init_window("Distance Calculator", 475, 420)

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
app_title.textContent = "Trip Distance (Miles)"
app_title.style.fontSize = '26px'
app_title.style.color = 'rgb(0, 255, 255)'
ba(app_title)

def update_result():
    s_text = ge('speed_val').value
    t_text = ge('time_val').value

    try:
        speed_num = float(s_text)
        time_num = float(t_text)

        distance = calculate_distance_miles(speed_num, time_num)

        result_box = ge('result_label')
        result_box.textContent = f"Total Distance: {distance:.2f} miles"
        result_box.style.color = 'rgb(0, 255, 255)'

    except ValueError:
        result_box = ge('result_label')
        if not s_text or not t_text:
            result_box.textContent = "Enter speed and minutes..."
            result_box.style.color = 'rgb(200, 200, 200)'
        else:
            result_box.textContent = "Invalid numbers"
            result_box.style.color = 'rgb(255, 80, 80)'

# Speed UI
speed_label = ce('text')
speed_label.textContent = 'Average Speed (MPH)'
ba(speed_label)

speed_input = ce('input')
speed_input.id = 'speed_val'
speed_input.placeholder = "e.g., 65 (mph)"
speed_input.oninput = update_result
ba(speed_input)

# Time UI
time_label = ce('text')
time_label.textContent = 'Time Traveled (Minutes)'
ba(time_label)

time_input = ce('input')
time_input.id = 'time_val'
time_input.placeholder = "e.g., 120 (minutes)"
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
result_display.textContent = "Enter speed and minutes..."
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

