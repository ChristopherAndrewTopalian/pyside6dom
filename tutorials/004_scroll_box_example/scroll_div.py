# scroll_div.py

from pyside6dom import *

init_window("Scroll Div", 600, 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
welcomeMessage.style.fontSize = '30px'
welcomeMessage.style.fontWeight = 'bold'
ba(welcomeMessage)

# Create a specific scrollable container for the buttons
messageBtns_scroll_box = ce('scroll_div')
messageBtns_scroll_box.style.border = '2px solid rgb(255, 255, 255)'
messageBtns_scroll_box.style.backgroundColor = 'rgb(0, 0, 0)'
messageBtns_scroll_box.style.height = '100px'
ba(messageBtns_scroll_box)

# Create buttons and append them TO the scroll box
sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click_hi():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click_hi
messageBtns_scroll_box.append(sayHiBtn)

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click_howdy():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click_howdy
messageBtns_scroll_box.append(sayHowdyBtn)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'This'
def handle_click_message(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click_message('Hey Now')
messageBtns_scroll_box.append(sayThisBtn)

sayYoBtn = ce('button')
sayYoBtn.textContent = 'Yo'
def handle_click_yo():
    welcomeMessage.textContent = 'Yo'
sayYoBtn.onclick = handle_click_yo
messageBtns_scroll_box.append(sayYoBtn)

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

