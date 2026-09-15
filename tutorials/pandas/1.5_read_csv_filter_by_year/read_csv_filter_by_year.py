# read_csv_filter_by_year.py

import pandas as pd
from pyside6dom import *

init_window('Filter by Year', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data as a beautiful HTML table
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Filtered Data (Year == 2026):</b>"
ba(sep_txt)

# Filter the data
# Show only the rows where the 'Year' column equals 2026
recent_data = theData[theData['Year'] == 2026]

# Display the filtered subset as its own HTML table
filtered_txt = ce('text')
filtered_txt.innerHTML = recent_data.to_html(index=False)
ba(filtered_txt)

run_app()

####

'''
             Name  Score  Year
0         Tabitha  98  2026
1            Jane  95  2025
2        Jennifer  90  2025
3  Alison, Martin  89  2024
-------------------------------
      Name  Score  Year
0  Tabitha  98  2026
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

