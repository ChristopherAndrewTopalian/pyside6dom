# read_csv_convert_to_dictionary_of_dictionaries.py

import pandas as pd
import json
from pyside6dom import *

init_window('Convert to Dictionary of Dictionaries', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Converted to Dictionary of Dictionaries (Lookup Table):</b><br>"
ba(sep_txt)

# Convert the DataFrame to a Dict of Dicts
# By setting 'Name' as the index first, the names become the master keys
data_obj = df.set_index('Name').to_dict(orient='index')

# Format the Python dictionary into a beautiful JSON string
formatted_json = json.dumps(data_obj, indent=4)

# Display the formatted string
# textContent perfectly preserves our indent=4 spacing
json_txt = ce('text')
json_txt.textContent = formatted_json
ba(json_txt)

run_app()

####

'''
{'Tabitha': {'Score': 98}, 'Jane': {'Score': 95}, 'Jennifer': {'Score': 90}, 'Alison, Martin': {'Score': 89}}
'''

'''
{
    'Tabitha':
    {
        'Score': 98
    },

    'Jane':
    {
        'Score': 95
    },

    'Jennifer':
    {
        'Score': 90
    },

    'Alison, Martin':
    {
        'Score': 89
    }
}
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

