# update_data.py

import sqlite3
from pyside6dom import *

init_window('Update SQLite Data', 700, 450)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Inventory System</b><br><hr><br>"
ba(title_txt)

# Connect to the database and set up the cursor
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to UPDATE existing data
sql_update = """
UPDATE Inventory 
SET quantity = 100 
WHERE part_name = 'Kevlar Vest';
"""

# Execute and save the changes
cursor.execute(sql_update)
conn.commit() # Always commit when modifying data!

# Display a styled success message!
status_txt = ce('text')
status_txt.innerHTML = "<b style='color: #00ffcc;'>Status: Inventory updated successfully!</b><br><br><b>Verification (Reading live from database):</b>"
ba(status_txt)

# Query the database to prove the quantity changed
cursor.execute("SELECT * FROM Inventory WHERE part_name = 'Kevlar Vest';")
updated_record = cursor.fetchone()

# Always close the connection when finished
conn.close()

# Show the exact tuple returned by SQLite on the screen
verify_txt = ce('text')
# textContent prevents the tuple's brackets and quotes from being mistaken for HTML tags
verify_txt.textContent = f"Database Record: {updated_record}"
ba(verify_txt)

run_app()

####

'''
A platoon just signed out 50 Kevlar Vests for deployment. 
We use the UPDATE command to change the existing quantity from 150 down to 100.
'''

'''
CRITICAL SAFETY RULE:
Always include the WHERE clause when updating! 
If you just write "UPDATE Inventory SET quantity = 100;" without the WHERE clause, 
the database will change the quantity of EVERY single item in the entire warehouse to 100!
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

