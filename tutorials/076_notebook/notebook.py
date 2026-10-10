# notebook.py

from pyside6dom import *

init_window('Notebook', 700, 600)

output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.placeholder = 'Type Here'
output_txt.style.fontSize = '24px'
ba(output_txt)

save_btn = ce('button')
save_btn.textContent = 'Save'
def q():
    with open("our_notes.txt", "a", encoding="utf-8") as file:
        file.write(output_txt.value + '\n')
save_btn.onclick = q
ba(save_btn)

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

