# true_ai.pyw

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
ba(left_panel, main_div)

####
# GROUP 1
####

tau_label = ce('text')
tau_label.textContent = str(TAU(A, B)) + ' TAU'
ba(tau_label, left_panel)

con_label = ce('text')
con_label.textContent = str(CON(A, B)) + ' CON'
ba(con_label, left_panel)

xor_label = ce('text')
xor_label.textContent = str(XOR(A, B)) + ' XOR'
ba(xor_label, left_panel)

xnor_label = ce('text')
xnor_label.textContent = str(XNOR(A, B)) + ' XNOR'
ba(xnor_label, left_panel)

####
# GROUP 2
####

and_label = ce('text')
and_label.textContent = str(AND(A, B)) + ' AND'
ba(and_label, left_panel)

nand_label = ce('text')
nand_label.textContent = str(NAND(A, B)) + ' NAND'
ba(nand_label, left_panel)

or_label = ce('text')
or_label.textContent = str(OR(A, B)) + ' OR'
ba(or_label, left_panel)

nor_label = ce('text')
nor_label.textContent = str(NOR(A, B)) + ' NOR'
ba(nor_label, left_panel)

####
# GROUP 3
####

mi_label = ce('text')
mi_label.textContent = str(MI(A, B)) + ' MI'
ba(mi_label, left_panel)

mni_label = ce('text')
mni_label.textContent = str(MNI(A, B)) + ' MNI'
ba(mni_label, left_panel)

ci_label = ce('text')
ci_label.textContent = str(CI(A, B)) + ' CI'
ba(ci_label, left_panel)

cni_label = ce('text')
cni_label.textContent = str(CNI(A, B)) + ' CNI'
ba(cni_label, left_panel)

####
# GROUP 4
####

lp_label = ce('text')
lp_label.textContent = str(LP(A, B)) + ' LP'
ba(lp_label, left_panel)

lc_label = ce('text')
lc_label.textContent = str(LC(A, B)) + ' LC'
ba(lc_label, left_panel)

rp_label = ce('text')
rp_label.textContent = str(RP(A, B)) + ' RP'
ba(rp_label, left_panel)

rc_label = ce('text')
rc_label.textContent = str(RC(A, B)) + ' RC'
ba(rc_label, left_panel)

####

right_panel = ce('div')
right_panel.style.border = '1px solid white'
ba(right_panel, main_div)

true_ai_diagram = ce('img')
true_ai_diagram.src = 'true_ai.png'
true_ai_diagram.width = 625
ba(true_ai_diagram, right_panel)

####

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting

