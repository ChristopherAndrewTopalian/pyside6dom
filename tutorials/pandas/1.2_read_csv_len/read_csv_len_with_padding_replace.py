# read_csv_len_with_padding_replace.py

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

# Generate the raw HTML string from Pandas
raw_html = theData.to_html(index=False, border=1)

# Inject standard HTML cellpadding directly into the table tag
padded_html = raw_html.replace('<table', '<table cellpadding="8"')

output_text = ce('text')
output_text.innerHTML = padded_html
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
4 people
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

