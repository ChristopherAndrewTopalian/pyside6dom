# read_csv_convert_to_list_of_dictionaries_show_names.py

import pandas as pd
from pyside6dom import *

init_window('Show Names from Dictionaries', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Looping Through Array of Objects:</b><br>"
ba(sep_txt)

# Convert the DataFrame to a List of Dictionaries (Array of Objects)
data_array = df.to_dict(orient='records')

# Loop through the array and build UI elements dynamically
for person in data_array:
    # Instead of printing to the console, we create a new text element for each person
    person_txt = ce('text')
    
    # We grab the 'Name' and 'Score' exactly like a JavaScript object
    person_txt.textContent = f"{person['Name']}: {person['Score']}"
    
    # Add it to the screen
    ba(person_txt)

run_app()

####

'''
Tabitha: 98
Jane: 95
Jennifer: 90
Alison, Martin: 89
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

