# grid_gallery.py

from pyside6dom import *

init_window('Grid Gallery Test', 600, 600)

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    button {
        background-color: rgb(40, 40, 50);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 8px;
        font-size: 24px;
        font-weight: bold;
    }
""")

# Create the Grid Container
gallery = ce('div')
gallery.style.display = 'grid'
gallery.style.gridTemplateColumns = 'repeat(4, 1fr)'  # Tell it to wrap every 4 items!
ba(gallery)

# Dump 16 buttons into it, and watch the Auto-Flow perfectly arrange them
for i in range(16):
    btn = ce('button')
    btn.textContent = f"{i + 1}"
    btn.style.height = '100px'
    ba(btn, gallery)

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

