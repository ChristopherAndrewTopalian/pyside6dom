# pyside6dom_open_url.py

import webbrowser

from pyside6dom import *

set_theme("""
    body {
        background-color: rgb(30, 30, 30);
    }
    button {
        background-color: rgb(0, 0, 0);
        color: cyan;
        /* we write 1px before solid */
        border: 1px solid rgb(255, 255, 255);
        border-radius: 5px;
    }
    button:hover {
        background-color: #555;
        border-color: rgb(0, 255, 255);
    }
    input {
        border: 1px solid white;
    }
""")

####

def goTo_url(url):
    if url.startswith('http://') or url.startswith('https://'):
        try:
            webbrowser.open(url)
            print("Web page opened successfully.")
            print(url)
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Enter a URL starting with 'http://' or 'https://'")

####

init_window('Website Links', 700, 500)

theTitle = ce('text')
theTitle.textContent = 'Websites'
ba(theTitle)

web_btns_scroll_box = ce('scroll_div')
web_btns_scroll_box.style('border: 1px solid white;')
ba(web_btns_scroll_box)

google_btn = ce('button')
google_btn.textContent = 'Google'
google_btn.onclick = lambda: goTo_url('https://www.google.com')
ba(google_btn, web_btns_scroll_box)

vidmax_btn = ce('button')
vidmax_btn.textContent = 'Vid Max'
vidmax_btn.onclick = lambda: goTo_url('https://vidmax.com/')
ba(vidmax_btn, web_btns_scroll_box)

rumble_btn = ce('button')
rumble_btn.textContent = 'Rumble'
rumble_btn.onclick = lambda: goTo_url('https://rumble.com/')
ba(rumble_btn, web_btns_scroll_box)

kick_btn = ce('button')
kick_btn.textContent = 'Kick'
kick_btn.onclick = lambda: goTo_url('https://kick.com/')
ba(kick_btn, web_btns_scroll_box)

youtube_btn = ce('button')
youtube_btn.textContent = 'YouTube'
youtube_btn.onclick = lambda: goTo_url('https://youtube.com/')
ba(youtube_btn, web_btns_scroll_box)

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

