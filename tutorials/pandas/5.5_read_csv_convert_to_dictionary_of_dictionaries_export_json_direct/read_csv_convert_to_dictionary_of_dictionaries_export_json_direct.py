# read_csv_convert_to_dictionary_of_dictionaries_export_json_direct.py

import pandas as pd
from pyside6dom import *

init_window('Direct Export to JSON', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Set the index to 'Name' and export directly to a formatted JSON file
export_filename = 'exported_dictionary_data.json'
df.set_index('Name').to_json(export_filename, orient='index', indent=4)

# Display a clean separator and a styled success message
status_txt = ce('text')
status_txt.innerHTML = f"<br><hr><br><b style='color: #00ffcc;'>Status: Successfully exported '{export_filename}' in a single line!</b><br><br><b>File Verification (Reading from drive):</b>"
ba(status_txt)

# Read the newly created file back from the hard drive to prove it exists
with open(export_filename, 'r', encoding='utf-8') as f:
    saved_json_content = f.read()

# Show the exact contents of the file on the screen
preview_txt = ce('text')
preview_txt.textContent = saved_json_content
ba(preview_txt)

run_app()

####

'''
{
    "Tabitha":{
        "Score":98
    },
    "Jane":{
        "Score":95
    },
    "Jennifer":{
        "Score":90
    },
    "Alison, Martin":{
        "Score":89
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

