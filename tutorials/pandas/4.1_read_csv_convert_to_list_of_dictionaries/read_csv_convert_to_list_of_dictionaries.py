# read_csv_convert_to_list_of_dictionaries.py

import pandas as pd
import json
from pyside6dom import *

init_window('Convert to List of Dictionaries', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Converted to List of Dictionaries (JSON Array of Objects):</b><br>"
ba(sep_txt)

# Convert the DataFrame to a List of Dictionaries
# orient='records' creates the classic Array of Objects format
data_array = df.to_dict(orient='records')

# Format the Python dictionary into a beautiful JSON string
# indent=4 gives it that perfect code-editor spacing
formatted_json = json.dumps(data_array, indent=4)

#  Display the formatted string
# We use textContent here so the GUI preserves all the spaces and line breaks
json_txt = ce('text')
json_txt.textContent = formatted_json
ba(json_txt)

run_app()

####

'''
[
    {
        'Name': 'Tabitha',
        'Score': 98
    },

    {
        'Name': 'Jane',
        'Score': 95
    },
    
    {
        'Name': 'Jennifer',
        'Score': 90
    },
    
    {
        'Name': 'Alison,
        Martin', 'Score': 89
    }
]
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

