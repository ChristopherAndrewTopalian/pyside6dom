# read_data.py

import sqlite3
from pyside6dom import *

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to SELECT data
sql_select = "SELECT part_name, price FROM Inventory WHERE quantity > 100;"

# Execute and fetch the results
cursor.execute(sql_select)
results = cursor.fetchall()
conn.close() # Safe to close as soon as you have the results in memory

# Start building the HTML string with standard table tags
html_data = "<table border='1' cellpadding='4' cellspacing='0'>"

html_data += "<tr><th>Part Name</th><th>Price</th></tr>"

# Loop through the database results and add a table row for each item
for row in results:
    part_name = row[0]
    # Format the price to ensure it always shows two decimal places
    price = f"${row[1]:.2f}" 
    
    # Print to console for debugging
    print(f"Item: {part_name} | Price: {price}")
    
    # Add to the HTML table
    html_data += f"<tr><td>{part_name}</td><td>{price}</td></tr>"

# Close the HTML table tag
html_data += "</table>"

####

init_window("Military Warehouse Inventory", 700, 500)

output = ce('text')
# Inject the constructed HTML string into the UI
output.innerHTML = html_data
ba(output)

run_app()

####

'''
Item: Kevlar Vest | Price: $450.5
Item: Field Medical Kit | Price: $75.25
'''

'''
Query (Read) the Data  
The SELECT command grabs the exact data requested from the database.
'''

'''
Explaining the Loop and row[0]
Let's look at the SELECT command we ran:
SELECT part_name, price FROM Inventory WHERE quantity > 100;

Because we asked for exactly two columns in that specific order, and filtered for quantities over 100, SQLite hands us a list of locked tuples that looks like this:
[
    ('Kevlar Vest', 450.50),
    ('Field Medical Kit', 75.25)
]

When we write the for loop, we are just extracting one tuple at a time:

for row in results:
    # On the first loop, row = ('Kevlar Vest', 450.50)
    
    # row[0] is the 1st item: 'Kevlar Vest'
    # row[1] is the 2nd item: 450.50
    
    print(f"Item: {row[0]} | Price: ${row[1]}")
'''

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

