# calculate_time_minutes.pyw

from pyside6dom import *

def calculate_time_minutes(distance_miles, speed_mph):
    """
    Calculates Time in Minutes.
    Time = Distance / Speed
    The math naturally returns Hours, so we multiply by 60 for Minutes!
    """
    if speed_mph <= 0:
        raise ValueError("Speed must be greater than zero.")
    
    time_hours = distance_miles / speed_mph
    time_minutes = time_hours * 60.0
    
    return time_minutes

init_window("Time Calculator", 475, 420)

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
app_title.textContent = "Estimated Trip Time"
app_title.style.fontSize = '26px'
app_title.style.color = 'rgb(0, 255, 255)'
ba(app_title)

def update_result():
    d_text = ge('dist_val').value
    s_text = ge('speed_val').value

    try:
        dist_num = float(d_text)
        speed_num = float(s_text)

        total_mins = calculate_time_minutes(dist_num, speed_num)
        
        # UX MAGIC: Format the time like a real GPS!
        if total_mins >= 60:
            hrs = int(total_mins // 60)
            mins = int(total_mins % 60)
            time_string = f"{hrs} hr {mins} min"
        else:
            time_string = f"{int(total_mins)} minutes"

        result_box = ge('result_label')
        result_box.textContent = f"Time: {time_string}"
        result_box.style.color = 'rgb(0, 255, 255)'

    except ValueError:
        result_box = ge('result_label')
        if not d_text or not s_text:
            result_box.textContent = "Enter miles and speed..."
            result_box.style.color = 'rgb(200, 200, 200)'
        else:
            result_box.textContent = "Invalid numbers (Speed > 0)"
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

# Speed UI
speed_label = ce('text')
speed_label.textContent = 'Average Speed (MPH)'
ba(speed_label)

speed_input = ce('input')
speed_input.id = 'speed_val'
speed_input.placeholder = "e.g., 45 (mph)"
speed_input.oninput = update_result
ba(speed_input)

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
result_display.textContent = "Enter miles and speed..."
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

