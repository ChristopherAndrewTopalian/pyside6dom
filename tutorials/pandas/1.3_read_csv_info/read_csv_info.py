# read_csv_info.py

import pandas as pd
import io
from pyside6dom import *

init_window('Read CSV Info', 700, 600)

theData = pd.read_csv('data.csv')

# Display the Data as a beautiful HTML table
# Because of our engine upgrade, to_html() automatically gets padded and styled
table_txt = ce('text')
table_txt.innerHTML = theData.to_html(index=False)
ba(table_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>DataFrame Info:</b>"
ba(sep_txt)

# Catch the .info() output
buffer = io.StringIO()
theData.info(buf=buffer)
info_string = buffer.getvalue()

# Display the .info() using textContent
# We use textContent here so the terminal spacing and alignment stays perfect
info_txt = ce('text')
info_txt.textContent = info_string
ba(info_txt)

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

