# scroll_div.py

from pyside6dom import *

init_window("Manual Scroll Div Example", 450, 450)

# ===
# THE OUTER CARD (Optional)
# Note for beginners: You do NOT need a 'div' to use a 'scroll_div'.
# We are just using this outer div as a cosmetic box to make things look nice.
# ===
card = ce('div')
card.style("background-color: #2b2b2b; border-radius: 10px; padding: 15px; border: 2px solid #555;")
ba(card) # Attach the card to the main window

title = ce('h1')
title.innerHTML = "<b>Starfleet Cargo Manifest</b>"
title.style("color: #4da6ff; font-size: 18px;")
ba(title, card) # Attach title to the card

# ===
# THE SCROLL DIV
# This is the actual scrolling window. We give it a fixed height so it 
# runs out of room and forces a scrollbar to appear.
# ===
inventory_list = ce('scroll_div')
inventory_list.style("background-color: #1a1a1a; min-height: 200px; max-height: 200px; padding: 5px;")
ba(inventory_list, card) # Attach the scroll box to the card

# ===
# MANUAL ENTRIES
# We create text elements one by one and attach them to the scroll_div.
# ===

item1 = ce('text')
item1.textContent = "1. Dilithium Crystals - 4 Crates"
item1.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item1, inventory_list)

item2 = ce('text')
item2.textContent = "2. Phaser Rifles - 12 Units"
item2.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item2, inventory_list)

item3 = ce('text')
item3.textContent = "3. Medical Tricorders - 8 Units"
item3.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item3, inventory_list)

item4 = ce('text')
item4.textContent = "4. Emergency Rations - 500 Packs"
item4.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item4, inventory_list)

item5 = ce('text')
item5.textContent = "5. Warp Plasma Conduits - 2 Spools"
item5.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item5, inventory_list)

item6 = ce('text')
item6.textContent = "6. Deflector Dish Emitters - 1 Array"
item6.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item6, inventory_list)

item7 = ce('text')
item7.textContent = "7. Photon Torpedo Casings - 6 Units"
item7.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item7, inventory_list)

item8 = ce('text')
item8.textContent = "8. Bio-Bed Sensor Pads - 4 Units"
item8.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item8, inventory_list)

item9 = ce('text')
item9.textContent = "9. Replicator Matter Supply - 10 Barrels"
item9.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item9, inventory_list)

item10 = ce('text')
item10.textContent = "10. Class-F Shuttle Parts - 3 Crates"
item10.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item10, inventory_list)

# ===
# A BUTTON AT THE BOTTOM
# Because this is attached to the 'card' and not the 'scroll_div', 
# it stays locked at the bottom of the screen
# ===
btn = ce('button')
btn.textContent = "Lock Cargo Bay Doors"
btn.style("background-color: #4da6ff; color: #1e1e1e; font-weight: bold; margin-top: 10px;")
ba(btn, card) # Attach to the card

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

