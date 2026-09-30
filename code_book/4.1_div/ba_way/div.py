# div.py

from pyside6dom import *

init_window('Our App', 700, 500)

message_container = ce('div')
message_container.style('border: 1px solid rgb(255, 255, 255); border-radius: 8px;')
ba(message_container)

hi_txt = ce('text')
hi_txt.textContent = 'Hi Everyone'
ba(hi_txt, message_container)

howdy_txt = ce('text')
howdy_txt.textContent = 'Howdy'
ba(howdy_txt, message_container)

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

