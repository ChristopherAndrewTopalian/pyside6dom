# class_inspect_DOMStyle.py

import inspect
from pyside6dom import *

init_window('Class Inspector', 800, 600)

# Create the UI
result_txt = ce('textarea')
result_txt.id = 'result_txt'
result_txt.style.fontSize = '24px' 
result_txt.style.fontFamily = 'Consolas, monospace'
result_txt.style.width = '700'
result_txt.style.height = '500'
result_txt.style.backgroundColor = '#1e1e1e'
result_txt.style.color = '#569cd6'
result_txt.raw.setReadOnly(True)
ba(result_txt)

# Extract ONLY the target class
try:
    # This single line grabs the exact source code for the DOMStyle class
    class_code = inspect.getsource(DOMStyle)
    result_txt.value = class_code
except Exception as err:
    result_txt.value = f"Error extracting code: {err}"

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

