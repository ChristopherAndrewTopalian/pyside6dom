# delete_data.py

import sqlite3
from pyside6dom import *

init_window('Delete SQLite Data', 700, 450)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Inventory System</b><br><hr><br>"
ba(title_txt)

# Connect to the database and set up the cursor
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to DELETE existing data
sql_delete = """
DELETE FROM Inventory 
WHERE part_name = 'Night Vision Goggles';
"""

# Execute and save the changes
cursor.execute(sql_delete)
conn.commit() # Always commit when modifying or deleting data!

# Display a styled success message!
status_txt = ce('text')
status_txt.innerHTML = "<b style='color: #00ffcc;'>Status: Item successfully deleted!</b><br><br><b>Verification (Searching database for deleted item):</b>"
ba(status_txt)

# Query the database to prove it is gone
cursor.execute("SELECT * FROM Inventory WHERE part_name = 'Night Vision Goggles';")
deleted_record = cursor.fetchone()

# Always close the connection when finished
conn.close()

# Show the exact result returned by SQLite on the screen
verify_txt = ce('text')
# We add a little note explaining what 'None' means for the students
verify_txt.textContent = f"Database Record: {deleted_record} \n(A result of 'None' means the data was completely erased!)"
ba(verify_txt)

run_app()

####

'''
A crate of Night Vision Goggles was crushed during a tank training exercise. 
We use the DELETE command to completely remove that row from our active inventory.
'''

'''
CRITICAL SAFETY RULE:
Always include the WHERE clause when deleting! 
If you just write "DELETE FROM Inventory;" without the WHERE clause, 
the database will instantly delete EVERY single row in the table, wiping out your entire warehouse!
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

