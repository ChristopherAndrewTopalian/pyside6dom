# wasd_player_addEventListener.py

from pyside6dom import *

init_window('WASD Player with addEventListener', 600, 600)

set_theme('''
    body { 
        background-color: rgb(30, 30, 30); 
        color: white; 
        font-family: Arial; 
    }
    .player_box {
        background-color: #00ffcc;
        border-radius: 8px;
        border: 2px solid white;
    }
    .control_btn {
        background-color: #555;
        color: white;
        padding: 10px;
        font-size: 16px;
        border-radius: 4px;
        font-weight: bold;
    }
''')

# ===
# STATE VARIABLES
# ===
player_x = 250
player_y = 250
speed = 25

# ===
# BUILD THE UI
# ===
# The UI wrapper for our controls
ui_layer = ce('div')
ui_layer.style.padding = 20
ba(ui_layer)

instruction_lbl = ce('h2')
instruction_lbl.textContent = "Use W, A, S, D to Move. Hit 'Enter' to reset."
ba(instruction_lbl, ui_layer)

reset_btn = ce('button')
reset_btn.className = 'control_btn'
reset_btn.textContent = 'Reset Position'
ba(reset_btn, ui_layer)

# The Player Cube (Absolute Positioned)
player = ce('div')
player.className = 'player_box'
player.style.position = 'absolute'
player.style.width = 50
player.style.height = 50
player.style.left = player_x
player.style.top = player_y
ba(player)

# ===
# LOGIC & EVENT SWITCHBOARD
# ===

def reset_position():
    global player_x, player_y
    player_x = 250
    player_y = 250
    player.style.left = player_x
    player.style.top = player_y

# FEATURE 1: Stacking Events on a single Element 
def hover_in(): 
    reset_btn.style.backgroundColor = '#ff0055'

def hover_out(): 
    reset_btn.style.backgroundColor = '#555'

# Notice how we stack three completely different listeners on ONE button!
# This is impossible with standard '.onclick'
reset_btn.addEventListener('click', reset_position)
reset_btn.addEventListener('mouseenter', hover_in)
reset_btn.addEventListener('mouseleave', hover_out)

# FEATURE 2: Global Window Keyboard Capture
def handle_keys(event):
    global player_x, player_y
    
    # We use event.key exactly like JavaScript
    key = event.key.lower()
    
    if key == 'w': player_y -= speed
    elif key == 's': player_y += speed
    elif key == 'a': player_x -= speed
    elif key == 'd': player_x += speed
    
    # We intercept your normalized 'Enter' key
    elif key == 'enter': 
        reset_position()
        return # Skip the movement logic
        
    # Apply the new coordinates to the engine
    player.style.left = player_x
    player.style.top = player_y

# Attach the keyboard listener to the whole window
window.addEventListener('keydown', handle_keys)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting

