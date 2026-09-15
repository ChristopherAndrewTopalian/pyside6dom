# boolean_masking.py

import numpy as np
from pyside6dom import *

init_window("Boolean Masking", 650, 600)

# 1D Boolean Masking (Thermal Anomaly Detection)
mask_txt = ce('text')

# A drone scans a line of ocean water. Most temps are freezing (around 32F).
# A human body will register much higher (around 98F).
ocean_scan = np.array([32, 33, 31, 98, 32, 97, 34])

# Step A: Create the "Mask" (Ask the true/false question)
# This instantly creates an array of True/False values
is_survivor = ocean_scan > 90

# Step B: Apply the Mask
# NumPy physically extracts only the data points where the mask is True
survivors_found = ocean_scan[is_survivor]

mask_txt.textContent = (
    f"1. 1D Boolean Masking (Thermal Anomaly Detection)\n"
    f"Raw Ocean Scan    : {ocean_scan}\n"
    f"Logical Mask      : {is_survivor}\n"
    f"Anomalies Found   : {survivors_found}"
)
ba(mask_txt)


# 2D Boolean Replacement (Signal Cleanup)
cleanup_txt = ce('text')

# Imagine a 3x3 grid of sonar data.
# Any negative number is static/noise that we need to zero out.
sonar_data = np.array([
    [ 15, -5,  22],
    [-10,  8,  14],
    [ 30, 25, -2]
])

raw_sonar_str = str(sonar_data)

# Instantly replace all negative numbers with 0 without a single loop!
sonar_data[sonar_data < 0] = 0

cleanup_txt.textContent = (
    f"\n------------------------------------------------\n\n"
    f"2. 2D Boolean Replacement (Signal Cleanup)\n"
    f"Raw Sonar Data:\n{raw_sonar_str}\n\n"
    f"Cleaned Sonar Data:\n{sonar_data}"
)
ba(cleanup_txt)

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

