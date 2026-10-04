# password_generator_with_slider.py

from pyside6dom import *
import random

init_window('Password Generator', 700, 600)

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('~!@#$%^&*()_')
all_chars = letters + numbers + symbols

def generate_password(length):
    password_list = random.choices(all_chars, k=int(length))
    return "".join(map(str, password_list))

# ===
# PASSWORD DISPLAY 
# ===
password_div = ce('input')
password_div.id = "password_display"
password_div.style("font-size: 30px; font-weight: bold;")
password_div.readOnly = True
ba(password_div)

# ===
# NUMBER INPUT BLOCK
# ===
password_length_input = ce('input')
password_length_input.id = "length_input"
password_length_input.value = "12"

def sync_from_input():
    try:
        current_val = int(ge("length_input").value)

        if current_val < 4: current_val = 4
        if current_val > 64: current_val = 64

        # MAP BACKWARD: Convert 4-64 scale into a 0.0-10.0 scale for the slider
        slider_target = ((current_val - 4) / 60.0) * 10.0
        
        ge("length_slider").value = slider_target
        ge("password_display").value = generate_password(current_val)
    except ValueError:
        pass 

password_length_input.oninput = sync_from_input
ba(password_length_input)

# ===
# SLIDER
# ===
length_slider = ce('slider')
length_slider.id = "length_slider"
# We don't try to set .min or .max here anymore, we accept the engine's 0-10 default

def sync_from_slider():
    # Grab the engine's raw 0.0 to 10.0 value
    raw_slider = float(ge("length_slider").value)
    
    # MAP FORWARD: Translate the 0-10 position into a 4-64 character length
    percentage = raw_slider / 10.0
    current_val = int(4 + (percentage * 60))
    
    ge("length_input").value = current_val
    ge("password_display").value = generate_password(current_val)

length_slider.oninput = sync_from_slider
ba(length_slider)

# ===
# RANDOM BUTTON BLOCK
# ===
random_btn = ce('button')
random_btn.id = "random_btn"
random_btn.textContent = "Random"

def handle_click():
    current_val = int(ge("length_input").value)
    ge("password_display").value = generate_password(current_val)

random_btn.onclick = handle_click
ba(random_btn)

# ===
# BOOT INITIALIZATION
# ===
# Set input to 12
ge("length_input").value = 12
# Set slider to the mathematical equivalent of 12 (which is 1.33 on the 0-10 scale)
ge("length_slider").value = ((12 - 4) / 60.0) * 10.0
# Generate initial password
ge("password_display").value = generate_password(12)

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

