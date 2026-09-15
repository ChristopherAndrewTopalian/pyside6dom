# broadcasting_and_scaling.py

import numpy as np
from pyside6dom import *

init_window("Broadcasting and Scaling", 600, 600)

# Scaling a 1D Vector (Audio Amplification)
scaling_txt = ce('text')

# Imagine this is a tiny snippet of a digital audio wave
audio_wave = np.array([20, 40, 15, -10, 5])

# To double the volume, we multiply the entire array by a Scalar (2).
# NumPy 'broadcasts' the 2 to every single element instantly.
amplified_wave = audio_wave * 2

scaling_txt.textContent = f"1. Scaling a 1D Vector (Audio Amplification)\nOriginal Audio Wave : {audio_wave}\nAmplified Audio Wave: {amplified_wave}"
ba(scaling_txt)


# Broadcasting across a 2D Matrix (Sensor Calibration)
broadcasting_txt = ce('text')

# Imagine a 3x3 grid of thermal sensors on a rescue drone.
# The factory calibration is off by exactly 5 degrees.
sensor_grid = np.array([
    [70, 72, 71],
    [68, 69, 70],
    [73, 74, 75]
])

# Add 5 to every sensor simultaneously without writing a loop
calibrated_grid = sensor_grid + 5

broadcasting_txt.textContent = f"\n------------------------------------------------\n\n2. Broadcasting across a 2D Matrix (Sensor Calibration)\nOriginal Sensor Grid:\n{sensor_grid}\n\nCalibrated Sensor Grid (+5):\n{calibrated_grid}"
ba(broadcasting_txt)

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

