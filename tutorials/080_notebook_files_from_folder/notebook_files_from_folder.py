# notebook_files_from_folder.py

import os
from pyside6dom import *

TEXT_DIR = 'text'
if not os.path.exists(TEXT_DIR):
    os.makedirs(TEXT_DIR)

init_window('Notebook Opens Files in Text Folder', 900, 650)
current_file = ""

# Layout Containers
main_container = ce('div')
main_container.style.display = 'flex'
main_container.style.flexDirection = 'row'
main_container.style.height = '600px'
ba(main_container)

sidebar = ce('scroll_div') 
sidebar.style.width = '250px'
sidebar.style.height = '500px'
sidebar.style.backgroundColor = 'rgb(40, 40, 40)'
sidebar.style.padding = '10px'
main_container.append(sidebar)

editor_panel = ce('div')
editor_panel.style.padding = '10px'
main_container.append(editor_panel)

# Editor Panel UI
status_lbl = ce('label')
status_lbl.textContent = 'Select a file to edit...'
status_lbl.style.color = 'rgb(0, 255, 150)'
status_lbl.style.fontSize = '18px'
editor_panel.append(status_lbl)

output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.style.width = '600px'
output_txt.style.height = '500px'
output_txt.style.marginTop = '10px'
output_txt.style.fontSize = '20px'
output_txt.style.backgroundColor = 'rgb(30, 30, 30)'
output_txt.style.color = 'rgb(255, 255, 255)'
editor_panel.append(output_txt)

save_btn = ce('button')
save_btn.textContent = 'Save Current File'
save_btn.style.marginTop = '10px'
save_btn.style.fontSize = '18px'
editor_panel.append(save_btn)

# Application Logic
def load_file(filename):
    global current_file
    current_file = filename
    filepath = os.path.join(TEXT_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        output_txt.value = file.read()

    status_lbl.textContent = f"Editing: {filename}"

def save_file():
    if current_file == "":
        status_lbl.textContent = "No file selected!"
        return

    filepath = os.path.join(TEXT_DIR, current_file)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(output_txt.value)

    status_lbl.textContent = f"Saved: {current_file}!"

save_btn.onclick = save_file

# Dynamic Sidebar Generation
def build_sidebar():
    sidebar.innerHTML = "" 

    title = ce('h3')
    title.textContent = 'My Files'
    title.style.color = 'white'
    sidebar.append(title)

    all_files = os.listdir(TEXT_DIR)
    text_files = [f for f in all_files if f.endswith('.txt')]
    
    for filename in text_files:
        btn = ce('button')
        btn.textContent = filename
        btn.style.marginBottom = '5px'
        btn.onclick = lambda f=filename: load_file(f)
        sidebar.append(btn)

build_sidebar()

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

