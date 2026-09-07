# pyside6dom_example.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 450)

area_label = ce('h1')
area_label.textContent = 'Area of a Square'
area_label.style("font-size: 32px; font-weight: bold; color: rgb(0, 255, 255); margin-bottom: 10px;")
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
    history_entry.style("font-size: 18px; color: rgb(0, 255, 255); font-family: Arial; border-bottom: 1px dashed rgb(255, 255, 255); padding-bottom: 5px;")

    # Append the new element directly into the scroll box
    ba(history_entry, result_scroll_box)

    # Clear the input box so it is ready for the next number
    side_input.value = ""

enter_btn.onclick = handle_click
ba(enter_btn)

# The container that will hold our history
result_scroll_box = ce('scroll_div')
result_scroll_box.style("min-height: 50px; border: 1px solid rgb(255, 255, 255); background-color: rgb(0, 0, 0); margin-top: 10px; padding: 5px;")
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

