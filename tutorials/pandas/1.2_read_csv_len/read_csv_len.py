# read_csv_len.py

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

output_text = ce('text')
output_text.innerHTML = theData.to_html(index=False, border=1)
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
4 people
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
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

