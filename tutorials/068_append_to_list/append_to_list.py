# append_to_list.py

from pyside6dom import *

init_window('Append to List', 600, 500)

set_theme('''
    body {
        background-color: rgb(30, 30, 30); color: white; font-family: Arial; padding: 24px;
    }
    input, textarea {
        background-color: #222;
        color: #00ffcc;
        border: 1px solid #555;
        padding: 5px; font-size: 22px;
    }
    button {
        background-color: rgb(0, 150, 200); color: white; font-size: 16px; padding: 5px 15px;
        border-radius: 4px;
    }
''')

people = []

# ---
# THE TITLE
# ---
theTitle = ce('a')
theTitle.id = 'theTitle'
theTitle.href = 'https://github.com/ChristopherAndrewTopalian/pyside6dom'
theTitle.target = '_blank'
theTitle.textContent = 'pyside6dom'
theTitle.style.fontSize = '20px'
theTitle.style.fontWeight = 'bold'
theTitle.style.textDecoration = 'none'
theTitle.style.color = 'rgb(170, 170, 170)'
ba(theTitle)

# An empty div to act like an <hr> or <br>
spacer = ce('div')
spacer.style.height = '20px'
ba(spacer)

# ---
# THE INPUT SANDWICH
# ---
name_input = ce('input')
name_input.id = 'name_input'
name_input.placeholder = 'Enter Name'

def _(event):
    if event.key == 'Enter':
        event.preventDefault()
        # We use ge() to find the button because it hasn't been drawn yet!
        # .click() perfectly mimics the JS button.click() function
        ge('enter_btn').click()
        
name_input.addEventListener('keydown', _)
ba(name_input)

spacer2 = ce('div')
spacer2.style.height = '20px'
ba(spacer2)

# ---
# THE BUTTON
# ---
enter_btn = ce('button')
enter_btn.id = 'enter_btn' # Assign the ID so the input above can find it!
enter_btn.textContent = 'Enter'

def _():
    if name_input.value.strip() == '': return # Prevent empty clicks
    
    people.append(name_input.value)
    ge('output_txt').value = json.dumps(people, indent=2)
    name_input.value = ''
    name_input.focus()
    
enter_btn.onclick = _
ba(enter_btn)

spacer3 = ce('div')
spacer3.style.height = '20px'
ba(spacer3)

# ---
# THE OUTPUT
# ---
output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.readOnly = True
output_txt.style.width = '400px'
output_txt.style.height = '200px'
ba(output_txt)

# Auto-focus the input when the app launches
name_input.focus()

run_app()

####

'''
We use _ as our 'anon function' style, but we can choose any name we want, such as:
handle_click or something like that.
We can use the same name over and over, without conflict.
'''

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

