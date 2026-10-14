# true_si_hypercube.py

from pyside6dom import *
import random

init_window('True SI - Active Hypercube', 750, 700)

# We map each gate to its truth-table coordinate and assign its distinct logic function
hypercube_nodes = {
    "CON":  {"coords": (0, 0, 0, 0), "value": 0, "func": lambda a, b: 0},
    "AND":  {"coords": (0, 0, 0, 1), "value": 0, "func": lambda a, b: a & b},
    "MNI":  {"coords": (0, 0, 1, 0), "value": 0, "func": lambda a, b: 1 if a > b else 0},
    "LP":   {"coords": (0, 0, 1, 1), "value": 0, "func": lambda a, b: a},
    "CNI":  {"coords": (0, 1, 0, 0), "value": 0, "func": lambda a, b: 1 if b > a else 0},
    "RP":   {"coords": (0, 1, 0, 1), "value": 0, "func": lambda a, b: b},
    "XOR":  {"coords": (0, 1, 1, 0), "value": 0, "func": lambda a, b: a ^ b},
    "OR":   {"coords": (0, 1, 1, 1), "value": 0, "func": lambda a, b: a | b},
    "NOR":  {"coords": (1, 0, 0, 0), "value": 0, "func": lambda a, b: 1 - (a | b)},
    "XNOR": {"coords": (1, 0, 0, 1), "value": 0, "func": lambda a, b: 1 - (a ^ b)},
    "RC":   {"coords": (1, 0, 1, 0), "value": 0, "func": lambda a, b: 1 - b},
    "MI":   {"coords": (1, 0, 1, 1), "value": 0, "func": lambda a, b: 1 if a <= b else 0},
    "LC":   {"coords": (1, 1, 0, 0), "value": 0, "func": lambda a, b: 1 - a},
    "CI":   {"coords": (1, 1, 0, 1), "value": 0, "func": lambda a, b: 1 if b <= a else 0},
    "NAND": {"coords": (1, 1, 1, 0), "value": 0, "func": lambda a, b: 1 - (a & b)},
    "TAU":  {"coords": (1, 1, 1, 1), "value": 0, "func": lambda a, b: 1}
}

a = 0
b = 0

def random_inputs():
    global a, b
    a = random.randint(0, 1)
    b = random.randint(0, 1)

def thinking():
    # Each node now evaluates the inputs using its own specific logic function
    for gate, data in hypercube_nodes.items():
        data["value"] = data["func"](a, b)

def show_thoughts():
    display_text = f"Energy Inputs -> A: {a} | B: {b}\n"
    display_text += "=" * 32 + "\n\n"
    
    for gate, data in hypercube_nodes.items():
        coord_str = f"{data['coords'][0]}{data['coords'][1]}{data['coords'][2]}{data['coords'][3]}"
        
        # We format the string so the columns align perfectly
        display_text += f"{gate.ljust(5)} at {coord_str} : State [ {data['value']} ]\n"
    
    result_div.textContent = display_text

####

# UI Setup
set_theme('''
    body {
        background-color: rgb(15, 15, 20);
        color: rgb(0, 255, 255);
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
        padding: 20px;
    }
''')

result_div = ce('div')
result_div.style.whiteSpace = 'pre'
result_div.textContent = 'Initializing hypercube vessel...'
ba(result_div)

# Active Loops
inputs_timer = setInterval(random_inputs, 1000)
think_timer = setInterval(thinking, 1000)
results_timer = setInterval(show_thoughts, 1000)

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

