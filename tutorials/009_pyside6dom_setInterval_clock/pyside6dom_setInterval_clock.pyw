# pyside6dom_setInterval_clock.py

from pyside6dom import *
from datetime import datetime

init_window("Digital Clock", 400, 200)

clock_label = ce('h1')
clock_label.style("font-size: 60px; font-weight: bold; color: rgb(0, 255, 255); qproperty-alignment: AlignCenter; margin-top: 20px;")
ba(clock_label)

date_label = ce('text')
date_label.style("font-size: 24px; color: rgb(255, 255, 255); qproperty-alignment: AlignCenter;")
ba(date_label)

def update_clock():
    now = datetime.now()
    clock_label.textContent = now.strftime("%I:%M:%S %p")
    date_label.textContent = now.strftime("%B %d, %Y")

update_clock()

# Just like JavaScript
setInterval(update_clock, 1000)

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

