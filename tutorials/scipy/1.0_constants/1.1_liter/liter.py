# liter.py

from pyside6dom import *
from scipy import constants

init_window('Our App', 700, 600)

result = ce('div')
result.textContent = f" liter: {constants.liter}"
result.style.fontSize = '100px'
result.style.fontWeight = 'bold'
result.style.color = 'rgb(0, 255, 255)'
result.style.padding = '20px 20px'
ba(result)

run_app()

####

'''
scipy.constants.liter returns the value of 1 liter in cubic meters (m³), which is exactly 0.001. We can also use the spelling variant scipy.constants.litre
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

