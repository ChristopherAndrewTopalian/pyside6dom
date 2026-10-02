from pyside6dom import *

# Import Qt's keyboard listener tools
from PySide6.QtGui import QShortcut, QKeySequence

init_window('Continuous Movement + WASD', 700, 600)

# OUR STATE 
state = {
    "x": 0,
    "timer": None
}

# THE PLAYER (The Cube)
player = ce('div')
player.id = 'player'
player.style.border = '2px solid rgb(0, 255, 200)'
player.style.background = 'rgb(20, 100, 150)'
player.style.width = 100
player.style.height = 100
player.style.position = 'absolute'
player.style.left = state["x"]
player.style.top = 100
ba(player)

# THE BUTTON CONTAINER FIX
move_btn_container = ce('div')
move_btn_container.style.display = 'flex'
move_btn_container.style.flexDirection = 'row'
move_btn_container.style.position = 'absolute'
move_btn_container.style.top = 230
# Hard dimensions prevent Qt from collapsing it
move_btn_container.style.width = 400 
move_btn_container.style.height = 50 
ba(move_btn_container)

# MOVEMENT LOGIC
def stop_moving():
    if state["timer"]:
        clearInterval(state["timer"])
        state["timer"] = None

def move_left():
    stop_moving() 
    def loop():
        state["x"] -= 5
        player.style.left = state["x"]
    state["timer"] = setInterval(loop, 20)

def move_right():
    stop_moving()
    def loop():
        state["x"] += 5
        player.style.left = state["x"]
    state["timer"] = setInterval(loop, 20)

# ATTACH BUTTONS
btn_left = ce('button')
btn_left.textContent = '<< Left (A)'
btn_left.onclick = move_left
move_btn_container.append(btn_left)

btn_stop = ce('button')
btn_stop.textContent = 'STOP (S)'
btn_stop.onclick = stop_moving
btn_stop.style.color = 'salmon'
move_btn_container.append(btn_stop)

btn_right = ce('button')
btn_right.textContent = 'Right (D) >>'
btn_right.onclick = move_right
move_btn_container.append(btn_right)

# ===
# WASD KEYBOARD CONTROLS
# QShortcut is Qt's version of addEventListener('keydown')!
# ===

QShortcut(QKeySequence("A"), player.raw).activated.connect(move_left)
QShortcut(QKeySequence("D"), player.raw).activated.connect(move_right)
QShortcut(QKeySequence("S"), player.raw).activated.connect(stop_moving)

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

