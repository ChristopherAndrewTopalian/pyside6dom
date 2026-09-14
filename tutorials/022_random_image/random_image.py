# random_image.py

import random
from pyside6dom import *

theImages = ['001.png', '002.png', '003.png']

# Initialize the Application
init_window("Showing an Image", 1100, 650)

theImage = ce('img')
theImage.src = random.choice(theImages)
theImage.width = 700
ba(theImage)

# Launch the App
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

