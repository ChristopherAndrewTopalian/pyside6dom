# move_div_left_right.py

from pyside6dom import *

init_window('OurApp', 700, 600)

player = ce('div')
player.id = 'player'
player.style.border = '1px solid rgb(255, 255, 255)'
player.style.width = 100
player.style.height = 100
player.style.position = 'absolute'
player.style.left = 0
player.style.top = 100
ba(player)

move_btn_container = ce('div')
move_btn_container.style.display = 'flex'
move_btn_container.style.flexDirection = 'row'
ba(move_btn_container)

move_left_btn = ce('button')
move_left_btn.textContent = 'Left'
def move_left():
    player.style.left -= 1
move_left_btn.onclick = move_left
move_btn_container.append(move_left_btn)

move_right_btn = ce('button')
move_right_btn.textContent = 'Right'
def move_right():
    player.style.left += 1
move_right_btn.onclick = move_right
move_btn_container.append(move_right_btn)

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

