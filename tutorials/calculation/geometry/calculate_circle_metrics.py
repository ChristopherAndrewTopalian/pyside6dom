# calculate_circle_metrics.py

import math
from pyside6dom import *

def get_circumference(radius):
    """ C = 2 * Pi * r """
    return 2 * math.pi * radius

def get_area(radius):
    """ A = Pi * r^2 """
    return math.pi * (radius ** 2)

####

init_window("Circle Geometry", 420, 400)

set_theme("""
    body { background-color: rgb(20, 25, 30); }
    input { 
        width: 300px; /* <--- THIS WILL NOW WORK IN YOUR UPDATED ENGINE! */
        padding: 10px; 
        font-size: 20px; 
        font-weight: bold;
        border: 2px solid rgb(100, 100, 150); 
        border-radius: 5px; 
        margin-bottom: 15px;
        color: rgb(255, 255, 255);
        background-color: rgb(30, 35, 45);
    }
    input:focus { border: 2px solid rgb(255, 100, 255); }
""")

# Title
app_title = ce('h1')
app_title.textContent = "Circle Engine"
app_title.style.color = 'rgb(255, 100, 255)' # Neon Pink/Purple theme for Geometry
ba(app_title)

def update_results():
    r_text = ge('radius_val').value

    try:
        radius_num = float(r_text)
        if radius_num < 0:
            raise ValueError("Radius cannot be negative")

        circ = get_circumference(radius_num)
        area = get_area(radius_num)

        ge('circ_label').textContent = f"Circumference: {circ:.2f}"
        ge('circ_label').style.color = 'rgb(0, 255, 200)'

        ge('area_label').textContent = f"Area: {area:.2f}"
        ge('area_label').style.color = 'rgb(0, 255, 200)'

    except ValueError:
        ge('circ_label').textContent = "Waiting for radius..."
        ge('circ_label').style.color = 'rgb(150, 150, 150)'
        ge('area_label').textContent = "Waiting for radius..."
        ge('area_label').style.color = 'rgb(150, 150, 150)'

# Input: Radius
radius_label = ce('text')
radius_label.textContent = 'Radius (distance from center to edge)'
radius_label.style.fontWeight = 'bold'
ba(radius_label)

radius_input = ce('input')
radius_input.id = 'radius_val'
radius_input.placeholder = "Enter radius (e.g., 5.5)"
radius_input.oninput = update_results
ba(radius_input)

# Display Container
result_box = ce('scroll_div')
result_box.style.border = '1px dashed rgb(100, 100, 150)'
result_box.style.padding = '15px'
# Testing the new engine style interception!
result_box.style.width = '300px'  
ba(result_box)

# Output: Circumference
circ_output = ce('text')
circ_output.id = 'circ_label'
circ_output.textContent = "Waiting for radius..."
circ_output.style.fontSize = '18px'
circ_output.style.fontWeight = 'bold'
ba(circ_output, result_box)

# Output: Area
area_output = ce('text')
area_output.id = 'area_label'
area_output.textContent = "Waiting for radius..."
area_output.style.fontSize = '18px'
area_output.style.fontWeight = 'bold'
ba(area_output, result_box)

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

