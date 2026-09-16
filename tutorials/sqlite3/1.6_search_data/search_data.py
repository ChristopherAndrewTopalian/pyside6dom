# search_data.py

import sqlite3
from pyside6dom import *

init_window('Search SQLite Data', 700, 500)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Database Search</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The dynamic variable we want to search for
search_term = 'Field Medical Kit'

# The SQL command using a '?' placeholder for safety
sql_search = "SELECT part_name, quantity, price FROM Inventory WHERE part_name = ?;"

# Execute the search, passing our variable inside a tuple
cursor.execute(sql_search, (search_term,))
results = cursor.fetchall()

# Display what we are searching for
header_txt = ce('text')
header_txt.innerHTML = f"<b>--- SEARCH RESULTS FOR: <span style='color: #00ffcc;'>{search_term.upper()}</span> ---</b><br>"
ba(header_txt)

# Loop through the results and build the UI dynamically
if len(results) == 0:
    # If the list is empty, show the not found message
    not_found_txt = ce('text')
    not_found_txt.textContent = "Status: Item not found in the warehouse."
    ba(not_found_txt)
else:
    # If we have results, loop through and create an element for each row
    for row in results:
        row_txt = ce('text')
        # Using innerHTML so we can selectively bold the labels
        row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> {row[1]} &nbsp;|&nbsp; <b>Price:</b> ${row[2]}<br>"
        ba(row_txt)

conn.close()

run_app()

####

'''
The Base Commander wants to look up the exact stock of a specific item without hard-coding it.
We use a Python variable and a '?' placeholder to safely pass the search term to the database.
'''

'''
CRITICAL SAFETY RULE (Preventing SQL Injection):
Never use standard Python f-strings (e.g., f"SELECT * FROM Inventory WHERE part_name = '{search_term}'") 
to pass variables into SQL. This opens the door to a cyberattack called SQL Injection. 
Always use the '?' placeholder! SQLite will safely sanitize the variable for you.
'''

'''
When web development students take input from a search bar, they might be tempted to concatenate the string directly into the SQL command (e.g., "... WHERE part_name = " + search_term). But, that is VERY DANGEROUS!

FOR SAFETY, we instead use the ? placeholder and passing the variable in a tuple, SQLite automatically sanitizes the data, protecting the database from malicious code.
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

