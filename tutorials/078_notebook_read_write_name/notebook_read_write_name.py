# notebook_read_write_name.py

import os
from pyside6dom import *

init_window('Notebook', 700, 650)

# The Filename Input
file_input = ce('input')
file_input.value = 'our_notes.txt'  # Default filename
file_input.style.fontSize = '20px'
file_input.style.marginBottom = '10px'
file_input.style.marginRight = '10px'
ba(file_input)

# The Load Button
load_btn = ce('button')
load_btn.textContent = 'Load File'
ba(load_btn)

# The Text Area
output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.placeholder = 'Type Here'
output_txt.style.fontSize = '24px'
output_txt.style.backgroundColor = 'rgb(30, 30, 30)'
output_txt.style.color = 'rgb(255, 255, 255)'
output_txt.style.height = '450px'
output_txt.style.marginTop = '10px'
ba(output_txt)

# The Save Button
save_btn = ce('button')
save_btn.textContent = 'Save'
save_btn.style.marginTop = '10px'
ba(save_btn)

# The Status Message Label (Starts empty)
status_lbl = ce('label')
status_lbl.textContent = ''
status_lbl.style.marginLeft = '15px'
status_lbl.style.color = 'rgb(0, 255, 150)' # A nice neon green
status_lbl.style.fontSize = '18px'
ba(status_lbl)

# Application Logic

def load_file():
    filename = file_input.value
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            output_txt.value = file.read()
        status_lbl.textContent = f"Loaded '{filename}' successfully."
    else:
        output_txt.value = ""
        status_lbl.textContent = f"Ready to create new file: '{filename}'"

# Run load_file once on startup to grab the default file
load_file()
load_btn.onclick = load_file

def save_file():
    filename = file_input.value
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_txt.value)
    status_lbl.textContent = f"Saved to '{filename}'!"

save_btn.onclick = save_file

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

