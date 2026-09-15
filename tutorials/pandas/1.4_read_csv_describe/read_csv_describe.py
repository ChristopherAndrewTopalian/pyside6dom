# read_csv_describe.py

import pandas as pd
from pyside6dom import *

init_window('Read CSV Describe', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data as a beautiful HTML table
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Statistical Summary (.describe):</b>"
ba(sep_txt)

# Display the describe() data as a second HTML table
# Because .describe() returns a DataFrame, it has .to_html() built right in.
# (We leave the index on here because the index contains the labels like 'mean', 'min', 'max')
desc_txt = ce('text')
desc_txt.innerHTML = theData.describe().to_html()
ba(desc_txt)

run_app()

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
-------------------------------
           Score
count   4.000000
mean   93.000000
std     4.242641
min    89.000000
25%    89.750000
50%    92.500000
75%    95.750000
max    98.000000
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

