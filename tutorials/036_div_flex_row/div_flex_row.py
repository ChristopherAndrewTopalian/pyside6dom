# div_flex_row.py

from pyside6dom import *

init_window("div flex row", 420, 400)

# Create a container
button_container = ce('div')
# Tell it to stack elements horizontally
button_container.style.display = 'flex'
button_container.style.flexDirection = 'row'
ba(button_container)

# Add buttons side-by-side
btn1 = ce('button')
btn1.textContent = "Left Button"
btn1.onclick = lambda: print('btn1')
ba(btn1, button_container)

btn2 = ce('button')
btn2.textContent = "Right Button"
btn2.onclick = lambda: print('btn2')
ba(btn2, button_container)

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

