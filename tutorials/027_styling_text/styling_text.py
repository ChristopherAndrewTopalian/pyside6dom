# styling_text.py

from pyside6dom import *

init_window('Our App', 700, 600)

ourTitle = ce('text')
ourTitle.textContent = 'Hi Everyone'
ourTitle.style.fontFamily = 'Arial'
ourTitle.style.fontSize = '70px'
ourTitle.style.fontWeight = 'bold'
ourTitle.style.color = 'rgb(255, 255, 255)'
ba(ourTitle)

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

