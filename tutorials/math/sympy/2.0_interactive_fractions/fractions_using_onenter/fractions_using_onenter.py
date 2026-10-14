# fractions_using_onenter.py

from sympy import Rational
from pyside6dom import *

init_window('PySide6 DOM Custom Events', 800, 600)

set_theme('''
    body {
        font-family: Arial;
        font-size: 30px;
    }
    button {
        background-color: rgb(0, 0, 0);
        color: rgb(255, 255, 255);
        font-family: Arial;
        font-size: 30px;
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
        
        # We clear inputs and focus back on the first box for the next calculation
        input_num1.value = ""
        input_den1.value = ""
        input_num2.value = ""
        input_den2.value = ""
        input_num1.focus()
    except ValueError:
        result.textContent = "Please enter valid whole numbers."

# MAIN ROW CONTAINER
equation_row = ce('div')
equation_row.style.display = 'flex'
equation_row.style.flexDirection = 'row'
equation_row.style.alignItems = 'center'
equation_row.style.gap = '20px'
equation_row.style.margin = '20px'
ba(equation_row)

# FIRST FRACTION
frac1_col = ce('div')
frac1_col.style.display = 'flex'
frac1_col.style.flexDirection = 'column'
frac1_col.style.gap = '10px'
equation_row.append(frac1_col)

input_num1 = ce('input')
input_num1.placeholder = "Num 1"
input_num1.onenter = calculate_addition
frac1_col.append(input_num1)

# Horizontal fraction line
line1 = ce('div')
line1.style.borderBottom = '2px solid white'
frac1_col.append(line1)

input_den1 = ce('input')
input_den1.placeholder = "Den 1"
input_den1.onenter = calculate_addition
frac1_col.append(input_den1)

# OPERATOR
plus_sign = ce('div')
plus_sign.textContent = "+"
equation_row.append(plus_sign)

# SECOND FRACTION
frac2_col = ce('div')
frac2_col.style.display = 'flex'
frac2_col.style.flexDirection = 'column'
frac2_col.style.gap = '10px'
equation_row.append(frac2_col)

input_num2 = ce('input')
input_num2.placeholder = "Num 2"
input_num2.onenter = calculate_addition
frac2_col.append(input_num2)

# Horizontal fraction line
line2 = ce('div')
line2.style.borderBottom = '2px solid white'
frac2_col.append(line2)

input_den2 = ce('input')
input_den2.placeholder = "Den 2"
input_den2.onenter = calculate_addition
frac2_col.append(input_den2)

# BUTTON & RESULT
calc_button = ce('button')
calc_button.id = 'calc_button'
calc_button.textContent = "Calculate"
calc_button.onclick = calculate_addition
ba(calc_button)

result = ce('div')
result.textContent = "Awaiting cadet input..."
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.paddingLeft = '20px'
ba(result)

# Auto-focus the input when the app launches
input_num1.focus()

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

