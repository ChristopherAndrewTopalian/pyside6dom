# how_many_in_list.py

from pyside6dom import *

init_window('OurApp', 700, 600)

people = [
    "Jane",
    "Joan",
    "Melissa",
    "Tabitha"
]

how_many_here = ce('div')
how_many_here.textContent = str(len(people)) + ' people are here'
ba(how_many_here)

who_is_here = ce('div')
who_is_here.textContent = people
ba(who_is_here)

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

