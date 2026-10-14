# adding_fractions.py

from sympy import Rational
from pyside6dom import *

init_window('Adding Fractions', 700, 600)

# We define our fractions
fraction_a = Rational(1, 2)
fraction_b = Rational(1, 3)

# We add the fractions together
total = fraction_a + fraction_b

# We create our div to hold the text
result = ce('div')
# Using str() gives us a clean "1/2 + 1/3 = 5/6" format
result.textContent = "Our Equation:\n" + str(fraction_a) + " + " + str(fraction_b) + " = " + str(total)
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.padding = '2px 10px'
ba(result)

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

