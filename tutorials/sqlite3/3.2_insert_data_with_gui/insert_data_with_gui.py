# insert_data_with_gui.py

import sqlite3
import pandas as pd
from pyside6dom import *

###
# DATABASE FUNCTIONS
###

def refresh_table():
    """Reads the latest data from the database and updates the GUI table."""
    conn = sqlite3.connect('social_media_links.db')
    theData = pd.read_sql_query("SELECT * FROM Social_Media_Links", conn)
    conn.close()
    
    # Update our PySide6DOM table_view instantly
    data_view.innerHTML = theData.to_html(index=False)

def save_new_link():
    """Grabs user input, secures it with parameterized queries, and saves it."""
    # Grab the live text typed by the user into the GUI text boxes
    user_date = date_input.value
    user_desc = desc_input.value
    user_link = link_input.value
    
    # Connect to the database
    conn = sqlite3.connect('social_media_links.db')
    cursor = conn.cursor()
    
    # The SQL command using the '?' Security Shield
    insert_sql = "INSERT INTO Social_Media_Links (date, description, link) VALUES (?, ?, ?)"
    
    # Safely merge the live user data with the SQL command
    cursor.execute(insert_sql, (user_date, user_desc, user_link))
    conn.commit()
    conn.close()
    
    # Clear the text boxes so they are ready for the next entry
    date_input.value = ""
    desc_input.value = ""
    link_input.value = ""
    
    # Refresh the visual table to show the new record!
    refresh_table()

###
# GUI DASHBOARD
###

init_window("Interactive Data Entry", 850, 750)

# Dashboard Title
title_txt = ce('h2')
title_txt.innerHTML = "Add New Social Media Link<hr>"
title_txt.style.color = '#00ffcc'
ba(title_txt)

###
# FORM INPUTS
###

# Date Input
date_label = ce('text')
date_label.innerHTML = "<b>Date (YYYY-MM-DD):</b>"
ba(date_label)
date_input = ce('input')
ba(date_input)

# Description Input
desc_label = ce('text')
desc_label.innerHTML = "<br><b>Video Description:</b>"
ba(desc_label)
desc_input = ce('input')
ba(desc_input)

# Link Input
link_label = ce('text')
link_label.innerHTML = "<br><b>URL Link:</b>"
ba(link_label)
link_input = ce('input')
ba(link_input)

###
# SUBMIT BUTTON
###

add_btn = ce('button')
add_btn.textContent = "Add Link"
# Attach our save function to the button click event
add_btn.onclick = save_new_link 
ba(add_btn)

###
# LIVE DATA TABLE
###

table_title = ce('text')
table_title.innerHTML = "<br><br><b style='color: #00ffcc;'>Live Database Records:</b><hr>"
ba(table_title)

# Create the table view component
data_view = ce('table_view')
ba(data_view)

# Run the refresh function once at startup to populate the table initially
refresh_table()

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

