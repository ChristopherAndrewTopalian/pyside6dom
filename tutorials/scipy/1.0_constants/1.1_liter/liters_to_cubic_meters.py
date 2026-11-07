# liters_to_cubic_meters.py

from pyside6dom import *
from scipy import constants

init_window('Our App', 700, 600)

set_theme('''
    .headline
    {
        font-size: 30px;
        font-weight: bold;
        color: rgb(0, 255, 255);
        padding: 20px 20px;
    }
''')

result_container = ce('div')
result_container.style.display = 'flex'
result_container.style.flexDirection = 'column'
ba(result_container)

# Get the conversion factor (1 liter in m^3)
print(constants.liter)  
conversion_factor = ce('textarea')
conversion_factor.value = f" conversion factor: {constants.liter}"
conversion_factor.className = 'headline'
result_container.append(conversion_factor)
# Output: 0.001

# Convert 500 liters to cubic meters
example = 500 * constants.liter

converted_liters = ce('textarea')
converted_liters.value = f" converted liters to cubic meters: 500 * {constants.liter} equals {example}"
converted_liters.className = 'headline'
result_container.append(converted_liters)
# Output: 0.5

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

