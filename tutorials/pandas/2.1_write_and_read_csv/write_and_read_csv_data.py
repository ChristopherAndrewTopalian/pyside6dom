# write_and_read_csv_data.py

import pandas as pd
import os
from pyside6dom import *

def create_mission_data():
    # We create a CSV string where some data points contain commas.
    # Notice how the names and locations are wrapped in quotes.
    csv_content = """ID,Name,Last_Known_Location,Status
101,"Smith, John","Sector 4, Alpha",Rescued
102,"Doe, Jane","Sector 7, Beta",Awaiting Rescue
103,"O'Connor, Sarah","Sector 4, Alpha",Rescued
104,"Patel, Ravi","Sector 9, Delta",Awaiting Rescue"""

    # Write it to a file
    with open('rescue_manifest.csv', 'w') as file:
        file.write(csv_content)
        
    return "System: 'rescue_manifest.csv' generated on local drive."

# Start the Engine
init_window('Write and Read CSV', 700, 650)

# Generate the file and show the status message
status_msg = create_mission_data()

status_txt = ce('text')
status_txt.textContent = f"{status_msg}\n\n1. Loading the Rescue Manifest..."
ba(status_txt)

# Read the entire file into a DataFrame
df = pd.read_csv('rescue_manifest.csv')

# Displaying the full DataFrame
header_1 = ce('text')
header_1.innerHTML = "<br><b>2. Displaying the DataFrame:</b>"
ba(header_1)

df_txt = ce('text')
df_txt.innerHTML = df.to_html(index=False)
ba(df_txt)

# Isolating a Specific Column (Just the Names)
header_2 = ce('text')
header_2.innerHTML = "<br><hr><br><b>3. Isolating a Specific Column (Just the Names):</b>"
ba(header_2)

# Convert the Series to a Frame so our engine styles it perfectly
names_txt = ce('text')
names_txt.innerHTML = df['Name'].to_frame().to_html(index=False)
ba(names_txt)

run_app()

####

'''
System: 'rescue_manifest.csv' generated on local drive.

1. Loading the Rescue Manifest...

2. Displaying the DataFrame:
    ID             Name Last_Known_Location           Status
0  101  Smith, John  Sector 4, Alpha  Rescued
1  102  Doe, Jane  Sector 7,  Beta  Awaiting Rescue
2  103  O'Connor, Sarah  Sector 4, Alpha  Rescued
3  104  Patel, Ravi  Sector 9, Delta  Awaiting Rescue

3. Isolating a Specific Column (Just the Names):
0  Smith, John
1  Doe, Jane
2  O'Connor, Sarah
3  Patel, Ravi
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

