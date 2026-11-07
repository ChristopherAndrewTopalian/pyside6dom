# matplotlib_telemetry.py

from pyside6dom import *
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Initialize our custom engine
init_window('Sensor Telemetry', 800, 600)

# Add a header using our engine's string element creator
header = ce('textarea')
header.value = " Warp Core Output Frequency"
header.style.fontSize = '30px'
header.style.fontWeight = 'bold'
header.style.color = 'rgb(0, 255, 255)'
header.style.padding = '10px'
ba(header)

# Setup Matplotlib's Dark Theme
plt.style.use('dark_background')

# Create the Matplotlib Figure (The math container)
fig = Figure(figsize=(7, 5), dpi=100)
fig.patch.set_facecolor('#1e1e1e') # Blends with standard dark themes

ax = fig.add_subplot(111)
ax.set_facecolor('#282828') # Inner plot background

# Define Data and Plot
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 22, 18]

# Starfleet tactical cyan
ax.plot(x, y, marker='o', linestyle='-', color='#00ffcc', linewidth=2, markersize=8)

ax.set_title("Energy Spike Analysis", color="white", pad=15)
ax.set_xlabel("Time (Seconds)", color="white")
ax.set_ylabel("Megajoules", color="white")

# Convert the Figure into a PySide6 Widget
canvas = FigureCanvas(fig)

# Append the Matplotlib Canvas directly using our custom DOM engine
ba(canvas)

# Start the event loop
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

