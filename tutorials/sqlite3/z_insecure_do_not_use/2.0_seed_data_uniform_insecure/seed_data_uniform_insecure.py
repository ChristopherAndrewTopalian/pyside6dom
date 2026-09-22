# seed_data_uniform.py

import sqlite3
from pyside6dom import *

init_window('Seed Uniform Data', 750, 650)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Database Initialization</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# Recreate the table so we start clean
# This is the ultimate "undo" button for students
cursor.execute("DROP TABLE IF EXISTS Inventory")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Inventory (
    id INTEGER PRIMARY KEY,
    part_name TEXT,
    quantity INTEGER,
    delivery_date TEXT
);
""")

# Insert the 10 uniform records
# Using standard ISO 8601 format (YYYY-MM-DD)
sql_insert = """
INSERT INTO Inventory (part_name, quantity, delivery_date) 
VALUES 
    ('Kevlar Vest', 150, '2025-11-15'),
    ('Night Vision Goggles', 45, '2026-02-10'),
    ('Field Medical Kit', 300, '2026-08-24'),
    ('Combat Boots', 220, '2026-01-05'),
    ('Tactical Radio', 60, '2025-12-01'),
    ('MRE Case', 500, '2026-03-22'),
    ('Ammunition Crate', 80, '2026-01-30'),
    ('First Aid Pouch', 175, '2026-02-14'),
    ('Portable Generator', 12, '2025-10-09'),
    ('Camouflage Netting', 95, '2026-04-02');
"""

# Execute and commit the massive insertion block
cursor.execute(sql_insert)
conn.commit()

# Display a styled success message
status_txt = ce('text')
status_txt.innerHTML = "<b style='color: #00ffcc;'>Status: Table reset and seeded with 10 uniform-date items successfully!</b><br><br><b>Verification (Live Database Contents):</b><br>"
ba(status_txt)

# Query the newly built table to prove the data is in there!
cursor.execute("SELECT part_name, quantity, delivery_date FROM Inventory;")
results = cursor.fetchall()

# Always close the connection
conn.close()

# Loop through and display the freshly inserted data
for row in results:
    row_txt = ce('text')
    # We apply the aqua color specifically to the date so students see the uniformity
    row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> {row[1]} &nbsp;|&nbsp; <b>Delivery Date:</b> <span style='color: #00ffcc;'>{row[2]}</span>"
    ba(row_txt)

run_app()

####

'''
By strictly enforcing the ISO 8601 format (YYYY-MM-DD), we are writing text that can be flawlessly sorted alphabetically by the database engine. 2026-01-05 will always structurally sort before 2026-02-10. It is a brilliant computer science concept that ensures our application behaves predictably when we inevitably write an ORDER BY delivery_date command later on
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

