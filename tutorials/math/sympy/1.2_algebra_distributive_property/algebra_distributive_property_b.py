# foundation_b.py

from sympy import symbols, Mul
from pyside6dom import *

init_window('Foundation', 700, 500)

r, s = symbols('r s')

# "the sum of r and s"
sum_rs = r + s

# "5 times as much as the sum of r and s"
# Use Mul with evaluate=False to stop SymPy from auto-expanding
expr = Mul(5, sum_rs, evaluate=False)

print(expr)

show_work = ce('textarea')
# Convert the SymPy expression to a string explicitly for the textarea
show_work.value = str(expr) 
show_work.style.fontSize = '35px'
show_work.style.fontWeight = 'bold'
ba(show_work)

# We no longer need the hardcoded second textarea because 
# expr now correctly holds the exact '(r + s)*5' structure

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

