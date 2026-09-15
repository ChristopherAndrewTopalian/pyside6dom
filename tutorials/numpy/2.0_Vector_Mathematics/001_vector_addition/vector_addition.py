# vector_addition.py

import numpy as np
from pyside6dom import *

init_window("Vector Addition", 600, 500)

# Basic Vector Addition (Combining Sensors)
addition_txt = ce('text')

# Imagine these are readings from two different sensor arrays
sensor_a = np.array([10, 20, 30])
sensor_b = np.array([1, 2, 3])

# NumPy instantly adds index 0 to index 0, index 1 to index 1, etc.
combined_sensors = sensor_a + sensor_b

addition_txt.textContent = f"1. Basic Vector Addition (Combining Sensors)\nSensor A:       {sensor_a}\nSensor B:       {sensor_b}\nCombined total: {combined_sensors}"
ba(addition_txt)

# Spatial Math (Drone Trajectory in 3D Space)
spatial_txt = ce('text')

# [X, Y, Z] coordinates
# X = East/West | Y = North/South | Z = Altitude
current_location = np.array([100, 50, 400])

# The drone moves 50 units East, 0 units North, and drops 20 units in Altitude
movement_vector = np.array([50, 0, -20])

# Calculate the exact new location in one seamless operation
new_location = current_location + movement_vector

spatial_txt.textContent = f"\n------------------------------------------------\n\n2. Spatial Math (Drone Trajectory in 3D Space)\nStarting Location [X, Y, Z]: {current_location}\nMovement Vector            : {movement_vector}\nNew Exact Location         : {new_location}"
ba(spatial_txt)

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

