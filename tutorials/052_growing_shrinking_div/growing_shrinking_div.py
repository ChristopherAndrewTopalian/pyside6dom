# growing_shrinking_div.py

from pyside6dom import *

init_window('OurApp', 700, 600)

energy_bar = ce('div')
energy_bar.id = 'energy_bar'
energy_bar.style.border = '1px solid rgb(255, 255, 255)'
energy_bar.style.width = 100
energy_bar.style.height = 100
ba(energy_bar)

size_btn_container = ce('div')
size_btn_container.style.display = 'flex'
size_btn_container.style.flexDirection = 'row'
ba(size_btn_container)

shrink_btn = ce('button')
shrink_btn.textContent = 'Shrink'
def handle_shrink():
    energy_bar.width -= 1
shrink_btn.onclick = handle_shrink
size_btn_container.append(shrink_btn)

grow_btn = ce('button')
grow_btn.textContent = 'Grow'
def handle_grow():
    energy_bar.width += 1
grow_btn.onclick = handle_grow
size_btn_container.append(grow_btn)

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

