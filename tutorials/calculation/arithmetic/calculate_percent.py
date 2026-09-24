# calculate_percent.py

from pyside6dom import *

def calculate_percent(percent, total):
    return (percent / 100) * total

####

init_window("Percentage Calculator", 400, 350)

set_theme("""
    body { background-color: rgb(20, 20, 20); }
    input { 
        padding: 10px; 
        font-size: 24px; 
        font-weight: bold;
        border: 2px solid rgb(100, 100, 100); 
        border-radius: 5px; 
        margin-bottom: 10px;
    }
    input:focus { border: 2px solid rgb(0, 255, 255); }
""")

# Title
app_title = ce('h1')
app_title.textContent = "Percentage Calculator"
app_title.style.fontSize = '30px'
app_title.style.fontWeight = 'bold'
app_title.style.marginBottom = '20px'
app_title.style.color = 'rgb(0, 255, 255)'
#app_title.style("font-size: 30px; font-weight: bold; margin-bottom: 20px; color: rgb(0, 255, 255);")
ba(app_title)

# Input: Percentage
percent_input = ce('input')
percent_input.id = 'percent_val'
percent_input.placeholder = "Enter percentage (e.g., 20)"
def update_result():
    # Grab the raw text from the DOM
    p_text = ge('percent_val').value
    t_text = ge('total_val').value

    # We use a try/except section in case the user types letters or leaves it blank
    try:
        # Convert text to floats (decimals)
        p_num = float(p_text)
        t_num = float(t_text)

        # Pass the numbers to our custom math function
        answer = calculate_percent(p_num, t_num)

        # Display the formatted result
        ge('result_label').textContent = f"{p_num}% of {t_num} is {answer:.2f}"

    except ValueError:
        # If the input isn't a valid number yet, reset the text gracefully
        ge('result_label').textContent = "Waiting for numbers..."
percent_input.oninput = update_result
ba(percent_input)

# Input: Total Amount
total_input = ce('input')
total_input.id = 'total_val'
total_input.placeholder = "Enter total amount (e.g., 150)"
total_input.oninput = update_result
ba(total_input)

result_scroll_div = ce('scroll_div')
result_scroll_div.style.border = '1px solid white'
result_scroll_div.style.width = '200px'
ba(result_scroll_div)

# Result Display
result_display = ce('text')
result_display.id = 'result_label'
result_display.textContent = "Result will appear here..."
result_display.style.border = 'none'
result_display.style.fontSize = '25px'
result_display.style.fontWeight = 'bold'
result_display.style.color = 'rgb(255, 255, 255)'
#result_display.style("font-size: 25px; font-weight: bold; color: rgb(255, 255, 255); margin-top: 20px;")
ba(result_display, result_scroll_div)

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

