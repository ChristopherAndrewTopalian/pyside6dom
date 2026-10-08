# algebra_linear_modeling.py

from sympy import symbols, Eq
from pyside6dom import *

init_window('Algebra Linear Modeling', 800, 600)

# Math Logic
v, t = symbols('v t')
initial_amount = 42
leak_rate = 0.5

# Volume equals initial amount minus (rate * time)
eq = Eq(v, initial_amount - leak_rate * t)

# UI Construction
# Display the word problem
problem_txt = ce('textarea')
problem_txt.value = (
    "A water cooler has 42 gallons of water.\n"
    "It leaks at a rate of 0.5 gallons per hour.\n\n"
    "Write an equation for the volume (v) remaining\n"
    "after (t) hours."
)
problem_txt.style.fontSize = '24px'
problem_txt.style.fontWeight = 'bold'
problem_txt.style.height = '200px'
ba(problem_txt)

# Display the translated equation
result_txt = ce('textarea')
# We replace the Python 'Eq(v, ...)' formatting with a standard equals sign for reading
result_txt.value = f"Equation:\nv = {eq.rhs}"
result_txt.style.fontSize = '35px'
result_txt.style.fontWeight = 'bold'
result_txt.style.color = 'rgb(100, 200, 100)'
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

