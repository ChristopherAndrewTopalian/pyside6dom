# input_upper.py

from pyside6dom import *

import datetime as dt

def get_year():
    today = dt.date.today()
    year = today.year
    return year

init_window('Our App', 700, 600)

year_txt = ce('text')
year_txt.textContent = get_year()
year_txt.style.fontFamily = 'Arial'
year_txt.style.fontSize = '70px'
year_txt.style.fontWeight = 'bold'
year_txt.style.color = 'rgb(255, 255, 255)'
ba(year_txt)

output_txt = ce('text')
output_txt.id = 'output_txt'
output_txt.textContent = 'Output'
output_txt.style.fontSize = '70px'
output_txt.style.fontWeight = 'bold'
output_txt.style.color = 'rgb(0, 255, 255)'
ba(output_txt)

if (get_year() == 2026):
    output_txt.textContent = "It's still 2026"
else:
    output_txt.textContent = "It's the year "+ get_year()

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

