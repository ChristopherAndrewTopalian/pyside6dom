# filter_after_date.py

import sqlite3
from pyside6dom import *

init_window('Filter by Date', 700, 500)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Delivery Filter</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The dynamic date we want to filter by
target_date = '2026-01-01'

# SQL command to find everything delivered AFTER the target date
# Notice we are still using the '?' placeholder for security!
sql_filter = "SELECT part_name, quantity, delivery_date FROM Inventory WHERE delivery_date > ?;"

# Execute the search securely
cursor.execute(sql_filter, (target_date,))
results = cursor.fetchall()

# Always close the connection
conn.close()

# Display the filter criteria with some red emphasis
header_txt = ce('text')
header_txt.innerHTML = f"<b>--- SHIPMENTS RECEIVED AFTER <span style='color: #ff3333;'>{target_date}</span> ---</b><br><br>"
ba(header_txt)

# Loop through the results and build the UI dynamically
if len(results) == 0:
    not_found_txt = ce('text')
    not_found_txt.textContent = "No shipments found after this date."
    ba(not_found_txt)
else:
    for row in results:
        row_txt = ce('text')
        # Highlighting the date in cyan so they can visually confirm the filter worked
        row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> {row[1]} &nbsp;|&nbsp; <b>Delivered:</b> <span style='color: #00ffcc;'>{row[2]}</span><br>"
        ba(row_txt)

run_app()

'''
SHIPMENTS RECEIVED AFTER 2026-01-01
Item: Night Vision Goggles | Stock: 45 | Delivered: 2026-02-10
Item: Field Medical Kit | Stock: 300 | Delivered: 2026-08-24
Item: Combat Boots | Stock: 220 | Delivered: 2026-01-05
Item: MRE Case | Stock: 500 | Delivered: 2026-03-22
Item: Ammunition Crate | Stock: 80 | Delivered: 2026-01-30
Item: First Aid Pouch | Stock: 175 | Delivered: 2026-02-14
Item: Camouflage Netting | Stock: 95 | Delivered: 2026-04-02
'''

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

