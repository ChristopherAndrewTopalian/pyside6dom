# width_height_percentage_bottom_right.py

from pyside6dom import *

init_window('CATopalian Responsive Engine Test', 800, 600)

set_theme('''
    body {
        background-color: #1e1e1e;
        margin: 0px;
        padding: 0px;
    }
    
    .hero_panel {
        background-color: #2d2d30;
        border: 2px solid #00ffcc;
    }
    
    .floating_btn {
        background-color: #ff3333;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border-radius: 25px; /* Rounded pill button */
        border: 2px solid white;
    }
    
    .floating_btn:hover {
        background-color: #ff6666;
    }
''')

# ===
# The 100% Fluid Container
# ===
hero = ce('div')
hero.className = 'hero_panel'
# These will now dynamically recalculate on every window resize
hero.style.width = '100%'
hero.style.height = '100%'
ba(hero)

title = ce('h1')
title.textContent = "Responsive Layouts in PySide6DOM"
title.style.color = "white"
title.style.padding = "40px"
hero.append(title)

# ===
# The Bottom-Right Floating Button
# ===
help_btn = ce('button')
help_btn.className = 'floating_btn'
help_btn.textContent = "💬 Help"

help_btn.style.position = 'absolute'
help_btn.style.width = '120px'
help_btn.style.height = '50px'

# Pin it exactly 20 pixels away from the bottom and right edges
help_btn.style.bottom = '20px'
help_btn.style.right = '20px'
ba(help_btn)

def clicked_help():
    title.textContent = "You clicked the floating button!"
    title.style.color = "#00ffcc"
    
help_btn.onclick = clicked_help

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting

