# sort_data.py

import sqlite3
from pyside6dom import *

init_window('Sort SQLite Data', 700, 500)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Reorder System</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to SELECT data and sort it
# ORDER BY quantity ASC tells the database engine to put the lowest numbers at the top!
sql_sort = "SELECT part_name, quantity, price FROM Inventory ORDER BY quantity ASC;"

# Execute and fetch the results
cursor.execute(sql_sort)
results = cursor.fetchall()

# We have the data, so we can safely close the connection
conn.close()

# Display the header for the sorted data
# Using a red hex code to emphasize the critical nature of the list
header_txt = ce('text')
header_txt.innerHTML = "<b><span style='color: #ff3333;'>CRITICAL REORDER LIST (LOWEST STOCK FIRST):</span></b><br><br>"
ba(header_txt)

# Loop through the sorted results and build the UI
for row in results:
    row_txt = ce('text')
    
    # Using inline HTML to style the stock numbers so they immediately catch the eye
    row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> <span style='color: #00ffcc;'>{row[1]}</span> &nbsp;|&nbsp; <b>Unit Cost:</b> ${row[2]}<br>"
    ba(row_txt)

run_app()

####

'''
The Quartermaster needs to know which items are closest to running out.
We use the ORDER BY command to automatically sort the results before Python even receives them.
'''

'''
ASC vs DESC:
ASC (Ascending) sorts from smallest to largest (A-Z, 1-100). This is the default if you leave it blank.
DESC (Descending) sorts from largest to smallest (Z-A, 100-1). Perfect for finding the most expensive items!
'''

'''
In web development, students might be tempted to use SELECT * FROM Inventory, pull every single item into JavaScript, and then use the array.sort() method to organize them. BUT, by instead doing the sorting inside the SQL query (ORDER BY quantity ASC) is infinitely faster. By making the database do the heavy lifting before the data even reaches Python, they save memory and ensure their pyside6dom interface loads instantly.
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

