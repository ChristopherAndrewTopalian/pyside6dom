# div.py

from pyside6dom import *

init_window("Div Container Example", 500, 400)

# Create the parent div (a "Card")
card = ce('div')
# Notice we use the style method to give the div a background and border
card.style("background-color: #2b2b2b; border-radius: 10px; border: 2px solid #4da6ff; padding: 15px;")
# Append the completely built card to the main window
ba(card)

# Create elements to go INSIDE the div
title = ce('h1')
title.innerHTML = "<b>Starfleet Engineering</b>"
title.style("color: #4da6ff; font-size: 20px;")
ba(title, card) # Append title TO the card (passing card as the parent)

desc = ce('text')
desc.textContent = "Warp core status: Nominal. Ready for deployment."
desc.style("color: #e0e0e0;")
ba(desc, card) # Append text TO the card

btn = ce('button')
btn.textContent = "Run Diagnostics"
btn.style("background-color: #4da6ff; color: #1e1e1e; font-weight: bold; padding: 6px;")
ba(btn, card) # Append button TO the card

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

