# types_of_clicks.py

from pyside6dom import *

init_window('Types of Clicks', 700, 600)

howdy_btn = ce('button')
howdy_btn.textContent = 'Howdy'
howdy_btn.onclick = lambda: print('Left Click')
howdy_btn.oncontextmenu = lambda: print('Right Click')
howdy_btn.onauxclick = lambda: print('Middle Button Click')
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

