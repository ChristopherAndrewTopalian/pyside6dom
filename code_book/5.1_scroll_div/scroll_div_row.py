# scroll_div_row.py

from pyside6dom import *

init_window('OurApp', 700, 600)

top_container = ce('scroll_div')
top_container.style.display = 'flex'
top_container.style.flexDirection = 'row'
top_container.style.height = '70px' 
ba(top_container)

btn1 = ce('button')
btn1.textContent = 'btn1'
btn1.onclick = lambda: print('btn1')
ba(btn1, top_container)

btn2 = ce('button')
btn2.textContent = 'btn2'
btn2.onclick = lambda: print('btn2')
ba(btn2, top_container)

btn3 = ce('button')
btn3.textContent = 'btn3'
btn3.onclick = lambda: print('btn3')
ba(btn3, top_container)

btn4 = ce('button')
btn4.textContent = 'btn4'
btn4.onclick = lambda: print('btn4')
ba(btn4, top_container)

btn5 = ce('button')
btn5.textContent = 'btn5'
btn5.onclick = lambda: print('btn5')
ba(btn5, top_container)

btn6 = ce('button')
btn6.textContent = 'btn6'
btn6.onclick = lambda: print('btn6')
ba(btn6, top_container)

btn7 = ce('button')
btn7.textContent = 'btn7'
btn7.onclick = lambda: print('btn7')
ba(btn7, top_container)

btn8 = ce('button')
btn8.textContent = 'btn8'
btn8.onclick = lambda: print('btn8')
ba(btn8, top_container)

btn9 = ce('button')
btn9.textContent = 'btn9'
btn9.onclick = lambda: print('btn9')
ba(btn9, top_container)

btn10 = ce('button')
btn10.textContent = 'btn10'
btn10.onclick = lambda: print('btn10')
ba(btn10, top_container)

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

