# show_commands_textarea.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window('Engine Manual', 700, 600)

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    textarea {
        background-color: rgb(10, 10, 15);
        color: rgb(0, 255, 200);
        font-family: Consolas, monospace;
        font-size: 24px;
        font-weight: bold;
        border: 2px solid rgb(0, 255, 200);
        border-radius: 8px;
        padding: 15px;
    }
""")

the_commands = ce('textarea')
# We execute the function immediately to grab the returned string!
the_commands.value = show_commands()

# Make it fill the screen nicely
the_commands.style.width = '650px'
the_commands.style.height = '550px'

ba(the_commands)

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

