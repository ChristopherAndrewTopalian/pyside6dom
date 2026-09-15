# one_dimensional_array.py

import numpy as np
from pyside6dom import *

init_window("One Dimensional Array", 400, 300)

# We make a one-dimensional array
our_array = np.array([10, 17, 41, 19, 16, 8])

# Display it in the UI instead of the console
array_txt = ce('text')
array_txt.textContent = f"Our 1D Array:\n{our_array}"
ba(array_txt)

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

