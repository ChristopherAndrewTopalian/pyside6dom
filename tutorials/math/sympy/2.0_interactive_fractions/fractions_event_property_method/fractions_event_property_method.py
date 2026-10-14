# fractions_event_property_method.py

from sympy import Rational
from pyside6dom import *

init_window('Adding Fractions', 800, 600)

set_theme('''
    button {
        background-color: rgb(0, 0, 0);
        color: rgb(255, 255, 255);
        font-family: Arial;
        font-size: 20px;
        border: 1px solid rgb(255, 255, 255);
    }
    button:hover {
        border-color: rgb(0, 255, 255);
    }
    button:active {
        color: rgb(255, 0, 255);
    }

    input {
        padding: 2px 8px;
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
    }
''')

# We create our calculation logic first so our inputs can reference it
def calculate_addition():
    try:
        num1 = int(input_num1.value)
        den1 = int(input_den1.value)
        num2 = int(input_num2.value)
        den2 = int(input_den2.value)

        fraction_a = Rational(num1, den1)
        fraction_b = Rational(num2, den2)
        total = fraction_a + fraction_b

        result.textContent = f"Our Equation:\n{fraction_a} + {fraction_b} = {total}"
    except ValueError:
        result.textContent = "Please enter valid whole numbers."

# We create our Enter key listener
def check_enter(event):
    if event.key.lower() == 'Enter':
        calculate_addition()

# MAIN ROW CONTAINER
equation_row = ce('div')
equation_row.style.display = 'flex'
equation_row.style.flexDirection = 'row'
equation_row.style.alignItems = 'center'
equation_row.style.gap = '20px'
equation_row.style.margin = '20px'
ba(equation_row)

# FIRST FRACTION (COLUMN)
frac1_col = ce('div')
frac1_col.style.display = 'flex'
frac1_col.style.flexDirection = 'column'
frac1_col.style.gap = '10px'
equation_row.append(frac1_col)

input_num1 = ce('input')
input_num1.placeholder = "Num 1"
input_num1.style.fontSize = '24px'
input_num1.style.textAlign = 'center'
input_num1.onkeyup = check_enter
frac1_col.append(input_num1)

input_den1 = ce('input')
input_den1.placeholder = "Den 1"
input_den1.style.fontSize = '24px'
input_den1.style.textAlign = 'center'
input_den1.onkeyup = check_enter
frac1_col.append(input_den1)

# OPERATOR SIGN
plus_sign = ce('div')
plus_sign.textContent = "+"
plus_sign.style.fontSize = '40px'
plus_sign.style.fontWeight = 'bold'
equation_row.append(plus_sign)

# SECOND FRACTION (COLUMN)
frac2_col = ce('div')
frac2_col.style.display = 'flex'
frac2_col.style.flexDirection = 'column'
frac2_col.style.gap = '10px'
equation_row.append(frac2_col)

input_num2 = ce('input')
input_num2.placeholder = "Num 2"
input_num2.style.fontSize = '24px'
input_num2.style.textAlign = 'center'
input_num2.onkeyup = check_enter
frac2_col.append(input_num2)

input_den2 = ce('input')
input_den2.placeholder = "Den 2"
input_den2.style.fontSize = '24px'
input_den2.style.textAlign = 'center'
input_den2.onkeyup = check_enter
frac2_col.append(input_den2)

# CALCULATE BUTTON
calc_button = ce('button')
calc_button.textContent = "Calculate"
calc_button.onclick = calculate_addition
calc_button.style.fontSize = '24px'
calc_button.style.margin = '20px'
ba(calc_button)

# RESULT DISPLAY
result = ce('div')
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.paddingLeft = '20px'
result.textContent = "Awaiting cadet input..."
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
# GitHub: https://github.com/ChristopherAndrewTopalian/pyside6dom
#
# PyPI: https://pypi.org/project/pyside6dom/
#
# GitHub: https://github.com/ChristopherAndrewTopalian
#
# GitHub: https://github.com/ChristopherTopalian
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting

