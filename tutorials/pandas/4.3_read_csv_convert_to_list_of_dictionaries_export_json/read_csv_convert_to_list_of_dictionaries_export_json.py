# read_csv_convert_to_list_of_dictionaries_export_json.py

import pandas as pd
import json
from pyside6dom import *

init_window('Export CSV to JSON', 700, 750)

# Load the CSV and create the array of objects
df = pd.read_csv('data.csv')
data_array = df.to_dict(orient='records')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Write the array to a JSON file on the local drive
with open('exported_data.json', 'w') as json_file:
    # json.dump() physically writes the file to the drive
    json.dump(data_array, json_file, indent=4)

# Display a clean separator and a success message
status_txt = ce('text')
status_txt.innerHTML = "<br><hr><br><b style='color: #00ffcc;'>Status: Successfully exported 'exported_data.json' to local drive!</b><br><br><b>File Preview:</b>"
ba(status_txt)

# Show a preview of the JSON data we just saved
preview_txt = ce('text')
# We use json.dumps() here to create a formatted string just for the visual preview
preview_txt.textContent = json.dumps(data_array, indent=4)
ba(preview_txt)

run_app()

####

'''
[
    {
        "Name": "Tabitha",
        "Score": 98
    },
    {
        "Name": "Jane",
        "Score": 95
    },
    {
        "Name": "Jennifer",
        "Score": 90
    },
    {
        "Name": "Alison, Martin",
        "Score": 89
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

