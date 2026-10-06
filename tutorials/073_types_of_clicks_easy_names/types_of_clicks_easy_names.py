# types_of_clicks_easy_names.py

from pyside6dom import *

init_window('Types of Clicks with Easy Names', 700, 600)

howdy_btn = ce('button')
howdy_btn.textContent = 'Howdy'
howdy_btn.onleftclick = lambda: print('Left Click')
howdy_btn.onrightclick = lambda: print('Right Click')
howdy_btn.onmiddleclick = lambda: print('Middle Button Click')
ba(howdy_btn)

run_app()

####

'''
we can say onclick or onleftclick
we can say oncontextmenu or onrightclick
we can say onauxclick or onmiddleclick
'''

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

