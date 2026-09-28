# button_date_time_show.py

from pyside6dom import *
import datetime as dt

def get_date_time_12():
    currentDateTime = dt.datetime.now()
    date = currentDateTime.strftime("%m-%d-%y")
    time = currentDateTime.strftime("%I:%M %p")
    return date + " " + time

init_window('Our App', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Date/Time'
def update_time_label():
    ge('output_txt').textContent = get_date_time_12()
howdy_btn.onclick = update_time_label 
ba(howdy_btn)

output_txt = ce('text')
output_txt.id = 'output_txt'
output_txt.style.fontSize = '30px'
output_txt.style.fontWeight = 'bold'
ba(output_txt)

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
# College of Scripting Music & Science
#
# GitHub: https://github.com/ChristopherAndrewTopalian
#
# GitHub: https://github.com/ChristopherTopalian
# Google Sites: https://sites.google.com/view/CollegeOfScripting

