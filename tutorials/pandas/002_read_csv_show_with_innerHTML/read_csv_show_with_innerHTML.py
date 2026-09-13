# read_csv_show_with_innerHTML.py

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV File', 700, 400)

output = ce('text')
# Inject the Pandas HTML directly into the text element
output.innerHTML = theData.to_html(index=False, border=1)

ba(output)

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

