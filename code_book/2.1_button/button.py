# button.py

from pyside6dom import *

init_window('Our App', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Hi Everyone'
def greetings(message):
    print(message)
howdy_btn.onclick = lambda: greetings('hi')
ba(howdy_btn)

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

