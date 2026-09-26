# scroll_div_row_column.py

from pyside6dom import *

init_window('True HTML Auto-Scroll', 700, 600)

set_theme("""
    body { background-color: rgb(20, 20, 20); }
    button {
        padding: 10px 20px;
        font-weight: bold;
        background-color: rgb(40, 45, 55);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 5px;
        margin: 5px;
    }
""")

####

top_scroll_ribbon = ce('scroll_div')
top_scroll_ribbon.style.display = 'flex'
top_scroll_ribbon.style.flexDirection = 'row'
# IMPORTANT: we explicitly set the height so it doesn't get greedy
top_scroll_ribbon.style.height = '85px' 
top_scroll_ribbon.style.border = '1px solid rgb(0, 255, 200)'
ba(top_scroll_ribbon)

for i in range(1, 21):
    btn = ce('button')
    btn.textContent = f'Option {i}'
    btn.onclick = lambda x=i: print(f'Clicked Option {x}')
    ba(btn, top_scroll_ribbon)

####

spacer = ce('text')
spacer.innerHTML = "<br><b>Main Content Area:</b><hr>"
spacer.style.color = 'white'
spacer.style.fontSize = '18px'
ba(spacer)

column_container = ce('div')
column_container.style.display = 'flex'
column_container.style.flexDirection = 'column'
column_container.style.alignItems = 'flex-start' 
ba(column_container)

for item in ["Run Diagnostics", "Clear Cache", "Reboot Engine"]:
    action_btn = ce('button')
    action_btn.textContent = item
    ba(action_btn, column_container)

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

