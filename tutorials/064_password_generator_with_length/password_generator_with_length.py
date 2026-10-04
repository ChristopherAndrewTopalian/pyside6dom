# password_generator_with_length.py

from pyside6dom import *
import random

init_window('Password Generator', 700, 600)

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('~!@#$%^&*()_')

def generate_password():
    all_chars = letters + numbers + symbols
    
    # Grab the length directly from the input box right now.
    try:
        current_length = int(password_length_input.value)
    except ValueError:
        current_length = 12 # Fallback if the user typed a letter by accident
        
    password_list = random.choices(all_chars, k=current_length)
    return "".join(map(str, password_list))

password_div = ce('input')
password_div.style.fontSize = '30px'
password_div.style.fontWeight = 'bold'
password_div.readOnly = True
ba(password_div)

password_length_input = ce('input')
password_length_input.value = 12 
ba(password_length_input)

# Boot up the first password AFTER the input box is created
password_div.value = generate_password()

random_password_btn = ce('button')
random_password_btn.textContent = 'Random'

def handle_click():
    # When clicked, generate_password() fires and immediately reads the new input value
    password_div.value = generate_password()

random_password_btn.onclick = handle_click
ba(random_password_btn)

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

