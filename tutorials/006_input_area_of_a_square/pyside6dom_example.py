# pyside6dom_example.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 400)

area_label = ce('text')
area_label.textContent = 'Area of a Square Calculator'
area_label.style("font-size: 40px; font-weight: bold; color: rgb(0, 255, 255);")
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length'
ba(side_input)

enter_btn = ce('button')
enter_btn.textContent = 'Enter'
def handle_click():
    side = float(side_input.value)
    area = side * side
    ge('result_label').textContent = area
enter_btn.onclick = handle_click
ba(enter_btn)

result_label = ce('text')
result_label.id = 'result_label'
result_label.textContent = 'Result'
result_label.style("font-size: 40px; font-weight: bold")
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

