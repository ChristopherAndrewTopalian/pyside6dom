# true_ai.pyw


import sys
import os

# Local Testing
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window('TRUE AI', 1100, 675, 'true_ai.png')

A = 1
B = 1

main_div = ce('div')
main_div.style.display = 'flex'
main_div.style.flexDirection = 'row'
ba(main_div)

left_panel = ce('div')
left_panel.style.display = 'flex'
left_panel.style.flexDirection = 'column'
left_panel.style.border = '1px solid white'
left_panel.style.padding = '5px'
main_div.append(left_panel)

####
# GROUP 1
####

tau_label = ce('div')
tau_label.textContent = str(TAU(A, B)) + ' TAU'
left_panel.append(tau_label)

con_label = ce('div')
con_label.textContent = str(CON(A, B)) + ' CON'
left_panel.append(con_label)

xor_label = ce('div')
xor_label.textContent = str(XOR(A, B)) + ' XOR'
left_panel.append(xor_label)

xnor_label = ce('div')
xnor_label.textContent = str(XNOR(A, B)) + ' XNOR'
left_panel.append(xnor_label)

####
# GROUP 2
####

and_label = ce('div')
and_label.textContent = str(AND(A, B)) + ' AND'
left_panel.append(and_label)

nand_label = ce('div')
nand_label.textContent = str(NAND(A, B)) + ' NAND'
left_panel.append(nand_label)

or_label = ce('div')
or_label.textContent = str(OR(A, B)) + ' OR'
left_panel.append(or_label)

nor_label = ce('div')
nor_label.textContent = str(NOR(A, B)) + ' NOR'
left_panel.append(nor_label)

####
# GROUP 3
####

mi_label = ce('div')
mi_label.textContent = str(MI(A, B)) + ' MI'
left_panel.append(mi_label)

mni_label = ce('div')
mni_label.textContent = str(MNI(A, B)) + ' MNI'
left_panel.append(mni_label)

ci_label = ce('div')
ci_label.textContent = str(CI(A, B)) + ' CI'
left_panel.append(ci_label)

cni_label = ce('div')
cni_label.textContent = str(CNI(A, B)) + ' CNI'
left_panel.append(cni_label)

####
# GROUP 4
####

lp_label = ce('div')
lp_label.textContent = str(LP(A, B)) + ' LP'
left_panel.append(lp_label)

lc_label = ce('div')
lc_label.textContent = str(LC(A, B)) + ' LC'
left_panel.append(lc_label)

rp_label = ce('div')
rp_label.textContent = str(RP(A, B)) + ' RP'
left_panel.append(rp_label)

rc_label = ce('div')
rc_label.textContent = str(RC(A, B)) + ' RC'
left_panel.append(rc_label)

####

right_panel = ce('div')
right_panel.style.border = '1px solid white'
main_div.append(right_panel)

true_ai_diagram = ce('img')
true_ai_diagram.src = 'true_ai.png'
true_ai_diagram.width = 625
right_panel.append(true_ai_diagram)

####

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

