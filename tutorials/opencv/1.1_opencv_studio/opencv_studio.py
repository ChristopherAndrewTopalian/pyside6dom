# opencv_studio.py

import cv2
from pyside6dom import *

init_window("Tactical Python Vision Studio (DOM Engine)", 950, 600)

set_theme("""
    body { background-color: rgb(18, 18, 20); }
    button {
        background-color: rgb(32, 32, 36); 
        color: rgb(255, 255, 255); 
        border: 2px solid rgb(41, 41, 46); 
        border-radius: 6px; 
        padding: 12px; 
        font-weight: bold;
        text-align: left;
        margin-bottom: 5px;
    }
    button:hover { 
        background-color: rgb(0, 255, 204); 
        color: black; 
        border-color: rgb(0, 255, 204); 
    }
""")

# === 
#  STATE TRACKER & HARDWARE SETUP
# === 
state = {"mode": "normal"}
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# === 
# MAIN DOM LAYOUT
# === 
# The Main Wrapper (Flex Row)
main_layout = ce('div')
main_layout.style.display = 'flex'
main_layout.style.flexDirection = 'row'
ba(main_layout)

# LEFT PANEL: THE SCROLLABLE MENU
scroll_area = ce('scroll_div')
scroll_area.style.display = 'flex'
scroll_area.style.flexDirection = 'column'
scroll_area.style.width = '280px'
scroll_area.style.border = '1px solid rgb(41, 41, 46)'
ba(scroll_area, main_layout)

header_label = ce('text')
header_label.textContent = "🌌 VISION CONTROLS"
header_label.style.color = "rgb(0, 255, 204)"
header_label.style.fontWeight = "bold"
header_label.style.marginBottom = "15px"
ba(header_label, scroll_area)

# RIGHT PANEL: THE VIDEO VIEWPORT
viewport = ce('div')
viewport.style.display = 'flex'
viewport.style.flexDirection = 'column'
viewport.style.marginLeft = '15px'
ba(viewport, main_layout)

status_label = ce('text')
status_label.textContent = "STATUS: OPTICAL SENSOR ACTIVE [MODE: NORMAL RGB]"
status_label.style.color = "rgb(0, 255, 204)"
status_label.style.fontWeight = "bold"
ba(status_label, viewport)

# The Video Screen
video_screen = ce('text')
video_screen.textContent = "Connecting to optical sensor..."
video_screen.style.border = "2px solid rgb(0, 255, 204)"
video_screen.style.backgroundColor = "black"
video_screen.style.minWidth = "640px"
video_screen.style.minHeight = "480px"
video_screen.style.borderRadius = "6px"
ba(video_screen, viewport)

# === #
# FUNCTIONAL LOGIC & CALLBACKS
# === #
def set_filter_mode(mode):
    state["mode"] = mode
    status_label.textContent = f"STATUS: OPTICAL SENSOR ACTIVE [MODE: {mode.upper()}]"

def update_video_frame():
    success, frame = capture.read()
    if not success or frame is None:
        return

    current_mode = state["mode"]
    if current_mode == "grayscale":
        processed = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rendered_frame = cv2.cvtColor(processed, cv2.COLOR_GRAY2RGB)
    elif current_mode == "edges":
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        rendered_frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)
    else:
        rendered_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    height, width, channels = rendered_frame.shape
    bytes_per_line = channels * width
    qt_image = QImage(rendered_frame.data, width, height, bytes_per_line, QImage.Format_RGB888)

    # IMPORTANT: We use .raw to bypass the DOM and efficiently blast pixels directly to the hardware widget.
    video_screen.raw.setPixmap(QPixmap.fromImage(qt_image).scaled(
        video_screen.raw.width(), video_screen.raw.height(), Qt.KeepAspectRatio
    ))

# Using the Functional Closure Helper we just learned
def make_diagnostic_action(btn_num):
    def action():
        print(f"Executing Diagnostic Routine {btn_num}...")
    return action

# ===
# CONNECT MENU BUTTONS
# ===
btn_normal = ce('button')
btn_normal.textContent = "🎥 1. Normal RGB Feed"
btn_normal.onclick = lambda: set_filter_mode("normal")
ba(btn_normal, scroll_area)

btn_gray = ce('button')
btn_gray.textContent = "🌑 2. Grayscale (B&W)"
btn_gray.onclick = lambda: set_filter_mode("grayscale")
ba(btn_gray, scroll_area)

btn_edges = ce('button')
btn_edges.textContent = "⚡ 3. Canny Edge Radar"
btn_edges.onclick = lambda: set_filter_mode("edges")
ba(btn_edges, scroll_area)

for i in range(4, 21):
    btn_extra = ce('button')
    btn_extra.textContent = f"🔧 Diagnostic Loop {str(i).zfill(2)}"
    btn_extra.onclick = make_diagnostic_action(i)
    ba(btn_extra, scroll_area)

# ===
# HARDWARE LOOP & CLEANUP
# ===
timer = QTimer()
timer.timeout.connect(update_video_frame)
timer.start(30)

# Safely shut down the camera when the user closes the window
QApplication.instance().aboutToQuit.connect(capture.release)

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

