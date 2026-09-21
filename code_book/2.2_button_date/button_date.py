# button_date_time.py

from pyside6dom import *
import datetime as dt

def get_date_time_12():
    currentDateTime = dt.datetime.now()
    # formatted date MM-DD-YY
    date = currentDateTime.strftime("%m-%d-%y")
    # formatted time HH:MM AM/PM
    time = currentDateTime.strftime("%I:%M %p")
    formattedDateTime = date + " " + time
    return formattedDateTime

####

init_window('Our App', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Date/Time'
howdy_btn.onclick = lambda: print(get_date_time_12())
ba(howdy_btn)

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

