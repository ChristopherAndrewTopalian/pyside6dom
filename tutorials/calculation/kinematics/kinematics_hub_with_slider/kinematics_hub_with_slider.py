# kinematics_hub.py

from pyside6dom import *

init_window("Kinematics Hub", 500, 680) # Made the window slightly taller

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    
    .hub_title {
        color: rgb(0, 255, 255);
        font-size: 28px;
        font-weight: bold;
        text-align: center; 
        margin-bottom: 20px;
    }
    
    .input_box { 
        width: 420px;
        padding: 12px; 
        font-size: 20px; 
        font-weight: bold;
        border: 2px solid rgb(80, 80, 90); 
        border-radius: 6px; 
        margin-bottom: 15px;
        color: white;
        background-color: rgb(30, 30, 40);
    }
    .input_box:focus { border: 2px solid rgb(0, 255, 200); }
    
    .dropdown_menu {
        width: 420px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        background-color: rgb(40, 40, 50);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 6px;
        margin-bottom: 25px;
    }
    
    .result_container {
        border: 1px solid rgb(60, 60, 80);
        background-color: rgb(15, 15, 18);
        border-radius: 8px;
        padding: 20px;
        width: 420px;
        margin-top: 10px;
    }
    
    .result_text {
        font-size: 24px;
        font-weight: bold;
        color: rgb(200, 200, 200);
        text-align: center; 
    }
    
    /* New Style for the Slider Label */
    .slider_label {
        color: rgb(150, 150, 150);
        font-size: 14px;
        text-align: center;
        margin-top: 20px;
    }
""")

def handle_mode_change():
    mode = ge('mode_select').value
    in1_lbl = ge('input1_label')
    in1 = ge('input1')
    in2_lbl = ge('input2_label')
    in2 = ge('input2')
    res = ge('result_label')
    speed_gauge = ge('speed_slider')

    in1.value = ""
    in2.value = ""
    speed_gauge.value = 0 # Reset the gauge!
    res.textContent = "Enter values to calculate..."
    res.style.color = 'rgb(200, 200, 200)'

    if mode == "Solve for Speed (MPH)":
        in1_lbl.textContent = "Distance (Miles)"
        in1.placeholder = "e.g., 15"
        in2_lbl.textContent = "Time (Minutes)"
        in2.placeholder = "e.g., 45"
    elif mode == "Solve for Distance (Miles)":
        in1_lbl.textContent = "Average Speed (MPH)"
        in1.placeholder = "e.g., 65"
        in2_lbl.textContent = "Time (Minutes)"
        in2.placeholder = "e.g., 120"
    elif mode == "Solve for Time (Minutes)":
        in1_lbl.textContent = "Distance (Miles)"
        in1.placeholder = "e.g., 15"
        in2_lbl.textContent = "Average Speed (MPH)"
        in2.placeholder = "e.g., 45"

def calculate_math():
    mode = ge('mode_select').value
    v1_text = ge('input1').value
    v2_text = ge('input2').value
    res = ge('result_label')
    speed_gauge = ge('speed_slider')

    try:
        val1 = float(v1_text)
        val2 = float(v2_text)
        
        current_speed = 0 # We will use this to set the slider

        if mode == "Solve for Speed (MPH)":
            if val2 <= 0: raise ValueError
            ans = val1 / (val2 / 60.0)
            res.textContent = f"Average Speed: {ans:.1f} mph"
            current_speed = ans
            
        elif mode == "Solve for Distance (Miles)":
            if val2 < 0: raise ValueError
            ans = val1 * (val2 / 60.0)
            res.textContent = f"Total Distance: {ans:.2f} miles"
            current_speed = val1 # The user inputted the speed in box 1
            
        elif mode == "Solve for Time (Minutes)":
            if val2 <= 0: raise ValueError
            total_mins = (val1 / val2) * 60.0
            if total_mins >= 60:
                res.textContent = f"Time: {int(total_mins // 60)} hr {int(total_mins % 60)} min"
            else:
                res.textContent = f"Time: {int(total_mins)} minutes"
            current_speed = val2 # The user inputted the speed in box 2

        res.style.color = 'rgb(0, 255, 200)'
        
        # Cap the visual slider at 120 mph so it doesn't break the UI
        speed_gauge.value = min(current_speed, 120) 

    except ValueError:
        speed_gauge.value = 0
        if not v1_text or not v2_text:
            res.textContent = "Enter values to calculate..."
            res.style.color = 'rgb(200, 200, 200)'
        else:
            res.textContent = "Invalid numbers"
            res.style.color = 'rgb(255, 80, 80)'


# (UI Building Code Stays the Same until the bottom)
title = ce('text')
title.className = 'hub_title'
title.textContent = "Kinematics Command Center"
ba(title)

mode_dropdown = ce('select')
mode_dropdown.id = 'mode_select'
mode_dropdown.className = 'dropdown_menu'
mode_dropdown.options = ["Solve for Speed (MPH)", "Solve for Distance (Miles)", "Solve for Time (Minutes)"]
mode_dropdown.oninput = handle_mode_change
ba(mode_dropdown)

in1_label = ce('text'); in1_label.id = 'input1_label'; in1_label.textContent = "Distance (Miles)"; ba(in1_label)
in1 = ce('input'); in1.id = 'input1'; in1.className = 'input_box'; in1.placeholder = "e.g., 15"; in1.oninput = calculate_math; ba(in1)

in2_label = ce('text'); in2_label.id = 'input2_label'; in2_label.textContent = "Time (Minutes)"; ba(in2_label)
in2 = ce('input'); in2.id = 'input2'; in2.className = 'input_box'; in2.placeholder = "e.g., 45"; in2.oninput = calculate_math; ba(in2)

res_container = ce('scroll_div')
res_container.className = 'result_container'
ba(res_container)

result_txt = ce('text')
result_txt.id = 'result_label'
result_txt.className = 'result_text'
result_txt.textContent = "Enter values to calculate..."
ba(result_txt, res_container)

####

# THE NEW SPEEDOMETER UI
slider_lbl = ce('text')
slider_lbl.className = 'slider_label'
slider_lbl.textContent = "0 mph ------------------------- Visual Speedometer ------------------------ 120 mph"
ba(slider_lbl)

speedometer = ce('slider')
speedometer.id = 'speed_slider'
# We access the raw Qt widget to adjust the max range to handle high speeds!
speedometer.raw.setMaximum(1200) # 1200 / 10 = 120 max value in your engine
speedometer.raw.setEnabled(False) # Prevents the user from manually dragging it
ba(speedometer)

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

