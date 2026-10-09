# title_attribute.py

from pyside6dom import *

init_window('Title Attribute', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Howdy'
howdy_btn.title = 'Click to see a message in console'
howdy_btn.onclick = lambda: print('Howdy')
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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting

