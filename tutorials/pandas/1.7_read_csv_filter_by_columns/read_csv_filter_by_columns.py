# read_csv_filter_by_columns.py

import pandas as pd
from pyside6dom import *

init_window('Filter by Columns', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Isolated Columns ('Name' and 'Job'):</b>"
ba(sep_txt)

# Isolate the specific columns
# Notice the double brackets [[ ]] - this passes a list of columns to Pandas
isolated_columns = theData[['Name', 'Job']]

# Display the new subset
isolated_txt = ce('text')
isolated_txt.innerHTML = isolated_columns.to_html(index=False)
ba(isolated_txt)

run_app()

####

'''
Name  Score  Year  Team  Job
0 Tabitha  98  2026   Red Engineer
1 Jane  95  2025  Blue  Computer Scientist
2 Jennifer  90  2025  Red  AI Specialist
3  Alison, Martin  89  2024  Blue  Robotics Technician
-------------------------------
             Name               Job
0         Tabitha  Engineer
1            Jane  Computer Scientist
2        Jennifer  AI Specialist
3  Alison, Martin  Robotics Technician
'''

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

