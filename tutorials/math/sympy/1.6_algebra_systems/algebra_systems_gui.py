# algebra_systems_gui.py

from sympy import symbols, Eq, solve
from pyside6dom import *

init_window('Systems of Equations', 700, 550)

x, y = symbols('x y')

# Define the system
eq1 = Eq(2*x - 3*y, 12)
eq2 = Eq(x + y, 1)

# Solve the system
sol = solve((eq1, eq2), (x, y))

# Display the equations
show_work = ce('textarea')
show_work.value = "Equation 1: 2x - 3y = 12\nEquation 2: x + y = 1\n\nFind (x, y)"
show_work.style.fontSize = '30px'
show_work.style.fontWeight = 'bold'
show_work.style.height = '180px'
ba(show_work)

# Extract the values from the dictionary and format them as a coordinate pair
# sol[x] gets the value 3, sol[y] gets the value -2
result_txt = ce('textarea')
result_txt.value = f"Solution:\n(x, y) = ({sol[x]}, {sol[y]})"
result_txt.style.fontSize = '35px'
result_txt.style.fontWeight = 'bold'
result_txt.style.color = 'rgb(100, 200, 255)'
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

