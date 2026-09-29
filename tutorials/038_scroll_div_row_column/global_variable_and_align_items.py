# global_variable_and_align_items.py

from pyside6dom import *

init_window("Our App", 600, 400)

set_theme("""
    body {
        background-color: rgb(30, 30, 30);
    }
    button {
        padding: 2px 6px;
        background-color: rgb(0, 0, 0);
        color: cyan;
        /* we write 1px before solid */
        border: 1px solid rgb(255, 255, 255);
        border-radius: 5px;
    }
    button:hover {
        background-color: #555;
        border-color: rgb(0, 255, 255);
    }
    button:pressed {
        font-weight: bold;
    }
    input {
        border: 1px solid white;
    }
""")

click_tracker = 0

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
ba(welcomeMessage)

panel_container = ce('div')
panel_container.style.display = 'flex'
panel_container.style.flexDirection = 'row'
ba(panel_container)

button_container = ce('scroll_div')
button_container.style.display = 'flex'
button_container.style.flexDirection = 'column'
button_container.style.alignItems = 'flex-start'
button_container.style.border = '1px solid white'
button_container.style.width = '200px'
button_container.style.height = '200px'
ba(button_container, panel_container)

sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click_say():
    global click_tracker
    welcomeMessage.textContent = 'Hi'
    click_tracker += 1
    ge('right_panel').value = str(click_tracker)
sayHiBtn.onclick = handle_click_say
ba(sayHiBtn, button_container)

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click_howdy():
    global click_tracker
    welcomeMessage.textContent = 'Howdy'
    click_tracker += 1
    ge('right_panel').value = str(click_tracker)
sayHowdyBtn.onclick = handle_click_howdy
ba(sayHowdyBtn, button_container)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'Custom'
def handle_click_this(message):
    global click_tracker
    welcomeMessage.textContent = message
    click_tracker += 1
    ge('right_panel').value = str(click_tracker)
sayThisBtn.onclick = lambda: handle_click_this('Hey Now')
ba(sayThisBtn, button_container)

right_panel = ce('textarea')
right_panel.id = 'right_panel'
right_panel.value = 'Hi Everyone'
ba(right_panel, panel_container) 

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

