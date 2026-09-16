# read_csv_convert_to_dictionary_of_dictionaries_filter_by_name.py

import pandas as pd
import json
from pyside6dom import *

init_window('Instant Lookup by Name', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Create the Lookup Table (Dictionary of Dictionaries)
# 'Name' is set as the index, becoming the master key
data_dict = df.set_index('Name').to_dict(orient='index')

# Display the List of Names (The Keys)
sep_1 = ce('text')
sep_1.innerHTML = "<br><hr><br><b>List of Names (Master Keys):</b>"
ba(sep_1)

for name in data_dict.keys():
    name_txt = ce('text')
    # Adding a clean HTML bullet point (&bull;) for visual styling
    name_txt.innerHTML = f"&bull; {name}"
    ba(name_txt)

# Perform the Instant Lookup
sep_2 = ce('text')
sep_2.innerHTML = "<br><hr><br><b style='color: #00ffcc;'>Instant Data Lookup (Tabitha):</b><br>"
ba(sep_2)

# Grab Tabitha's data directly and format it as a beautiful JSON string
tabitha_data = data_dict['Tabitha']
formatted_tabitha = json.dumps(tabitha_data, indent=4)

lookup_txt = ce('text')
# We use textContent here to preserve all the line breaks and spaces
lookup_txt.textContent = f"{formatted_tabitha}"
ba(lookup_txt)

run_app()

####

'''
List of Names (Keys)
Tabitha
Jane
Jennifer
Alison, Martin

Instant Data Lookup
Tabitha's data: {'Score': 98}
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

