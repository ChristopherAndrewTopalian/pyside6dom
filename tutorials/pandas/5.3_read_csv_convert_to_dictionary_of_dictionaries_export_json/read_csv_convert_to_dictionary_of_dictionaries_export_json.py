# read_csv_convert_to_dictionary_of_dictionaries_export_json.py

import pandas as pd
import json
from pyside6dom import *

init_window('Export Dictionary of Dictionaries to JSON', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Convert the DataFrame to a Dictionary of Dictionaries
# Setting 'Name' as the index makes the names the master keys
data_dict = df.set_index('Name').to_dict(orient='index')

# Write the dictionary to a JSON file on the local drive
# We include encoding='utf-8' just in case there are any special characters in the data!
with open('exported_dict_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, indent=4)

# Display a clean separator and a styled success message
status_txt = ce('text')
status_txt.innerHTML = "<br><hr><br><b style='color: #00ffcc;'>Status: Successfully exported 'exported_dict_data.json' to local drive!</b><br><br><b>File Preview:</b>"
ba(status_txt)

# Show a preview of the JSON data we just saved
preview_txt = ce('text')
# We use json.dumps() to create a formatted string for the visual preview
preview_txt.textContent = json.dumps(data_dict, indent=4)
ba(preview_txt)

run_app()

####

'''
{
    "Tabitha": {
        "Score": 98
    },
    "Jane": {
        "Score": 95
    },
    "Jennifer": {
        "Score": 90
    },
    "Alison, Martin": {
        "Score": 89
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

