# overflow_hidden.py

from pyside6dom import *

init_window('CATopalian Overflow Test', 500, 600)

set_theme('''
    body {
        background-color: rgb(0, 50, 50); 
        padding: 20px;
        font-family: 'Segoe UI', Arial; 
        color: white;
    }
    
    .viewport {
        border: 3px solid #00ffcc;
        background-color: rgb(0, 50, 50);
    }
    
    .giant_content {
        background-color: rgb(0, 50, 50);
        font-size: 24px;
        font-weight: bold;
        padding: 20px;
    }
    
    button {
        background-color: rgb(0, 0, 0);
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        border: 2px solid white;
        margin-bottom: 20px;
    }
    button:hover {
        background-color: #555; 
        border-color: #00ffcc;
    }
''')

# ===
# The Toggle Button
# ===
toggle_btn = ce('button')
toggle_btn.textContent = "State: overflow: hidden 👁️"
ba(toggle_btn)

# ===
# The Restricted Container (400x400)
# ===
box = ce('scroll_div')
box.className = 'viewport'
box.style.width = '400px'
box.style.height = '400px'
# Start with scrollbars hidden
box.style.overflow = 'hidden' 
ba(box)

# ===
# The Giant Content (800x800)
# ===
giant = ce('div')
giant.className = 'giant_content'
giant.style.width = '800px'
giant.style.height = '800px'
giant.textContent = "Top Left Corner... (Scroll to see more!)"
box.append(giant)

marker = ce('text')
marker.textContent = "Bottom Right Corner!"
marker.style.position = 'absolute'
marker.style.right = '20px'
marker.style.bottom = '20px'
giant.append(marker)

# ===
# The Real-Time Toggle Logic
# ===
def toggle_overflow():
    if box.style.overflow == 'hidden':
        box.style.overflow = 'auto'
        toggle_btn.textContent = "State: overflow: auto (Scrollbars ON)"
        toggle_btn.style.borderColor = "rgb(0, 150, 150)"
    else:
        box.style.overflow = 'hidden'
        toggle_btn.textContent = "State: overflow: hidden (Scrollbars OFF)"
        toggle_btn.style.borderColor = "white"

toggle_btn.onclick = toggle_overflow

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

