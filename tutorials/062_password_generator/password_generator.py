# password_generator.py

from pyside6dom import *

init_window('OurApp', 700, 600)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')','_']

def generate_password():
    all = letters + numbers + symbols

    password = random.sample(all, 12)

    password_string = ", ".join(map(str, password))

    password = password_string.replace(",", "")    
    return password


password_div = ce('div')
password_div.textContent = generate_password()
password_div.style.fontSize = '30px'
password_div.style.fontWeight = 'bold'
ba(password_div)

random_password_btn = ce('button')
random_password_btn.textContent = 'Random'
def handle_click():
    password_div.textContent = generate_password()
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

