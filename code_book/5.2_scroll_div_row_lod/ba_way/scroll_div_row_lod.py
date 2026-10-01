# scroll_div_row_lod.py

from pyside6dom import *

people = [
    {"name": "Jane", "score": 96},
    {"name": "Joan", "score": 90},
    {"name": "Melissa", "score": 92},
    {"name": "Tabitha", "score": 90},
    {"name": "Jess", "score": 87},
    {"name": "Katie", "score": 98},
    {"name": "Nicky", "score": 80},
    {"name": "Samantha", "score": 97},
    {"name": "Brie", "score": 90},
]

init_window('OurApp', 700, 600)

set_theme("""
    body { background-color: rgb(25, 25, 25); }
    button {
        padding: 8px 15px;
        font-weight: bold;
        background-color: rgb(45, 45, 55);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 5px;
        margin: 5px;
    }
    button:hover{
        border-color: rgb(255, 255, 255);
    }
""")

top_container = ce('scroll_div')
top_container.style.display = 'flex'
top_container.style.flexDirection = 'row'
top_container.style.alignItems = 'flex-start'
# 85px to leave room for the scrollbar
top_container.style.height = '85px' 
ba(top_container)

for person in people:
    the_btn = ce('button')
    the_btn.textContent = person["name"]
    # p=person locks the current object into the lambda's memory
    the_btn.onclick = lambda p=person: print(f"{p['name']} scored: {p['score']}")
    #the_btn.onclick = lambda p=person: print(p['name'] + " scored: " + str(p['score']))
    ba(the_btn, top_container)

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

