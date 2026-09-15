# read_csv_info.py

# read_csv_info.py

import pandas as pd
import io
from pyside6dom import *

init_window('Read CSV Info', 700, 600)

theData = pd.read_csv('data.csv')

# Display the raw Data
data_txt = ce('text')
data_txt.textContent = theData.to_string()
ba(data_txt)

# Display the Separator
sep_txt = ce('text')
sep_txt.textContent = "\n-------------------------------\n"
ba(sep_txt)

# Catch and Display the .info()
# We create an empty "catcher's mitt"
buffer = io.StringIO()

# We tell Pandas to print the info into the buffer instead of the console
theData.info(buf=buffer)

# We grab the caught text out of the buffer
info_string = buffer.getvalue()

# Now we can display it in the DOM!
info_txt = ce('text')
info_txt.textContent = info_string
ba(info_txt)

run_app()

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
-------------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    4 non-null      object
 1   Score   4 non-null      int64
dtypes: int64(1), object(1)
memory usage: 196.0+ bytes
None
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

