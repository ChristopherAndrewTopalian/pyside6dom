# perimeter_of_a_rectangle.py

from pyside6dom import *

def calculate_rectangle_perimeter(length, width):
    try:
        perimeter = 2 * (float(length) + float(width))
        return perimeter
    except ValueError:
        print("Error: Could not convert input to a number.")
        return None

####

init_window("Perimeter of a Rectangle Calculator", 600, 450)

set_theme('''
    body {
        background-color: rgb(0, 0, 0);
        font-family: Arial;
        font-size: 20px;
        font-weight: bold;
        color: rgb(255, 255, 255);
    }

    input {
        padding: 2px 5px;
        font-size: 30px;
        font-weight: bold;
    }

    #perimeter_label
    {
        /*padding: 2px 40px;*/
    }
''')

perimeter_label = ce('div')
perimeter_label.id = 'perimeter_label'
perimeter_label.textContent = 'Perimeter of a Rectangle'
perimeter_label.style.fontSize = '32px'
perimeter_label.style.fontWeight = 'bold'
perimeter_label.style.color = 'rgb(0, 255, 255)'
perimeter_label.style.paddingLeft = '8px'
perimeter_label.style.marginBottom = '2px'
ba(perimeter_label)

####

length_input = ce('input')
length_input.placeholder = 'Enter Length...'
ba(length_input)

####

width_input = ce('input')
width_input.placeholder = 'Enter Width...'
ba(width_input)

####

enter_btn = ce('button')
enter_btn.textContent = 'Calculate perimeter'

def handle_click():
    length = length_input.value
    width = width_input.value
    
    # Safety Check: Don't calculate if the boxes are empty!
    if not length or not width: return
    
    perimeter = calculate_rectangle_perimeter(length, width)

    # make new element for this calculation
    history_entry = ce('p')
    history_entry.textContent = str(perimeter) + ' = ' + str(length) + ' x ' + str(width)
    history_entry.style.fontSize = '30px'
    history_entry.style.fontFamily = 'Impact'
    history_entry.style.border = '1px dashed rgb(255, 255, 255)'
    history_entry.style.paddingBottom = '5px'
    result_scroll_box.append(history_entry)

    # Clear both input boxes so they are ready for the next numbers
    length_input.value = ""
    width_input.value = ""
    # place mouse cursor in length input
    length_input.focus()

enter_btn.onclick = handle_click

# Hitting Enter inside either text box triggers the math
length_input.onenter = handle_click
width_input.onenter = handle_click

ba(enter_btn)

####

# The container that will hold our history
result_scroll_box = ce('scroll_div')
result_scroll_box.style.height = '250px'
result_scroll_box.style.border = '1px solid rgb(255, 255, 255)'
result_scroll_box.style.backgroundColor = 'rgb(0, 0, 0)'
result_scroll_box.style.marginTop = '10px'
result_scroll_box.style.padding = '5px'
ba(result_scroll_box)

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

