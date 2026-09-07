# pyside6dom_easy_example.py

from pyside6dom import *

init_window("Our App", width = 600, height = 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
ba(welcomeMessage)

sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click
ba(sayHiBtn)

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click
ba(sayHowdyBtn)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'This'
def handle_click(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click('Hey Now')
ba(sayThisBtn)

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

