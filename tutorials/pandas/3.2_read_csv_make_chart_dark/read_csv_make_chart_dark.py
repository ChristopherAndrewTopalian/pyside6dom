# read_csv_make_chart_dark.py

import pandas as pd
import matplotlib.pyplot as plt
import os
from pyside6dom import *

init_window('Read CSV Chart Dark', 800, 800)

# Turn on the worldwide dark theme for all matplotlib charts
plt.style.use('dark_background')

# Load our data
theData = pd.read_csv('data.csv')

# Display the raw Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Dark Theme Sales Bar Chart:</b><br>"
ba(sep_txt)

# Create the bar chart and force the bars to be neon cyan
theData.plot(kind='bar', x='Month', y='Sales', color='#00FFFF')

# Save the dark chart as an image
chart_filename = 'sales_chart_dark.png'
plt.savefig(chart_filename, bbox_inches='tight') 
plt.close() # Close it in the background to free up memory

# Load the image into the DOM
chart_img = ce('img')
chart_img.src = chart_filename
chart_img.width = 600  
ba(chart_img)

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

