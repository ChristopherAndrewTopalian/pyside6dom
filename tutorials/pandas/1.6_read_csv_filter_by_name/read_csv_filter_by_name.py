# read_csv_filter_by_name.py

import pandas as pd
from pyside6dom import *

init_window('Filter by Name', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Filtered Data (Name == 'Jane'):</b>"
ba(sep_txt)

# Filter the data for a specific string
# Show only rows where the 'Name' column is 'Jane'
jane_data = theData[theData['Name'] == 'Jane']

# Display the filtered subset
filtered_txt = ce('text')
filtered_txt.innerHTML = jane_data.to_html(index=False)
ba(filtered_txt)

run_app()

####

'''
             Name  Score  Year
0         Tabitha  98  2026
1            Jane  95  2025
2        Jennifer  90  2025
3  Alison, Martin  89  2024
-------------------------------
   Name  Score  Year
1  Jane  95  2025
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

