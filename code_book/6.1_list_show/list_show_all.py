# list_show_all.py

from pyside6dom import *

init_window('List Show All', 700, 500)

people = [
    'Jane',
    'Joan',
    'Melissa',
    'Tabitha'
]

people_div = ce('div')
people_div.textContent = people
people_div.style.fontSize = '30px'
people_div.style.fontWeight = 'bold'
ba(people_div)

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

