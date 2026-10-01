# move_div_left_right.py

from pyside6dom import *

init_window('OurApp', 700, 600)

energy_bar = ce('div')
energy_bar.id = 'energy_bar'
energy_bar.style.border = '1px solid rgb(255, 255, 255)'
energy_bar.style.width = 100
energy_bar.style.height = 100
energy_bar.style.position = 'absolute'
energy_bar.style.left = 0
energy_bar.style.top = 100
ba(energy_bar)

size_btn_container = ce('div')
size_btn_container.style.display = 'flex'
size_btn_container.style.flexDirection = 'row'
ba(size_btn_container)

move_left_btn = ce('button')
move_left_btn.textContent = 'Left'
def move_left():
    energy_bar.style.left -= 1
move_left_btn.onclick = move_left
size_btn_container.append(move_left_btn)

move_right_btn = ce('button')
move_right_btn.textContent = 'Right'
def move_right():
    energy_bar.style.left += 1
move_right_btn.onclick = move_right
size_btn_container.append(move_right_btn)

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

