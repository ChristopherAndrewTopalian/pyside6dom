# area_of_square_calculator.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 450)

area_label = ce('h1')
area_label.textContent = 'Area of a Square'
area_label.style.fontSize = '32px'
area_label.style.fontWeight = 'bold'
area_label.style.color = 'rgb(0, 255, 255)'
area_label.style.marginBottom = '10px'
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length...'
ba(side_input)

enter_btn = ce('button')
enter_btn.textContent = 'Calculate Area'
def handle_click():
    # Grab and calculate
    side = float(side_input.value)
    area = side * side

    # Create a brand new element for this specific calculation
    history_entry = ce('p')
    history_entry.textContent = f"Side: {side}  →  Area: {area}"
    history_entry.style.fontSize = '18px'
    history_entry.style.color = 'rgb(0, 255, 255)'
    history_entry.style.fontFamily = 'Arial'
    history_entry.style.borderBottom = '1px dashed rgb(255, 255, 255)'
    history_entry.style.paddingBottom = '5px'
    result_scroll_box.append(history_entry)

    # Clear the input box so it is ready for the next number
    side_input.value = ""

enter_btn.onclick = handle_click
ba(enter_btn)

# The container that will hold our history
result_scroll_box = ce('scroll_div')
result_scroll_box.style.height = '200px'
result_scroll_box.style.border = '1px solid rgb(255, 255, 255)'
result_scroll_box.style.backgroundColor = 'rgb(0, 0, 0)'
result_scroll_box.style.marginTop = '10px'
result_scroll_box.style.padding = '5px'
#result_scroll_box.style("min-height: 50px; border: 1px solid rgb(255, 255, 255); background-color: rgb(0, 0, 0); margin-top: 10px; padding: 5px;")
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

