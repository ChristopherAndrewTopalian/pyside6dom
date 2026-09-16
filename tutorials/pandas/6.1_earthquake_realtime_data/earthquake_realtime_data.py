# earthquake_realtime_data.py

import pandas as pd
from pyside6dom import *

init_window('Real-Time Earthquake Data', 900, 700)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>USGS Real-Time Earthquake Monitor (Past 24 Hours)</b><br><hr><br>"
ba(title_txt)

# Fetch the live data directly from the USGS servers
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
theData = pd.read_csv(url)

# Display the live data as a beautiful HTML table
# Even though it is live data from the web, our engine instantly applies 
# the aqua headers and padding the second it renders
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

run_app()

####

'''
This app will take longer to load on older computers and will scroll slower.
This is because the Earthquake data is thousands and thousands of lines!

On the next tutorial we show the optimized version, where we only load some at a time!
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

