# earthquake_realtime_data_optimized.py

import pandas as pd
from pyside6dom import *

init_window('Real-Time Earthquakes (Optimized)', 1200, 700)

# Fetch the live data
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
theData = pd.read_csv(url)

# Find out exactly how many rows (earthquakes) are in the data today!
total_quakes = len(theData)

# Add a stylish dashboard title with the live count
title_txt = ce('text')
title_txt.innerHTML = f"<b style='color: #00ffcc; font-size: 18px;'>USGS Real-Time Earthquake Monitor</b><br>Worldwide Earthquakes in the past 24 hours: <b>{total_quakes}</b><br><hr><br>"
ba(title_txt)

# THE SPEED FIX: Grab only the first 50 rows
# This prevents the HTML renderer from overloading your computer's memory
recent_50 = theData.head(50)

# Display the optimized data
data_txt = ce('text')
data_txt.innerHTML = recent_50.to_html(index=False)
ba(data_txt)

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

