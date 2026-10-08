# foundation.py

from sympy import symbols, Eq, solve, Rational

from pyside6dom import *

init_window('SymPY Foundation', 700, 600)

x = symbols('x')

# 1/2x + 3/2(x + 1) - 1/4 = 5
eq = Eq(Rational(1,2)*x + Rational(3,2)*(x + 1) - Rational(1,4), 5)

sol = solve(eq, x)

print(sol)

show_work = ce('textarea')
show_work.value = eq
show_work.style.fontSize = '35px'
show_work.style.fontWeight = 'bold'
ba(show_work)

result_div = ce('textarea')
result_div.value = sol
result_div.style.fontSize = '35px'
result_div.style.fontWeight = 'bold'
ba(result_div)

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

