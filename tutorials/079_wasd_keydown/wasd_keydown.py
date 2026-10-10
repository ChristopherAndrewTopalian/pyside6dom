# wasd_keydown.py

from pyside6dom import *

init_window('Our App', 700, 600)

output_txt = ce('div')
output_txt.id = 'output_txt'
output_txt.textContent = 'output'
output_txt.style.fontSize = '50px'
ba(output_txt)

def handle_keys(event):
    key = event.key.lower()

    if key == 'w':
        output_txt.textContent = 'w pressed'
    elif key == 's':
        output_txt.textContent = 's pressed'
    elif key == 'a':
        output_txt.textContent = 'a pressed'
    elif key == 'd':
        output_txt.textContent = 'd pressed'


# Attach the keyboard listener to the whole window
window.addEventListener('keydown', handle_keys)

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

