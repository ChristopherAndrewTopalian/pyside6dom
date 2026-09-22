# db_connect_or_create_and_read.py

import sqlite3
import pandas as pd
from pyside6dom import *

# Connect to the database (creates the file automatically if it doesn't exist)
conn = sqlite3.connect('social_media_links.db')
cursor = conn.cursor()

# SQL command to CREATE the table
sql_command = """
CREATE TABLE IF NOT EXISTS Social_Media_Links (
    id INTEGER PRIMARY KEY,
    date DATE,
    description TEXT,
    link TEXT
);
"""
cursor.execute(sql_command)

# Insert a test record if the table is completely empty
cursor.execute("SELECT COUNT(*) FROM Social_Media_Links")

# if there are no records currently
if cursor.fetchone()[0] == 0:
    insert_sql = "INSERT INTO Social_Media_Links (date, description, link) VALUES (?, ?, ?)"

    # Using the standard YYYY-MM-DD format
    cursor.execute(insert_sql, ('2026-09-22', 'Main GitHub Page', 'https://github.com/ChristopherAndrewTopalian/'))

conn.commit()

# READ THE DATA
# Since we just built a beautiful HTML table engine, using Pandas to read the SQL 
# is the fastest, cleanest way to bridge the database to our GUI
theData = pd.read_sql_query("SELECT * FROM Social_Media_Links", conn)

conn.close()

####

init_window("Create and Read Database", 800, 500)

# Status Title
status_message = ce('h2')
status_message.innerHTML = 'Database Connected & Read Successfully<hr>'
status_message.style.color = '#00ffcc'
ba(status_message)

# Display the database contents instantly using the new table_view!
data_view = ce('table_view')
data_view.innerHTML = theData.to_html(index=False)
ba(data_view)

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

