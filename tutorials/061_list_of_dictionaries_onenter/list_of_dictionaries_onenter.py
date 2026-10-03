# list_of_dictionaries_onenter.py

from pyside6dom import *

init_window('List of Dictionaries (lod)', 700, 600)

set_theme('''
    input {
        padding: 6px;
        font-family: Arial;
        font-size: 20px;
        margin-right: 10px;
    }
    button {
        padding: 6px 15px;
        font-size: 20px;
        background-color: rgb(0, 150, 200);
        color: white;
        border-radius: 4px;
    }
''')

# we make an empty list
people = []

# Input: Name
name_input = ce('input')
name_input.placeholder = 'Enter Name'
ba(name_input)

# Input: Role
role_input = ce('input')
role_input.placeholder = 'Enter Role (e.g. Admin)'
ba(role_input)

enter_btn = ce('button')
enter_btn.textContent = 'Add Person'

def add_to_list():
    # Only add if they actually typed something!
    if name_input.value == '' or role_input.value == '':
        # If they hit enter while empty, remove focus (blur) so they know it failed
        name_input.blur() 
        role_input.blur()
        return

    # Create the "Object" (Dictionary)
    new_person = {
        "name": name_input.value,
        "role": role_input.value
    }
    
    # Push it to the list
    people.append(new_person)
    
    # Format it beautifully as a string with indents
    pretty_json = json.dumps(people, indent=4)
    ge('output_txt').value = pretty_json
    
    # Clear inputs and return focus
    name_input.value = ''
    role_input.value = ''
    name_input.focus()

# The Button submits
enter_btn.onclick = add_to_list

# Hitting Enter on the Name box jumps the cursor to the Role box
name_input.onenter = role_input.focus 

# Hitting Enter on the Role box submits the data
role_input.onenter = add_to_list
ba(enter_btn)

# Output Box
output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.style.marginTop = '15px'
output_txt.style.fontSize = '20px'
output_txt.style.height = '400px'
output_txt.readOnly = 'true'
ba(output_txt)

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

