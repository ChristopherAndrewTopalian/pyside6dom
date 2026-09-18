# video_play_pause_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window("Video Player", 800, 600)

my_vid = ce("video")
my_vid.src = "our_test_video.mp4" # Can be local file or HTTP link
ba(my_vid)

play_btn = ce("button")
play_btn.textContent = "▶ Play"
play_btn.onclick = my_vid.play
ba(play_btn)

pause_btn = ce("button")
pause_btn.textContent = "⏸ Pause"
pause_btn.onclick = my_vid.pause
ba(pause_btn)

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

