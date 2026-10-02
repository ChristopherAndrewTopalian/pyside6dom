# class_inspect.py

import inspect
from pyside6dom import *

init_window('Inspect DOMStyle File', 800, 600)

result_txt = ce('textarea')
result_txt.id = 'result_txt'
result_txt.style.fontSize = '24px' 
result_txt.style.fontFamily = 'Arial'
result_txt.style.width = '700'
result_txt.style.height = '500'
result_txt.style.backgroundColor = '#1e1e1e'
result_txt.style.color = '#569cd6'
#result_txt.raw.setReadOnly(True)
result_txt.readOnly = 'true'
ba(result_txt)

# Get the file path
our_query = inspect.getfile(DOMStyle)

# Read the file and populate the element
if os.path.isfile(our_query):
    with open(our_query, 'r') as file:
        content = file.read()
        result_txt.value = content 
else:
    result_txt.value = "File not found."

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

