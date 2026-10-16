# get_year_month_day.py

import datetime as dt
from pyside6dom import *

def get_year_month_day():
    today = dt.date.today()
    return today

init_window('Date', 800, 500)

date_div = ce('div')
date_div.textContent = get_year_month_day()
date_div.style.fontFamily = 'Arial'
date_div.style.fontSize = '50px'
date_div.style.fontWeight = 'bold'
date_div.style.padding = '5px 10px'
ba(date_div)

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

