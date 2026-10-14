# true_si_hypercube.py

from pyside6dom import *
import random

init_window('True SI - Hypercube Structure', 700, 600)

# We map each of the 16 logic gates to a 4D coordinate (w, x, y, z)
# This creates the mathematical "structure" of the tesseract
hypercube_nodes = {
    "TAU":  {"coords": (0, 0, 0, 0), "value": 1},
    "CON":  {"coords": (0, 0, 0, 1), "value": 1},
    "XOR":  {"coords": (0, 0, 1, 0), "value": 1},
    "XNOR": {"coords": (0, 0, 1, 1), "value": 1},
    "AND":  {"coords": (0, 1, 0, 0), "value": 1},
    "NAND": {"coords": (0, 1, 0, 1), "value": 1},
    "OR":   {"coords": (0, 1, 1, 0), "value": 1},
    "NOR":  {"coords": (0, 1, 1, 1), "value": 1},
    "MI":   {"coords": (1, 0, 0, 0), "value": 1},
    "MNI":  {"coords": (1, 0, 0, 1), "value": 1},
    "CI":   {"coords": (1, 0, 1, 0), "value": 1},
    "CNI":  {"coords": (1, 0, 1, 1), "value": 1},
    "LP":   {"coords": (1, 1, 0, 0), "value": 1},
    "LC":   {"coords": (1, 1, 0, 1), "value": 1},
    "RP":   {"coords": (1, 1, 1, 0), "value": 1},
    "RC":   {"coords": (1, 1, 1, 1), "value": 1}
}

a = 0
b = 0

def random_inputs():
    global a, b
    a = random.randint(0, 1)
    b = random.randint(0, 1)

def thinking():
    # In a real implementation, we would define the actual logic for TAU(a,b), XOR(a,b), etc.
    # For now, we simulate the state changes across the nodes based on the inputs
    for gate, data in hypercube_nodes.items():
        # Example placeholder logic: shifting states based on inputs
        data["value"] = (data["value"] + a + b) % 2 

def show_thoughts():
    # We can output the current state of the entire network to the DOM
    display_text = "Current Network State:\n"
    for gate, data in hypercube_nodes.items():
        display_text += f"{gate} {data['coords']}: {data['value']}\n"
    
    result_div.textContent = display_text

# UI Setup
result_div = ce('div')
result_div.style.fontFamily = 'Courier New' # Monospace keeps the coordinates aligned
result_div.style.fontSize = '20px'
result_div.style.whiteSpace = 'pre'
result_div.style.color = 'rgb(0, 255, 255)'
result_div.style.padding = '20px'
ba(result_div)

# Loops
setInterval(random_inputs, 1000)
setInterval(thinking, 1000)
setInterval(show_thoughts, 1000)

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

