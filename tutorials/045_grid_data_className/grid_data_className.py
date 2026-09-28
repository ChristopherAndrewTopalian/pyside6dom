# grid_data_className.py

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
    
    /* The Engine now utilizes the .class syntax */
    .player_card {
        background-color: rgb(30, 30, 40);
        border: 1px solid rgb(50, 50, 70);
        border-radius: 6px;
        padding: 15px;
    }
    
    /* We can even add Qt's built-in hover states */
    .player_card:hover {
        border: 1px solid rgb(0, 255, 200);
        background-color: rgb(40, 40, 50);
    }
    
    .player_name {
        color: rgb(0, 255, 200);
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .player_score {
        color: white;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
""")

players = [
    {"name": "Jane", "score": 92},
    {"name": "Melissa", "score": 95},
    {"name": "Tabitha", "score": 93},
    {"name": "Christopher", "score": 90},
    {"name": "Alex", "score": 85},
    {"name": "Sarah", "score": 97}
]

grid = ce('div')
grid.id = 'scoreboard_grid' # Uses the #id CSS rule!
grid.style.display = 'grid'
grid.style.gridTemplateColumns = 'repeat(3, 1fr)' 
ba(grid)

# Look how clean this loop is now!
for p in players:
    card = ce('div')
    card.className = 'player_card'
    card.style.display = 'flex'
    card.style.flexDirection = 'column'
    card.style.alignItems = 'center'
    ba(card, grid)
    
    name_lbl = ce('text')
    name_lbl.className = 'player_name'
    name_lbl.textContent = p["name"]
    ba(name_lbl, card)
    
    score_lbl = ce('text')
    score_lbl.className = 'player_score'
    score_lbl.textContent = str(p["score"])
    #score_lbl.style.textAlign = 'center'
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
# College of Scripting Music & Science
#
# GitHub: https://github.com/ChristopherAndrewTopalian
#
# GitHub: https://github.com/ChristopherTopalian
# Google Sites: https://sites.google.com/view/CollegeOfScripting

