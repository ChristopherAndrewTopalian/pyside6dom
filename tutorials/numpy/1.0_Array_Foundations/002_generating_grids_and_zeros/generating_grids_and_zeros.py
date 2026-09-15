# generating_grids_and_zeros.py

import numpy as np
from pyside6dom import *

init_window("Generating Grids and Zeros", 600, 650)

# Generating an Empty Search Grid (Zeros)
zeros_txt = ce('text')
search_grid = np.zeros((5, 5), dtype=int)
zeros_txt.textContent = f"1. Generating an Empty Search Grid (Zeros)\n5x5 Grid:\n{search_grid}"
ba(zeros_txt)

# Generating an Active Status Grid (Ones)
ones_txt = ce('text')
active_sensors = np.ones((3, 4), dtype=int)
ones_txt.textContent = f"\n2. Generating an Active Status Grid (Ones)\n3x4 Grid:\n{active_sensors}"
ba(ones_txt)

# Generating a Custom Filled Grid
full_txt = ce('text')
water_map = np.full((4, 4), 7)
full_txt.textContent = f"\n3. Generating a Custom Filled Grid\n4x4 Grid filled with 7:\n{water_map}"
ba(full_txt)

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

