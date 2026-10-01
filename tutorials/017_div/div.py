# div.py

from pyside6dom import *

init_window("Div Container Example", 500, 400)

# Create the parent div (a "Card")
card = ce('div')
card.style.backgroundColor = 'rgb(0, 0, 0)'
card.style.border = '2px solid rgb(255, 255, 255)'
card.style.borderRadius = '8px'
card.style.padding = '15px'
#card.style("background-color: #2b2b2b; border-radius: 10px; border: 2px solid #4da6ff; padding: 15px;")
# Append the completely built card to the main window
ba(card)

# Create elements to go INSIDE the div
our_title = ce('h1')
our_title.textContent = "Starfleet Engineering"
our_title.style.fontWeight = 'bold'
our_title.style.fontSize = '20px'
our_title.style.fontColor = 'rgb(255, 255, 255)'
#our_title.style("color: #4da6ff; font-size: 20px;")
ba(our_title, card) # Append our_title TO the card (passing card as the parent)

description = ce('text')
description.textContent = "Warp core status: Nominal. Ready for deployment."
description.style("color: #e0e0e0;")
ba(description, card) # Append text TO the card

run_btn = ce('button')
run_btn.textContent = "Run Diagnostics"
run_btn.style.backgroundColor = '#4da6ff'
run_btn.style.fontWeight = 'bold'
run_btn.style.padding = '6px'
#run_btn.style("background-color: #4da6ff; color: #1e1e1e; font-weight: bold; padding: 6px;")
run_btn.onclick = lambda: print('hi')
ba(run_btn, card) # Append button TO the card

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

