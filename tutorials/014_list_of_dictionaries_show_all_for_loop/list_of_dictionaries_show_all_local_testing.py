# list_of_dictionaries_show_all_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

people = [
    {
        "name": "Jane",
        "score": 93
    },

    {
        "name": "Joan",
        "score": 90
    },

    {
        "name": "Melissa",
        "score": 98
    },

    {
        "name": "Jennifer",
        "score": 91
    },

    {
        "name": "Tabitha",
        "score": 88
    },

    {
        "name": "Sabrina",
        "score": 85
    },

    {
        "name": "Nicole",
        "score": 94
    },

    {
        "name": "Britney",
        "score": 92
    },

    {
        "name": "Zoe",
        "score": 82
    },

    {
        "name": "Clarissa",
        "score": 79
    },

    {
        "name": "Bonnie",
        "score": 100
    },
]

init_window('Scores', 700, 500)

output_label = ce('text')
output_label.style('font-size: 30px; font-weight: bold')
ba(output_label)

people_scroll_box = ce('scroll_div')
people_scroll_box.id = 'people_scroll_box'
people_scroll_box.style("border: 1px solid rgb(255, 255, 255);")
ba(people_scroll_box)

for person in people:
    name_btn = ce('button')
    name_btn.textContent = f"{person['name']}: {person['score']}"
    name_btn.style("font-size: 30px; font-weight: bold; color: aqua;")
    # we can type color or font-color, either is fine

    # Freeze the current person into a local variable 'p'
    def handle_click(p=person):
        print(f"{p['name']}: {p['score']}")
        output_label.textContent = f"{p['name']}: {p['score']}"
        
    name_btn.onclick = handle_click
    ba(name_btn, people_scroll_box)

####

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

