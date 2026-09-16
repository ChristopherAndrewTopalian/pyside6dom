# read_csv_make_chart.py

import pandas as pd
import matplotlib.pyplot as plt
import os
from pyside6dom import *

init_window('Read CSV Chart', 800, 800)

theData = pd.read_csv('data.csv')

# Display the raw Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Sales Bar Chart:</b><br>"
ba(sep_txt)

# Create the bar chart using Pandas/Matplotlib
theData.plot(kind='bar', x='Month', y='Sales')

# Instead of plt.show(), we save it as an image
chart_filename = 'sales_chart.png'
plt.savefig(chart_filename, bbox_inches='tight') # bbox_inches keeps the edges clean
plt.close() # Closes it in matplotlib's invisible background to free up memory

# Load the image into the PySide6 DOM using your engine's img tag
chart_img = ce('img')
chart_img.src = chart_filename
chart_img.width = 600  # our engine's proportional sizing will auto-calculate the height
ba(chart_img)

run_app()

####

'''
Name  Score  Year  Team  Job    Month  Sales
0  Tabitha  98  2026  Red  Engineer  January  4000
1  Jane  95  2025  Blue  Computer Scientist  August  5000
2  Jennifer  90  2025  Red  AI Specialist  June  1000
3  Alison, Martin  89  2024  Blue  Robotics Technician  March  500
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

