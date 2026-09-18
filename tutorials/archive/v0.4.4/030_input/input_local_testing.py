# input_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window('Our App', 700, 600)

our_greeting = ce('text')
our_greeting.textContent = 'Hi Everyone'
our_greeting.style.fontFamily = 'Arial'
our_greeting.style.fontSize = '70px'
our_greeting.style.fontWeight = 'bold'
our_greeting.style.color = 'rgb(255, 255, 255)'
ba(our_greeting)

word_input = ce('input')
word_input.placeholder = 'Enter Name'
def handle_input():
    print(word_input.value)
word_input.oninput = handle_input
ba(word_input)

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

