# pyside6dom_example.py

from pyside6dom import *

init_window("Show Result", 600, 400)

number_input = ce('input')
number_input.placeholder = 'Enter number'
ba(number_input)

enter_btn = ce('button')
enter_btn.textContent = 'Enter'
def handle_click():
    print(number_input.value)
    ge('result_label').textContent = number_input.value
enter_btn.onclick = handle_click
ba(enter_btn)

result_label = ce('text')
result_label.id = 'result_label'
result_label.textContent = 'Result'
result_label.style("font-size: 30px; font-weight: bold")
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

