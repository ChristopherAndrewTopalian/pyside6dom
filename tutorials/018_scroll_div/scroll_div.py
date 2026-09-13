# scroll_div.py

from pyside6dom import *

init_window("Div and Scroll Div", 500, 550)

# The Standard Div (The outer "Card")
# A standard div stretches to hold whatever is inside it. It provides structure.
card = ce('div')
card.style("background-color: #2b2b2b; border-radius: 10px; padding: 15px;")
ba(card) # Append to main window

title = ce('h1')
title.innerHTML = "<b>Warp Core Diagnostic Logs</b>"
title.style("color: #ff9900; font-size: 20px;")
ba(title, card)

# The Scroll Div (The inner "Viewport")
# By giving it a fixed height, it forces a scrollbar when content exceeds 250px.
log_window = ce('scroll_div')
log_window.style("background-color: #1a1a1a; border: 1px solid #ff9900; min-height: 250px; max-height: 250px;")
ba(log_window, card)

# Generate 30 entries to force the log window to overflow and scroll
for i in range(1, 31):
    # We create a mini standard div for each row just to give it a bottom border
    row = ce('div')
    row.style("border-bottom: 1px solid #333333; padding: 2px;")
    
    txt = ce('text')
    txt.textContent = f"Stardate {45000 + i}.{i*3} - Relay {i} stabilized. Coolant nominal."
    
    # Simulate a warning on the 15th log entry
    if i == 15:
        txt.textContent = f"Stardate {45000 + i}.{i*3} - WARNING: Micro-fracture detected in Relay {i}!"
        txt.style("color: #ff3333; font-family: monospace; font-weight: bold;")
    else:
        txt.style("color: #00cc66; font-family: monospace;")
        
    ba(txt, row)
    ba(row, log_window) # Append the row to the scrollable log window

# A button at the bottom of the static card
btn = ce('button')
btn.textContent = "Acknowledge Alerts"
btn.style("background-color: #ff9900; color: #1e1e1e; font-weight: bold; margin-top: 10px;")
ba(btn, card)

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

