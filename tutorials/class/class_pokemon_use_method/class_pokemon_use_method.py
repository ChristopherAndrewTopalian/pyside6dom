# class_pokemon_use_method.py

from pyside6dom import *

init_window('PySide6DOM Pokedex', 800, 600)

set_theme("""
    body { background-color: rgb(25, 25, 30); color: white; font-family: 'Segoe UI', Arial; }
    
    .summon_btn {
        background-color: rgb(50, 50, 60);
        color: white;
        border: 2px solid rgb(100, 100, 120);
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
        font-size: 16px;
    }
    .summon_btn:hover { background-color: rgb(80, 80, 90); border-color: white; }
    
    .poke_card {
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.5);
    }
""")

# ===
# THE CLASS
# ===
class Pokemon:
    def __init__(self, name, kind, hex_color):
        self.name = name
        self.kind = kind
        self.color = hex_color

    def renderCard(self, parent_container):
        """Builds a DOM Div and appends it to the container"""
        card = ce('div')
        card.className = 'poke_card'
        card.style.backgroundColor = self.color
        card.style.display = 'flex'
        card.style.flexDirection = 'column'
        card.style.padding = 15  
        card.style.width = 250
        
        name_lbl = ce('h1')
        name_lbl.textContent = self.name
        name_lbl.style.margin = 0
        name_lbl.style.color = 'white'
        card.append(name_lbl)
        
        kind_lbl = ce('text')
        kind_lbl.textContent = f"Type: {self.kind}"
        kind_lbl.style.fontSize = '18px'
        kind_lbl.style.fontWeight = 'bold'
        kind_lbl.style.color = 'rgba(255, 255, 255, 0.8)'
        card.append(kind_lbl)

        parent_container.append(card)

# ===
# BUILD THE UI LAYOUT
# ===
main_row = ce('div')
main_row.style.display = 'flex'
main_row.style.flexDirection = 'row'
main_row.style.gap = 40  # Our new flex gap!
main_row.style.padding = 30
ba(main_row)

# Left Column: Buttons
controls = ce('div')
controls.style.display = 'flex'
controls.style.flexDirection = 'column'
controls.style.gap = 15
main_row.append(controls)

# Right Column: The Pokedex Screen
pokedex_screen = ce('scroll_div')
pokedex_screen.style.width = 350
pokedex_screen.style.height = 500
pokedex_screen.style.backgroundColor = 'rgb(15, 15, 18)'
pokedex_screen.style.border = '3px solid rgb(100, 100, 100)'
pokedex_screen.style.padding = 15 # Internal padding so cards don't touch the edges
main_row.append(pokedex_screen)

# ===
# INSTANTIATE DATA & LOGIC
# ===
roster = [
    Pokemon("Pikachu", "Electric", "#D4A017"),
    Pokemon("Charmander", "Fire", "#C0392B"),
    Pokemon("Bulbasaur", "Grass", "#27AE60"),
    Pokemon("Squirtle", "Water", "#2980B9")
]

# Generate a button for every Pokemon in our array
for poke in roster:
    btn = ce('button')
    btn.className = 'summon_btn'
    btn.textContent = f"Summon {poke.name}"
    
    # Freeze the current 'poke' variable into the lambda!
    btn.onclick = lambda p=poke: p.renderCard(pokedex_screen)
    
    controls.append(btn)

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

