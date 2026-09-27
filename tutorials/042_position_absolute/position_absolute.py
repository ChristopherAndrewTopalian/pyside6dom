# position_absolute.py

from pyside6dom import *

init_window('Position Elements', 700, 600)

our_element = ce('div')
our_element.textContent = 'test'
our_element.style.position = 'absolute'
our_element.style.left = '350px'
our_element.style.top = '50px'
our_element.style.border = '2px solid white'
our_element.style.width = '100px'
our_element.style.height = '100px'
ba(our_element)

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

