# proportions_and_ratios.py

from sympy import symbols, Eq, solve, Rational
from pyside6dom import *

init_window('Algebra Proportions', 700, 500)

x = symbols('x')

# 20 grams per 10 ounces = x grams per 8 ounces
eq = Eq(Rational(20, 10), x / 8)

# Solve the equation
sol = solve(eq, x)

# Display the raw equation to the student
show_work = ce('textarea')
show_work.value = "20 / 10 = x / 8"
show_work.style.fontSize = '35px'
show_work.style.fontWeight = 'bold'
ba(show_work)

# Display the calculated result
result_txt = ce('textarea')
result_txt.value = f"x = {sol[0]}"
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

