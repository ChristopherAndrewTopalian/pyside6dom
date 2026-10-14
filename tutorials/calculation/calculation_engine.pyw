# calculation_engine.pyw

from pyside6dom import *

rectangle_area = os.path.join(os.getcwd(), 'geometry', 'rectangle', 'area_of_a_rectangle.pyw')

perimeter_area = os.path.join(os.getcwd(), 'geometry', 'rectangle', 'perimeter_of_a_rectangle.pyw')

init_window('Calculation Engine', 700, 600)

our_container = ce('div')
our_container.style.display = 'flex'
our_container.style.flexDirection = 'column'
ba(our_container)

area_of_rect_btn = ce('button')
area_of_rect_btn.textContent = 'Area of a Rectangle'
area_of_rect_btn.onclick = lambda: dom.open_file(rectangle_area)
area_of_rect_btn.oncontextmenu = lambda: dom.show_in_file_explorer(rectangle_area)
our_container.append(area_of_rect_btn)

perimeter_of_rect_btn = ce('button')
perimeter_of_rect_btn.textContent = 'Perimeter of a Rectangle'
perimeter_of_rect_btn.onclick = lambda: dom.open_file(perimeter_area)
perimeter_of_rect_btn.oncontextmenu = lambda: dom.show_in_file_explorer(perimeter_area)
our_container.append(perimeter_of_rect_btn)

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
# College of Scripting Music & Science
#
# GitHub: https://github.com/ChristopherAndrewTopalian
#
# GitHub: https://github.com/ChristopherTopalian
# Google Sites: https://sites.google.com/view/CollegeOfScripting

