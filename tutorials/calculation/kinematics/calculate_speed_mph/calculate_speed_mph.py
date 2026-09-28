# calculate_speed_mph.py

from pyside6dom import *

def calculate_speed_mph(distance_miles, time_minutes):
    """
    Calculates Speed in Miles Per Hour (mph).
    Automatically converts minutes into hours behind the scenes!
    """
    if time_minutes <= 0:
        raise ValueError("Time must be greater than zero.")
    
    # Convert minutes to hours
    time_hours = time_minutes / 60.0 
    
    return distance_miles / time_hours

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
app_title.textContent = "Commute Speed (MPH)"
app_title.style.fontSize = '26px'
app_title.style.color = 'rgb(0, 255, 255)'
ba(app_title)

def update_result():
    d_text = ge('dist_val').value
    t_text = ge('time_val').value

    try:
        dist_num = float(d_text)
        time_num = float(t_text)

        # Call our updated MPH calculator
        speed = calculate_speed_mph(dist_num, time_num)

        result_box = ge('result_label')
        result_box.textContent = f"Average Speed: {speed:.1f} mph"
        result_box.style.color = 'rgb(0, 255, 255)'

    except ValueError:
        result_box = ge('result_label')
        if not d_text or not t_text:
            result_box.textContent = "Enter miles and minutes..."
            result_box.style.color = 'rgb(200, 200, 200)'
        else:
            result_box.textContent = "Time must be > 0"
            result_box.style.color = 'rgb(255, 80, 80)'

# Distance UI
distance_label = ce('text')
distance_label.textContent = 'Distance (Miles)'
ba(distance_label)

distance_input = ce('input')
distance_input.id = 'dist_val'
distance_input.placeholder = "e.g., 15 (miles)"
distance_input.oninput = update_result
ba(distance_input)

# Time UI
time_label = ce('text')
time_label.textContent = 'Time (Minutes)'
ba(time_label)

time_input = ce('input')
time_input.id = 'time_val'
time_input.placeholder = "e.g., 45 (minutes)"
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
result_display.textContent = "Enter miles and minutes..."
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

