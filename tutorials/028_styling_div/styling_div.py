# styling_div.py

from pyside6dom import *

init_window('Our App', 700, 600)

title_container = ce('div')
title_container.style.fontFamily = 'Arial'
title_container.style.fontSize = '70px'
title_container.style.fontWeight = 'bold'
title_container.style.color = 'rgb(255, 255, 255)'
ba(title_container)

our_title = ce('text')
our_title.textContent = 'Hi Everyone'
ba(our_title, title_container)

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

