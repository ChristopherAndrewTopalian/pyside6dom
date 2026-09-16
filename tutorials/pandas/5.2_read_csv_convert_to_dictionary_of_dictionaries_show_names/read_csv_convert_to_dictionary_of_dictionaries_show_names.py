# read_csv_convert_to_dictionary_of_dictionaries_show_names.py

import pandas as pd
from pyside6dom import *

init_window('Show Names from Dictionary of Dictionaries', 700, 600)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Looping Through Dictionary Keys (Names):</b><br>"
ba(sep_txt)

# Convert the DataFrame to a Dict of Dicts
# 'Name' becomes the master key for each record
data_dict = df.set_index('Name').to_dict(orient='index')

# Loop through the keys!
# This behaves exactly like a 'for...in' loop in vanilla JavaScript.
for name in data_dict:
    # Create a brand new text element for each name
    name_txt = ce('text')

    # We display the name (the dictionary key)
    name_txt.textContent = f"Master Key: {name}"
    
    # Append it to the screen
    ba(name_txt)

run_app()

####

'''
Tabitha
Jane
Jennifer
Alison, Martin
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

