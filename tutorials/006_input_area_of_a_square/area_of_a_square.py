# area_of_a_square.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 400)

set_theme('''
    input
    {
        margin: 2px;
        padding: 2px 5px;
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
    }

    #result_label
    {
        margin: 2px;
    }
    button
    {
        background-color: rgb(0, 0, 0);
        border: 1px solid rgb(255, 255, 255);
        color: rgb(255, 255, 255);
    }
    button:hover
    {
        border-color: aqua;
    }
    button:active
    {
        color: rgb(255, 0, 255);
    }
''')

area_label = ce('div')
area_label.textContent = 'Area of a Square Calculator'
area_label.style.padding = '2px 10px'
area_label.style.fontSize = '40px'
area_label.style.fontWeight = 'bold'
area_label.style.color = 'rgb(0, 255, 255)'
#area_label.style("font-size: 40px; font-weight: bold; color: rgb(0, 255, 255);")
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length'
def q():
    ge('enter_btn').click()
    side_input.value = ''
side_input.onenter = q
ba(side_input)

enter_btn = ce('button')
enter_btn.id = 'enter_btn'
enter_btn.textContent = 'Enter'
def q():
    side = float(side_input.value)
    area = side * side
    ge('result_label').textContent = area
    side_input.value = ''
enter_btn.onclick = q
ba(enter_btn)

result_label = ce('div')
result_label.id = 'result_label'
result_label.textContent = 'Result'
result_label.style.fontSize = '40px'
result_label.style.fontWeight = 'bold'
result_label.style.padding = '2px 4px'
#result_label.style("font-size: 40px; font-weight: bold")
ba(result_label)

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

