# list_make_buttons.py

from pyside6dom import *

init_window('List Show All', 700, 500)

people = [
    'Jane',
    'Joan',
    'Melissa',
    'Tabitha'
]

name_container = ce('scroll_div')
name_container.style.height = '200px'
ba(name_container)

for person in people:
    people_div = ce('button')
    people_div.textContent = person
    people_div.style.fontSize = '30px'
    people_div.style.fontWeight = 'bold'
    people_div.onclick = lambda p=person: print(p)
    name_container.append(people_div)

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

