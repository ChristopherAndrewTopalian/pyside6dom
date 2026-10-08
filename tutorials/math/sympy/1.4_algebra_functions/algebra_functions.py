# algebra_functions.py

from sympy import symbols
from pyside6dom import *

init_window('Algebra Functions', 700, 500)

x = symbols('x')

# Define the math function
f_x = -3*x + 5

# Substitute -2 for x
result = f_x.subs(x, -2)

# Display the original function notation
show_func = ce('textarea')
show_func.value = "f(x) = -3x + 5\nFind f(-2)"
show_func.style.fontSize = '35px'
show_func.style.fontWeight = 'bold'
ba(show_func)

# Display the substitution step and final answer
result_txt = ce('textarea')
result_txt.value = f"f(-2) = -3(-2) + 5\nf(-2) = {result}"
result_txt.style.fontSize = '35px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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

