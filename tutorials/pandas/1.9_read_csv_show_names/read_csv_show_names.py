# read_csv_show_names.py

import pandas as pd
from pyside6dom import *

init_window('Show Names', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Isolated Column ('Name') as a Series:</b>"
ba(sep_txt)

# Extract the single column
# Using single brackets returns a Pandas 'Series' instead of a 'DataFrame'
names_series = theData["Name"]

# Display the Series
# We use .to_frame() to convert the 1D Series back into a 2D table so 
# our engine can automatically style it with the beautiful CSS!
names_txt = ce('text')
names_txt.innerHTML = names_series.to_frame().to_html(index=False)
ba(names_txt)

run_app()

####

'''
0  Tabitha
1  Jane
2  Jennifer
3  Alison, Martin
Name: Name, dtype: object
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

