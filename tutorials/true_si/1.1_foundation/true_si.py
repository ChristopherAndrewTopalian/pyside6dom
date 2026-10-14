# true_si.py

from pyside6dom import *
import random

init_window('True SI', 700, 600)

a = 0
b = 0

our_tau = 1
our_con = 1
our_xor = 1
our_xnor = 1
our_and = 1
our_nand = 1
our_or = 1
our_nor = 1
our_mi = 1
our_mni = 1
our_ci = 1
our_cni = 1
our_lp = 1
our_lc = 1
our_rp = 1
our_rc = 1

def random_inputs():
    global a, b
    # randint(0, 1) ensures we strictly get 0 or 1, not floats
    a = random.randint(0, 1)
    b = random.randint(0, 1)

def thinking():
    try:
        global our_tau, our_con, our_xor, our_xnor
        global our_and, our_nand, our_or, our_nor
        global our_mi, our_mni, our_ci, our_cni
        global our_lp, our_lc, our_rp, our_rc

        our_tau = TAU(a, b)
        our_con = CON(a, b)
        
        our_xor = XOR(a, b)
        our_xnor = XNOR(a, b)
        
        our_and = AND(a, b)
        our_nand = NAND(a, b)
        our_or = OR(a, b)
        our_nor = NOR(a, b)
        
        our_mi = MI(a, b)
        our_mni = MNI(a, b)
        our_ci = CI(a, b)
        our_cni = CNI(a, b)
        
        our_lp = LP(a, b)
        our_lc = LC(a, b)
        our_rp = RP(a, b)
        our_rc = RC(a, b)
        
    except Exception as error:
        # If any gate fails, we catch the error to keep the timer alive
        print(f"Error in thinking matrix: {error}")

def show_thoughts():
    ge('results_div').textContent = (
        'TAU: ' + str(our_tau) + '\n' +
        'CON: ' + str(our_con) + '\n' +
        'XOR: ' + str(our_xor) + '\n' +
        'XNOR: ' + str(our_xnor) + '\n' +
        'AND: ' + str(our_and) + '\n' +
        'NAND: ' + str(our_nand) + '\n' +
        'OR: ' + str(our_or) + '\n' +
        'NOR: ' + str(our_nor) + '\n' +
        'MI: ' + str(our_mi) + '\n' +
        'MNI: ' + str(our_mni) + '\n' +
        'CI: ' + str(our_ci) + '\n' +
        'CNI: ' + str(our_cni) + '\n' +
        'LP: ' + str(our_lp) + '\n' +
        'LC: ' + str(our_lc) + '\n' +
        'RP: ' + str(our_rp) + '\n' +
        'RC: ' + str(our_rc) + '\n'
    )

results_div = ce('div')
results_div.id = 'results_div'
results_div.style.whiteSpace = 'pre'
results_div.style.fontSize = '30px'
results_div.style.fontFamily = 'Arial'
results_div.style.fontWeight = 'bold'
results_div.style.padding = '20px'
results_div.textContent = 'Initializing thoughts...'
ba(results_div)

# environment loop
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

