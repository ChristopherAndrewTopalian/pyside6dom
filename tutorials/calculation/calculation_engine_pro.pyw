# calculation_engine_pro.pyw

import os
import subprocess
from pathlib import Path
from pyside6dom import *

init_window('Calculation Engine Pro', 1100, 700)

# We define a function to launch the file directly in VS Code
def open_in_vscode(file_path):
    subprocess.Popen(f'code "{file_path}"', shell=True)

# Main vertical container
our_container = ce('div')
our_container.style.display = 'flex'
our_container.style.flexDirection = 'column'
our_container.style.gap = '15px'
our_container.style.padding = '20px'
our_container.style.fontFamily = 'Arial'
ba(our_container)

title_label = ce('h1')
title_label.textContent = 'Calculation Engine Hub'
title_label.style.borderBottom = '2px solid white'
title_label.style.paddingBottom = '10px'
our_container.append(title_label)

# We use pathlib to easily find all .pyw files without confusing nested loops
base_folder = Path.cwd()

# .rglob() searches all subfolders automatically
for pyw_file in base_folder.rglob('*.pyw'):
    # We skip the engine script itself so it doesn't make a button for itself
    if pyw_file.name == 'calculation_engine_pro.pyw':
        continue

    # pyw_file is a Path object, so we convert it to a string for our functions
    file_string = str(pyw_file)
    
    # We clean up the file and folder names for the display 
    # e.g., "area_of_a_rectangle" becomes "Area Of A Rectangle"
    clean_name = pyw_file.stem.replace('_', ' ').title()
    category_name = pyw_file.parent.name.capitalize()

    # Create a horizontal row for this specific app
    app_row = ce('div')
    app_row.style.display = 'flex'
    app_row.style.flexDirection = 'row'
    app_row.style.alignItems = 'center'
    app_row.style.gap = '10px'
    app_row.style.padding = '5px'
    app_row.style.backgroundColor = 'rgba(255, 255, 255, 0.1)'
    app_row.style.borderRadius = '5px'
    
    # The App Title Label
    app_label = ce('div')
    app_label.textContent = f"[{category_name}] {clean_name}"
    app_label.style.width = '550px'
    app_label.style.fontWeight = 'bold'
    app_row.append(app_label)

    # THE BUTTONS
    # We use lambda p=file_string to solve Python's late-binding loop issue!

    # RUN BUTTON
    run_btn = ce('button')
    run_btn.textContent = '▶ Run'
    run_btn.onclick = lambda p=file_string: dom.open_file(p)
    app_row.append(run_btn)

    # CODE BUTTON
    code_btn = ce('button')
    code_btn.textContent = '📝 Code'
    code_btn.onclick = lambda p=file_string: open_in_vscode(p)
    app_row.append(code_btn)

    # FOLDER BUTTON
    folder_btn = ce('button')
    folder_btn.textContent = '📁 Folder'
    folder_btn.onclick = lambda p=file_string: dom.show_in_file_explorer(p)
    app_row.append(folder_btn)

    # Add the completed row to the main container
    our_container.append(app_row)

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

