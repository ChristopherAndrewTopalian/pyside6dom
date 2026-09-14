# random_greeting.py

import random

from pyside6dom import *

init_window('Random Greeting', 700, 600)

greetings = ['Howdy', 'Hi Everyone', 'Hi There!', 'Hey You', 'Good to see ya']

greeting_txt = ce('text')
greeting_txt.textContent = random.choice(greetings)
greeting_txt.style('font-family: Arial; font-size: 50px; font-weight: bold;')
ba(greeting_txt)

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

