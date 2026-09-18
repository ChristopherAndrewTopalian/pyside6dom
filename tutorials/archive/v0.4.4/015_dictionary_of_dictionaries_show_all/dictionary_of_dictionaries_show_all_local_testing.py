# dictionary_of_dictionaries_show_all_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

people = {
    "jane_doe": {
        "first_name": "Jane",
        "last_name": "Doe",
        "score": 93
    },
    "joan_smith": {
        "first_name": "Joan",
        "last_name": "Smith",
        "score": 90
    },
    "melissa_taylor": {
        "first_name": "Melissa",
        "last_name": "Taylor",
        "score": 98
    },
    "jennifer_parker": {
        "first_name": "Jennifer",
        "last_name": "Parker",
        "score": 91
    },
    "tabitha_brooks": {
        "first_name": "Tabitha",
        "last_name": "Brooks",
        "score": 88
    },
    "sabrina_clark": {
        "first_name": "Sabrina",
        "last_name": "Clark",
        "score": 85
    },
    "nicole_morgan": {
        "first_name": "Nicole",
        "last_name": "Morgan",
        "score": 94
    },
    "britney_cooper": {
        "first_name": "Britney",
        "last_name": "Cooper",
        "score": 92
    },
    "zoe_baker": {
        "first_name": "Zoe",
        "last_name": "Baker",
        "score": 82
    },
    "clarissa_hayes": {
        "first_name": "Clarissa",
        "last_name": "Hayes",
        "score": 79
    },
    "bonnie_bell": {
        "first_name": "Bonnie",
        "last_name": "Bell",
        "score": 100
    }
}

init_window('Scores', 700, 600)

output_label = ce('text')
ba(output_label)

people_scroll_box = ce('scroll_div')
people_scroll_box.id = 'people_scroll_box'
people_scroll_box.style("border: 1px solid rgb(255, 255, 255);")
ba(people_scroll_box)

for person_key, person_data in people.items():
    name_btn = ce('button')
    # Display the properly capitalized first and last name on the button
    name_btn.textContent = f"{person_data['first_name']} {person_data['last_name']}: {person_data['score']}"
    name_btn.style("font-size: 25px; font-weight: bold; color: aqua;")

    # Freeze the lowercase key AND the inner dictionary data
    def handle_click(p_key=person_key, p_data=person_data):
        # Print the lowercase key first to prove we are pulling it from the top level
        print(f"Dictionary Key: '{p_key}' -> Student: {p_data['first_name']} {p_data['last_name']}, Score: {p_data['score']}")

        output_label.textContent = f"Dictionary Key: '{p_key}' -> Student: {p_data['first_name']} {p_data['last_name']}, Score: {p_data['score']}"

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

