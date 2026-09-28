# grid_data.py

from pyside6dom import *

init_window('Player Scoreboard', 700, 500)

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    
    #scoreboard_grid {
        background-color: rgb(15, 15, 18);
        border: 2px solid rgb(40, 40, 50);
        border-radius: 8px;
        padding: 15px;
        margin: 20px;
    }
""")

# THE DATA
players = [
    {"name": "Jane", "score": 9540},
    {"name": "Melissa", "score": 8200},
    {"name": "Tabitha", "score": 10550},
    {"name": "Christopher", "score": 10000},
    {"name": "Alex", "score": 7430},
    {"name": "Sarah", "score": 12400}
]

# BUILD THE GRID CONTAINER
grid_container = ce('div')
grid_container.id = 'scoreboard_grid'
grid_container.style.display = 'grid'
# Auto-wrap into 3 columns
grid_container.style.gridTemplateColumns = 'repeat(3, 1fr)' 
ba(grid_container)

####

# POPULATE THE DATA
for p in players:
    # The Outer Card (Flex Column)
    card = ce('div')
    card.style.display = 'flex'
    card.style.flexDirection = 'column'
    card.style.alignItems = 'center'
    card.style.backgroundColor = 'rgb(30, 30, 40)'
    card.style.border = '1px solid rgb(50, 50, 70)'
    card.style.borderRadius = '6px'
    ba(card, grid_container)

    # The Name Label
    name_lbl = ce('text')
    name_lbl.textContent = p["name"]
    name_lbl.style.color = 'rgb(0, 255, 200)'
    name_lbl.style.fontSize = '18px'
    name_lbl.style.fontWeight = 'bold'
    ba(name_lbl, card)

    # The Score Label
    score_lbl = ce('text')
    score_lbl.textContent = str(p["score"])
    score_lbl.style.color = 'white'
    score_lbl.style.fontSize = '24px'
    score_lbl.style.fontWeight = 'bold'
    ba(score_lbl, card)

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

