# CODE BOOK

---

<details>
<summary><b>Section: 018_scroll_div</b></summary>


### `scroll_div.py`

```python

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

```


</details>

---

<details>
<summary><b>Section: 019_scroll_div</b></summary>


### `scroll_div.py`

```python

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

```


</details>


---
