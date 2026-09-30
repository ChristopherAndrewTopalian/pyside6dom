# div_append.py

from pyside6dom import *

init_window('Our App', 400, 300)

# Use ba() to attach the main container to the window (just like document.body.append)
main_panel = ce('div')
ba(main_panel)

# attach our_title to the main_panel
our_title = ce('text')
our_title.textContent = "Welcome to the App"
main_panel.append(our_title) 

# attach hi_btn to the main_panel
hi_btn = ce('button')
hi_btn.textContent = "Click Me"
hi_btn.onclick = lambda: print('hi')
main_panel.append(hi_btn)

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

