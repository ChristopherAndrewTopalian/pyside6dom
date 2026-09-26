# sound.py

from pyside6dom import *

init_window("Sound Test", 400, 300)

set_theme("""
    body { background-color: rgb(30, 30, 30); }
    button {
        padding: 20px;
        font-size: 24px;
        font-weight: bold;
        background-color: rgb(50, 50, 60);
        color: white;
        border: 2px solid white;
        border-radius: 10px;
        margin: 50px;
    }
""")

# Create the button
btn = ce('button')
btn.textContent = "Hover and Click Me!"
ba(btn)

# Option 1: Use a lambda for a quick inline sound
btn.onmouseover = lambda: play_sound('hover.wav')

# Option 2: Use a standard function to play the sound AND do logic
def handle_click():
    play_sound('click.wav')
    print("Action executed!")
    btn.style.backgroundColor = "rgb(0, 255, 200)" # Visual feedback

btn.onclick = handle_click

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

