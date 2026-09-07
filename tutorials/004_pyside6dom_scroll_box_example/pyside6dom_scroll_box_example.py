# pyside6dom_scroll_box_example.py

from pyside6dom import *

init_window("Our App", width = 600, height = 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
welcomeMessage.style("font-size: 30px; font-weight: bold;")
ba(welcomeMessage)

# Create a specific scrollable container for the buttons
messageBtns_scroll_box = ce('scroll_div')
messageBtns_scroll_box.style("border: 2px solid #555; background-color: #1a1a1a; min-height: 200px;")
ba(messageBtns_scroll_box)

# Create buttons and append them TO the scroll box
sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click_hi():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click_hi
ba(sayHiBtn, messageBtns_scroll_box) # Notice the second argument

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click_howdy():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click_howdy
ba(sayHowdyBtn, messageBtns_scroll_box)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'This'
def handle_click_message(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click_message('Hey Now')
ba(sayThisBtn, messageBtns_scroll_box)

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

