# pyside6dom_example.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window("Notepad App", 500, 400)

theTitle = ce('h1')
theTitle.textContent = "Notes"
theTitle.style("color: rgb(0, 255, 255); margin-bottom: 10px;")
ba(theTitle)

# The new textarea tag!
note_pad = ce('textarea')
note_pad.placeholder = "Start typing your notes here...\n(Press Enter for a new line)"
note_pad.style("background-color: #1a1a1a; color: rgb(0, 255, 255); font-family: Arial; font-size: 24px;")
ba(note_pad)

char_count = ce('text')
char_count.textContent = "Characters: 0"
char_count.style("color: rgb(130, 130, 130); text-align: right;")
ba(char_count)

# Real-time event mapping
def update_count(text):
    char_count.textContent = f"Characters: {len(text)}"

note_pad.oninput = update_count

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

