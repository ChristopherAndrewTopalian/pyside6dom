# read_csv_len_with_padding_style_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up THREE levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) 
sys.path.insert(0, project_root)
# --------------------------

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

# Generate the raw HTML string from Pandas (no need to force the border here anymore)
raw_html = theData.to_html(index=False)

# Write pure CSS exactly how a web developer would expect to
table_css = """
<style>
    table {
        border-collapse: collapse;
        margin-top: 10px;
    }
    th, td {
        padding: 8px 15px; 
        border: 1px solid white;
    }
    th {
        background-color: #333333;
        font-weight: bold;
    }
</style>
"""

output_text = ce('text')
# We just glue the CSS and the HTML together, like a real webpage
output_text.innerHTML = table_css + raw_html
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
4 people
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
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

