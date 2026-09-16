# insert_data.py

import sqlite3

from pyside6dom import *

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to INSERT data
sql_insert = """
INSERT INTO Inventory (part_name, quantity, price) 
VALUES 
    ('Night Vision Goggles', 45, 2500.00),
    ('Kevlar Vest', 150, 450.50),
    ('Field Medical Kit', 300, 75.25);
"""

cursor.execute(sql_insert)
conn.commit() # Always commit when making changes!
conn.close()

print("Military Warehouse data inserted successfully!")

####

init_window("Insert Data", 700, 500)

status_message = ce('text')
status_message.textContent = 'Data Inserted'
ba(status_message)

run_app()

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

