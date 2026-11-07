# CODE BOOK

---

<details>
<summary><b>Section: 0.12_minimal_app_with_icon</b></summary>


### `minimal_app_with_icon.py`

```python
# minimal_app_with_icon.py

from pyside6dom import *

init_window('OurApp', 700, 600, '001.png')

run_app()

####

'''
We must run this from the folder
because it must reference the texture.
'''

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
```


</details>

---

<details>
<summary><b>Section: 0.1_minimal_app</b></summary>


### `minimal_app.py`

```python
# minimal_app.py

from pyside6dom import *

init_window('Our App', 700, 500)

run_app()

####

'''
Creates a Dark Theme Window of specified Width and Height
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.12_text_style_direct</b></summary>


### `text_div_style_direct.py`

```python
# text_div_style_direct.py

from pyside6dom import *

init_window('Our App', 700, 500)

howdy_txt = ce('div')
howdy_txt.textContent = 'Hi Everyone'
howdy_txt.style.fontFamily = 'Arial'
howdy_txt.style.fontWeight = 'bold'
howdy_txt.style.fontSize = '70px'
howdy_txt.style.color = 'rgb(0, 255, 255)'
ba(howdy_txt)

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
```

### `text_style_direct.py`

```python
# text_style_direct.py

from pyside6dom import *

init_window('Our App', 700, 500)

howdy_txt = ce('text')
howdy_txt.textContent = 'Hi Everyone'
howdy_txt.style.fontFamily = 'Arial'
howdy_txt.style.fontWeight = 'bold'
howdy_txt.style.fontSize = '70px'
howdy_txt.style.color = 'rgb(0, 255, 255)'
ba(howdy_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.13_text_style_css_selector</b></summary>


### `text_div_style_css_selector.py`

```python
# text_div_style_css_selector.py

from pyside6dom import *

init_window('Our App', 700, 500)

set_theme("""
    #howdy_txt {
        font-family: Arial;
        font-weight: bold;
        font-size: 70px;
        color: rgb(0, 255, 255);
    }
""")

howdy_txt = ce('div')
howdy_txt.id = 'howdy_txt'
howdy_txt.textContent = 'Hi Everyone'
ba(howdy_txt)

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
```

### `text_style_css_selector.py`

```python
# text_style_css_selector.py

from pyside6dom import *

init_window('Our App', 700, 500)

set_theme("""
    #howdy_txt {
        font-family: Arial;
        font-weight: bold;
        font-size: 70px;
        color: rgb(0, 255, 255);
    }
""")

howdy_txt = ce('text')
howdy_txt.id = 'howdy_txt'
howdy_txt.textContent = 'Hi Everyone'
ba(howdy_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.14_text_style_css_className</b></summary>


### `text_div_style_css_className.py`

```python
# text_div_style_css_className.py

from pyside6dom import *

set_theme("""
    .aqua_bold_text{
        font-family: Arial;
        font-weight: bold;
        font-size: 70px;
        color: rgb(0, 255, 255);
    }
""")

init_window('Our App', 700, 500)

howdy_txt = ce('div')
howdy_txt.className = 'aqua_bold_text'
howdy_txt.textContent = 'Hi Everyone'
ba(howdy_txt)

message_txt = ce('div')
message_txt.className = 'aqua_bold_text'
message_txt.textContent = 'Happy Scripting'
ba(message_txt)

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
```

### `text_style_css_className.py`

```python
# text_style_css_className.py

from pyside6dom import *

set_theme("""
    .aqua_bold_text {
        font-family: Arial;
        font-weight: bold;
        font-size: 70px;
        color: rgb(0, 255, 255);
    }
""")

init_window('Our App', 700, 500)

howdy_txt = ce('text')
howdy_txt.className = 'aqua_bold_text'
howdy_txt.textContent = 'Hi Everyone'
ba(howdy_txt)

message_txt = ce('text')
message_txt.className = 'aqua_bold_text'
message_txt.textContent = 'Happy Scripting'
ba(message_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.1_text</b></summary>


### `text.py`

```python
# text.py

from pyside6dom import *

init_window('Our App', 700, 500)

howdy_txt = ce('text')
howdy_txt.textContent = 'Hi Everyone'
ba(howdy_txt)

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
```

### `text_div.py`

```python
# text_div.py

from pyside6dom import *

init_window('Our App', 700, 500)

howdy_txt = ce('div')
howdy_txt.textContent = 'Hi Everyone'
ba(howdy_txt)

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
```


</details>

---

<details>
<summary><b>Section: 2.1_button</b></summary>


### `button.py`

```python
# button.py

from pyside6dom import *

init_window('Our App', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Hi Everyone'
def greetings(message):
    print(message)
howdy_btn.onclick = lambda: greetings('hi')
ba(howdy_btn)

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
```


</details>

---

<details>
<summary><b>Section: 2.2_button_date_time_print</b></summary>


### `button_date_time_print.py`

```python
# button_date_time_print.py

from pyside6dom import *
import datetime as dt

def get_date_time_12():
    currentDateTime = dt.datetime.now()
    # formatted date MM-DD-YY
    date = currentDateTime.strftime("%m-%d-%y")
    # formatted time HH:MM AM/PM
    time = currentDateTime.strftime("%I:%M %p")
    formattedDateTime = date + " " + time
    return formattedDateTime

####

init_window('Our App', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Date/Time'
howdy_btn.onclick = lambda: print(get_date_time_12())
ba(howdy_btn)

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
```


</details>

---

<details>
<summary><b>Section: 2.3_button_date_time_show</b></summary>


### `button_date_time_show.py`

```python
# button_date_time_show.py

from pyside6dom import *
import datetime as dt

def get_date_time_12():
    currentDateTime = dt.datetime.now()
    date = currentDateTime.strftime("%m-%d-%y")
    time = currentDateTime.strftime("%I:%M %p")
    return date + " " + time

init_window('Our App', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Date/Time'
def update_time_label():
    ge('output_txt').textContent = get_date_time_12()
howdy_btn.onclick = update_time_label 
ba(howdy_btn)

output_txt = ce('text')
output_txt.id = 'output_txt'
output_txt.style.fontSize = '30px'
output_txt.style.fontWeight = 'bold'
ba(output_txt)

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
```


</details>

---

<details>
<summary><b>Section: 3.1_input_name</b></summary>


### `input.py`

```python
# input.py

from pyside6dom import *

init_window('Our App', 700, 500)

name_input = ce('input')
name_input.placeholder = 'Enter First Name: '
ba(name_input)

confirm_btn = ce('button')
confirm_btn.textContent = 'Enter'
confirm_btn.onclick = lambda: print(name_input.value)
ba(confirm_btn)

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
```


</details>

---

<details>
<summary><b>Section: 4.1_div</b></summary>


### `div.py`

```python
# div.py

from pyside6dom import *

init_window('Our App', 700, 500)

message_container = ce('div')
message_container.style('border: 1px solid rgb(255, 255, 255); border-radius: 8px;')
ba(message_container)

hi_txt = ce('text')
hi_txt.textContent = 'Hi Everyone'
message_container.append(hi_txt)

howdy_txt = ce('text')
howdy_txt.textContent = 'Howdy'
message_container.append(howdy_txt)

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
```

### `div_textContent.py`

```python
# div_textContent.py

from pyside6dom import *

init_window('Our App', 700, 500)

message_container = ce('div')
message_container.style('border: 1px solid rgb(255, 255, 255); border-radius: 8px;')
ba(message_container)

hi_txt = ce('div')
hi_txt.textContent = 'Hi Everyone'
message_container.append(hi_txt)

howdy_txt = ce('div')
howdy_txt.textContent = 'Howdy'
message_container.append(howdy_txt)

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
```


</details>

---

<details>
<summary><b>Section: ba_way</b></summary>


### `div.py`

```python
# div.py

from pyside6dom import *

init_window('Our App', 700, 500)

message_container = ce('div')
message_container.style('border: 1px solid rgb(255, 255, 255); border-radius: 8px;')
ba(message_container)

hi_txt = ce('text')
hi_txt.textContent = 'Hi Everyone'
ba(hi_txt, message_container)

howdy_txt = ce('text')
howdy_txt.textContent = 'Howdy'
ba(howdy_txt, message_container)

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
```


</details>

---

<details>
<summary><b>Section: 5.1_scroll_div</b></summary>


### `scroll_div_row.py`

```python
# scroll_div_row.py

from pyside6dom import *

init_window('Scroll Div Row', 700, 600)

top_container = ce('scroll_div')
top_container.style.display = 'flex'
top_container.style.flexDirection = 'row'
top_container.style.height = '70px' 
ba(top_container)

btn1 = ce('button')
btn1.textContent = 'btn1'
btn1.onclick = lambda: print('btn1')
top_container.append(btn1)

btn2 = ce('button')
btn2.textContent = 'btn2'
btn2.onclick = lambda: print('btn2')
top_container.append(btn2)

btn3 = ce('button')
btn3.textContent = 'btn3'
btn3.onclick = lambda: print('btn3')
top_container.append(btn3)

btn4 = ce('button')
btn4.textContent = 'btn4'
btn4.onclick = lambda: print('btn4')
top_container.append(btn4)

btn5 = ce('button')
btn5.textContent = 'btn5'
btn5.onclick = lambda: print('btn5')
top_container.append(btn5)

btn6 = ce('button')
btn6.textContent = 'btn6'
btn6.onclick = lambda: print('btn6')
top_container.append(btn6)

btn7 = ce('button')
btn7.textContent = 'btn7'
btn7.onclick = lambda: print('btn7')
top_container.append(btn7)

btn8 = ce('button')
btn8.textContent = 'btn8'
btn8.onclick = lambda: print('btn8')
top_container.append(btn8)

btn9 = ce('button')
btn9.textContent = 'btn9'
btn9.onclick = lambda: print('btn9')
top_container.append(btn9)

btn10 = ce('button')
btn10.textContent = 'btn10'
btn10.onclick = lambda: print('btn10')
top_container.append(btn10)

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
```


</details>

---

<details>
<summary><b>Section: ba_way</b></summary>


### `scroll_div_row.py`

```python
# scroll_div_row.py

from pyside6dom import *

init_window('OurApp', 700, 600)

top_container = ce('scroll_div')
top_container.style.display = 'flex'
top_container.style.flexDirection = 'row'
top_container.style.height = '70px' 
ba(top_container)

btn1 = ce('button')
btn1.textContent = 'btn1'
btn1.onclick = lambda: print('btn1')
ba(btn1, top_container)

btn2 = ce('button')
btn2.textContent = 'btn2'
btn2.onclick = lambda: print('btn2')
ba(btn2, top_container)

btn3 = ce('button')
btn3.textContent = 'btn3'
btn3.onclick = lambda: print('btn3')
ba(btn3, top_container)

btn4 = ce('button')
btn4.textContent = 'btn4'
btn4.onclick = lambda: print('btn4')
ba(btn4, top_container)

btn5 = ce('button')
btn5.textContent = 'btn5'
btn5.onclick = lambda: print('btn5')
ba(btn5, top_container)

btn6 = ce('button')
btn6.textContent = 'btn6'
btn6.onclick = lambda: print('btn6')
ba(btn6, top_container)

btn7 = ce('button')
btn7.textContent = 'btn7'
btn7.onclick = lambda: print('btn7')
ba(btn7, top_container)

btn8 = ce('button')
btn8.textContent = 'btn8'
btn8.onclick = lambda: print('btn8')
ba(btn8, top_container)

btn9 = ce('button')
btn9.textContent = 'btn9'
btn9.onclick = lambda: print('btn9')
ba(btn9, top_container)

btn10 = ce('button')
btn10.textContent = 'btn10'
btn10.onclick = lambda: print('btn10')
ba(btn10, top_container)

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
```


</details>

---

<details>
<summary><b>Section: 5.2_scroll_div_row_lod</b></summary>


### `scroll_div_row_lod.py`

```python
# scroll_div_row_lod.py

from pyside6dom import *

people = [
    {"name": "Jane", "score": 96},
    {"name": "Joan", "score": 90},
    {"name": "Melissa", "score": 92},
    {"name": "Tabitha", "score": 90},
    {"name": "Jess", "score": 87},
    {"name": "Katie", "score": 98},
    {"name": "Nicky", "score": 80},
    {"name": "Samantha", "score": 97},
    {"name": "Brie", "score": 90},
]

init_window('OurApp', 700, 600)

set_theme("""
    body { background-color: rgb(25, 25, 25); }
    button {
        padding: 8px 15px;
        font-weight: bold;
        background-color: rgb(45, 45, 55);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 5px;
        margin: 5px;
    }
    button:hover{
        border-color: rgb(255, 255, 255);
    }
""")

top_container = ce('scroll_div')
top_container.style.display = 'flex'
top_container.style.flexDirection = 'row'
top_container.style.alignItems = 'flex-start'
# 85px to leave room for the scrollbar
top_container.style.height = '85px' 
ba(top_container)

for person in people:
    the_btn = ce('button')
    the_btn.textContent = person["name"]
    # p=person locks the current object into the lambda's memory
    the_btn.onclick = lambda p=person: print(f"{p['name']} scored: {p['score']}")
    #the_btn.onclick = lambda p=person: print(p['name'] + " scored: " + str(p['score']))
    top_container.append(the_btn)

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
```


</details>

---

<details>
<summary><b>Section: ba_way</b></summary>


### `scroll_div_row_lod.py`

```python
# scroll_div_row_lod.py

from pyside6dom import *

people = [
    {"name": "Jane", "score": 96},
    {"name": "Joan", "score": 90},
    {"name": "Melissa", "score": 92},
    {"name": "Tabitha", "score": 90},
    {"name": "Jess", "score": 87},
    {"name": "Katie", "score": 98},
    {"name": "Nicky", "score": 80},
    {"name": "Samantha", "score": 97},
    {"name": "Brie", "score": 90},
]

init_window('OurApp', 700, 600)

set_theme("""
    body { background-color: rgb(25, 25, 25); }
    button {
        padding: 8px 15px;
        font-weight: bold;
        background-color: rgb(45, 45, 55);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 5px;
        margin: 5px;
    }
    button:hover{
        border-color: rgb(255, 255, 255);
    }
""")

top_container = ce('scroll_div')
top_container.style.display = 'flex'
top_container.style.flexDirection = 'row'
top_container.style.alignItems = 'flex-start'
# 85px to leave room for the scrollbar
top_container.style.height = '85px' 
ba(top_container)

for person in people:
    the_btn = ce('button')
    the_btn.textContent = person["name"]
    # p=person locks the current object into the lambda's memory
    the_btn.onclick = lambda p=person: print(f"{p['name']} scored: {p['score']}")
    #the_btn.onclick = lambda p=person: print(p['name'] + " scored: " + str(p['score']))
    ba(the_btn, top_container)

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
```


</details>

---

<details>
<summary><b>Section: 6.1_list_show</b></summary>


### `list_show_all.py`

```python
# list_show_all.py

from pyside6dom import *

init_window('List Show All', 700, 500)

people = [
    'Jane',
    'Joan',
    'Melissa',
    'Tabitha'
]

people_div = ce('div')
people_div.textContent = people
people_div.style.fontSize = '30px'
people_div.style.fontWeight = 'bold'
ba(people_div)

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
```


</details>

---

<details>
<summary><b>Section: 6.2_list_make_buttons</b></summary>


### `list_make_buttons.py`

```python
# list_make_buttons.py

from pyside6dom import *

init_window('List Show All', 700, 500)

people = [
    'Jane',
    'Joan',
    'Melissa',
    'Tabitha'
]

name_container = ce('scroll_div')
name_container.style.height = '200px'
ba(name_container)

for person in people:
    people_div = ce('button')
    people_div.textContent = person
    people_div.style.fontSize = '30px'
    people_div.style.fontWeight = 'bold'
    people_div.onclick = lambda p=person: print(p)
    name_container.append(people_div)

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
```


</details>

---

<details>
<summary><b>Section: pyside6dom</b></summary>


### `__init__.py`

```python
# pyside6dom.py

import os
import sys
import re
import json      # For saving/loading data (like localStorage)
import math      # For advanced kinematics and geometry
import random    # For games and generative art
import subprocess
from pathlib import Path

from datetime import datetime

from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFrame, QBoxLayout, QVBoxLayout, QHBoxLayout, 
    QGridLayout, QPushButton, QLineEdit, QLabel, QSlider, QScrollArea, 
    QCheckBox, QComboBox, QSizePolicy, QPlainTextEdit, QTextBrowser
)
from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QImage, QPixmap, QIcon, QDesktopServices
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput, QSoundEffect
from PySide6.QtMultimediaWidgets import QVideoWidget

def show_commands():
    """Returns and prints a helpful list of all available DOM engine commands."""
    lines = []
    lines.append("="*45)
    lines.append(" PYSIDE6DOM ENGINE - AVAILABLE COMMANDS")
    lines.append("="*45 + "\n")
    
    for name, obj in globals().items():
        if callable(obj) and getattr(obj, '__module__', '') == __name__ and not name.startswith('_'):
            description = obj.__doc__ if obj.__doc__ else "No description provided."
            lines.append(f" > {name}()")
            lines.append(f"   {description.strip()}\n")
            
    lines.append("="*45)
    final_text = "\n".join(lines)
    print(final_text)
    return final_text

# ========================================== #
#               LOGIC GATES
# ========================================== #

def TAU(a, b):
    if (a == 0 and b == 0) or (a == 0 and b == 1) or (a == 1 and b == 0) or (a == 1 and b == 1):
        return 1
    return 1

def CON(a, b):
    if (a == 0 and b == 0) or (a == 0 and b == 1) or (a == 1 and b == 0) or (a == 1 and b == 1):
        return 0
    return 0

def XOR(a, b):
    if (a == 1 and b == 0) or (a == 0 and b == 1):
        return 1
    return 0

def XNOR(a, b):
    if (a == 0 and b == 0) or (a == 1 and b == 1):
        return 1
    return 0

def AND(a, b):
    if a == 1 and b == 1:
        return 1
    return 0

def NAND(a, b):
    if a == 0 or b == 0:
        return 1
    return 0

def OR(a, b):
    if a == 1 or b == 1:
        return 1
    return 0

def NOR(a, b):
    if a == 0 and b == 0:
        return 1
    return 0

def MI(a, b):
    if a == 0 or b == 1:
        return 1
    return 0

def MNI(a, b):
    if a == 1 and b == 0:
        return 1
    return 0

def CI(a, b):
    if a == 1 or b == 0:
        return 1
    return 0

def CNI(a, b):
    if a == 0 and b == 1:
        return 1
    return 0

def LP(a, b):
    if a == 1:
        return 1
    return 0

def LC(a, b):
    if a == 0:
        return 1
    return 0

def RP(a, b):
    if (a == 0 and b == 1) or (a == 1 and b == 1):
        return 1
    return 0

def RC(a, b):
    if (a == 0 and b == 0) or (a == 1 and b == 0):
        return 1
    return 0

# ===
#  DATE & TIME HELPERS
# ===

class dom:
    '''Namespace class for this engine's utility functions'''

    @staticmethod
    def get_year():
        """Returns the current 4-digit year (e.g., 2026)."""
        return datetime.today().year

    @staticmethod
    def get_month():
        """Returns the current month number (1-12)."""
        return datetime.today().month

    @staticmethod
    def get_day_of_month():
        """Returns the day of the month (1-31)."""
        return datetime.today().day

    @staticmethod
    def get_day_name():
        """Returns the full name of the day (e.g., 'Monday', 'Tuesday')."""
        return datetime.today().strftime("%A")

    @staticmethod
    def get_day_of_week():
        """Returns the day of the week as an integer (0-6).
        Matches JS DOM getDay(): 0=Sunday ... 6=Saturday."""
        return int(datetime.today().strftime('%w'))

    @staticmethod
    def get_day_of_week_iso():
        """Returns the day of the week as an integer (1-7).
        Matches ISO standard: 1=Monday ... 7=Sunday."""
        return datetime.today().isoweekday()

    @staticmethod
    def get_month_day_year():
        """Returns today's date formatted as MM-DD-YYYY."""
        return datetime.today().strftime("%m-%d-%Y")

    @staticmethod
    def get_year_month_day():
        """Returns today's date formatted as YYYY-MM-DD."""
        return datetime.today().strftime("%Y-%m-%d")

    # TIME FUNCTIONS

    @staticmethod
    def get_hours():
        """Returns the current hour in 24-hour format (0-23)."""
        return datetime.now().hour

    @staticmethod
    def get_minutes():
        """Returns the current minute (0-59)."""
        return datetime.now().minute

    @staticmethod
    def get_seconds():
        """Returns the current second (0-59)."""
        return datetime.now().second

    # UTILITY

    @staticmethod
    def is_target_date(target_string):
        ''' Compare today yy-mm-dd with target_string'''
        # Get today's date object and instantly convert it to a string
        today_str = str(datetime.today().strftime("%Y-%m-%d"))
        
        # Now we can safely compare text to text
        if today_str == target_string:
            return True
        else:
            return False

    # ===
    # FILE
    # ===

    @staticmethod
    def open_file(whichFilePath):
        '''Open the specified File'''
        if os.path.exists(whichFilePath):
            if sys.platform == 'win32':
                os.startfile(whichFilePath)
            elif sys.platform == 'darwin':
                subprocess.call(('open', whichFilePath))
            else:
                subprocess.call(('xdg-open', whichFilePath))
        else:
            print('File not found:', whichFilePath)

    @staticmethod
    def show_in_file_explorer(path):
        """Reveal a file, highlighted, in the OS file manager."""
        path = str(Path(path).resolve())

        if sys.platform == 'win32':
            subprocess.Popen(f'explorer /select,"{path}"')
        elif sys.platform == 'darwin':
            subprocess.Popen(['open', '-R', path])
        else:
            # Most Linux file managers don't support "select this file" —
            # opening the containing folder is the reliable fallback
            subprocess.Popen(['xdg-open', str(Path(path).parent)])

####

# ========================================== #
#               CONSOLE ALIAS
# ========================================== #
def cl(*args):
    print(*args)

class console:
    log = cl

# ========================================== #
#             UI AUDIO MANAGER
# ========================================== #
_ui_audio_cache = {}

def play_sound(file_path):
    """Plays a local .wav file instantly for UI feedback."""
    if not os.path.exists(file_path):
        cl(f"[Audio Missing] Pretend you heard: {file_path}")
        return

    if file_path not in _ui_audio_cache:
        sfx = QSoundEffect()
        sfx.setSource(QUrl.fromLocalFile(os.path.abspath(file_path)))
        sfx.setVolume(0.5) 
        _ui_audio_cache[file_path] = sfx
        
    _ui_audio_cache[file_path].play()

# ========================================== #
#             TIMER MANAGEMENT
# ========================================== #
_timers = {}
_timer_counter = 0

def set_interval(callback_func, ms):
    global _timer_counter
    _timer_counter += 1
    timer_id = f"timer_{_timer_counter}"
    
    t = QTimer()
    t.timeout.connect(callback_func)
    t.start(ms)
    
    _timers[timer_id] = t
    return timer_id

def clear_interval(timer_id):
    if timer_id in _timers:
        _timers[timer_id].stop()
        del _timers[timer_id]

setInterval = set_interval
clearInterval = clear_interval

# ========================================== #
#            WORLDWIDE REGISTRY
# ========================================== #
_dom_registry = {}
_app_instance = None
_root_window = None
_main_container = None
_pending_theme = None

####

# ========================================== #
#            RESPONSIVE LAYOUT ENGINE
# ========================================== #
_responsive_registry = set()

def _trigger_layout_update(elem=None):
    """Forces a math recalculation for percentages and absolute right/bottom positions."""
    targets = [elem] if elem else _responsive_registry
    
    for e in targets:
        if not e or not e.raw: continue
        
        parent_w = e.raw.parentWidget()
        if not parent_w: continue 
            
        # NEW: The Phantom Scrollbar Fix!
        # Jump up TWO levels to the actual QScrollArea widget. 
        # This completely ignores temporary scrollbars when measuring!
        if parent_w.parentWidget() and parent_w.parentWidget().objectName() == "qt_scrollarea_viewport":
            parent_w = parent_w.parentWidget().parentWidget()
            
        pw = parent_w.width()
        ph = parent_w.height()
        
        # Percentage Dimensions
        w_val = str(getattr(e.style, 'width', ''))
        if '%' in w_val:
            pct = float(w_val.replace('%', '')) / 100.0
            e.raw.setFixedWidth(int(pw * pct))
            
        h_val = str(getattr(e.style, 'height', ''))
        if '%' in h_val:
            pct = float(h_val.replace('%', '')) / 100.0
            e.raw.setFixedHeight(int(ph * pct))
            
        # Absolute Right/Bottom Positioning
        if getattr(e.style, 'position', '') == 'absolute':
            e.raw.adjustSize() 
            cw = e.raw.width()
            ch = e.raw.height()
            
            x, y = e.raw.x(), e.raw.y()
            
            right_val = getattr(e.style, 'right', None)
            if right_val is not None:
                x = pw - cw - int(float(str(right_val).replace('px', '')))
                
            bottom_val = getattr(e.style, 'bottom', None)
            if bottom_val is not None:
                y = ph - ch - int(float(str(bottom_val).replace('px', '')))
                
            e.raw.move(x, y)

####

# ========================================== #
#            DOM STYLE ENGINE
# ========================================== #
class DOMStyle:
    def __init__(self, element):
        object.__setattr__(self, '_element', element)
        object.__setattr__(self, '_styles', {})

    def __setattr__(self, key, value):
        # ABSOLUTE POSITIONING
        if key == 'position':
            self.__dict__['position'] = value
            return 

        if key in ('width', 'height'):
            val_str = str(value).strip()

            # The Percentage Interceptor
            if '%' in val_str:
                self.__dict__[key] = val_str
                _responsive_registry.add(self._element)
                _trigger_layout_update(self._element)
                return

            val_str = val_str.replace('px', '')
            try:
                num = int(float(val_str))
                self.__dict__[key] = num
                if key == 'width': self._element.raw.setFixedWidth(num)
                elif key == 'height': self._element.raw.setFixedHeight(num)
                return
            except ValueError:
                pass

        if key in ('left', 'top', 'right', 'bottom'):
            self.__dict__[key] = value 

            # If using right/bottom, track it for window resizes!
            if key in ('right', 'bottom'):
                _responsive_registry.add(self._element)
            
            # Allow instant movement if the element is already parented
            if key in ('left', 'top'):
                val_str = str(value).replace('px', '').strip()
                try:
                    num = int(float(val_str))
                    if key == 'left': self._element.raw.move(num, self._element.raw.y())
                    elif key == 'top': self._element.raw.move(self._element.raw.x(), num)
                except ValueError:
                    pass
                    
            _trigger_layout_update(self._element)

        # OVERFLOW SUPPORT
        if key == 'overflow':
            self.__dict__[key] = value
            # If the element is a scroll_div, translate 'hidden' to Qt's scrollbar policies
            if hasattr(self._element.raw, 'setHorizontalScrollBarPolicy'):
                if value == 'hidden':
                    self._element.raw.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                    self._element.raw.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                elif value in ('auto', 'scroll'):
                    self._element.raw.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
                    self._element.raw.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
            return

        # CSS GRID ENGINE
        if key == 'display' and value == 'grid':
            if hasattr(self._element, 'layout') and self._element.layout is not None:
                QWidget().setLayout(self._element.layout) 
            
            grid = QGridLayout(self._element.raw)
            self._element.layout = grid
            
            self._element.layout._auto_row = 0
            self._element.layout._auto_col = 0
            self._element.layout._max_cols = 3 
            return
            
        if key == 'gridTemplateColumns':
            self.__dict__[key] = value
            if hasattr(self._element, 'layout') and isinstance(self._element.layout, QGridLayout):
                cols = len(str(value).split())
                match = re.search(r'repeat\((\d+)', str(value))
                if match: cols = int(match.group(1))
                self._element.layout._max_cols = max(1, cols)
            return

        if key in ('gridRow', 'gridColumn'):
            self.__dict__[key] = value
            return

        # FLEXBOX LAYOUT ENGINE
        if key == 'display' and value == 'flex':
            return 

        if key == 'flexDirection':
            if hasattr(self._element, 'layout') and isinstance(self._element.layout, QBoxLayout):
                if value == 'row':
                    self._element.layout.setDirection(QBoxLayout.Direction.LeftToRight)
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                elif value == 'column':
                    self._element.layout.setDirection(QBoxLayout.Direction.TopToBottom)
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
            return

        if key == 'alignItems':
            if hasattr(self._element, 'layout') and isinstance(self._element.layout, QBoxLayout):
                if value in ('flex-start', 'start'):
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
                elif value == 'center':
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignTop)
                elif value in ('flex-end', 'end'):
                    self._element.layout.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)
                elif value == 'stretch':
                    self._element.layout.setAlignment(Qt.AlignmentFlag(0)) 
            return

        # ===
        # Flex Layout Spacing Translators
        # ===
                
        if key == 'gap':
            # Translate gap to C++ setSpacing
            if hasattr(self._element, 'layout') and self._element.layout:
                try:
                    val = int(str(value).replace('px', '').strip())
                    self._element.layout.setSpacing(val)
                except: pass
            return # Qt CSS doesn't understand 'gap', so we safely exit here.
        # ===

        # ===
        # INLINE TEXT DECORATION 
        # Bypasses the CSS Engine to prevent QLabel warnings!
        # ===
        if key == 'textDecoration':
            font = self._element.raw.font()
            if value == 'underline':
                font.setUnderline(True)
            elif value == 'line-through':
                font.setStrikeOut(True)
            elif value in ('none', ''):
                font.setUnderline(False)
                font.setStrikeOut(False)
            
            self._element.raw.setFont(font)
            return # Exit instantly so it doesn't hit the CSS compiler

        # INLINE TEXT ALIGNMENT
        if key == 'textAlign':
            # Hijack the key so the compiler below automatically turns it into 'qproperty-alignment'
            key = 'qpropertyAlignment' 
            
            if value == 'center': value = 'AlignCenter'
            elif value == 'right': value = 'AlignRight'
            elif value == 'left': value = 'AlignLeft'

        # CSS COMPILER
        css_property = ''.join(['-' + c.lower() if c.isupper() else c for c in key])
        self._styles[css_property] = value
        
        css_string = ""
        for prop, val in self._styles.items():
            css_string += f"{prop}: {val}; "
            
        # Route it through your master compiler
        self._element.set_style(css_string)

    def __call__(self, css_string):
        self._element.set_style(css_string)

# ========================================== #
#           DOM ELEMENT WRAPPER
# ========================================== #
class DOMElement:
    def __init__(self, tag, qt_widget):
        self.tag = tag
        self.raw = qt_widget
        self._id = ""
        self._children = []
        self._dom_style = DOMStyle(self)

    @property
    def style(self): return self._dom_style

    @property
    def id(self): return self._id

    @id.setter
    def id(self, value):
        self._id = value
        _dom_registry[value] = self
        self.raw.setObjectName(str(value)) # Enables #id CSS styling
        
        # Force Qt to instantly refresh the CSS paint job when an ID is added!
        self.raw.style().unpolish(self.raw)
        self.raw.style().polish(self.raw)
        self.raw.update()

    # CLASS NAME SUPPORT
    @property
    def className(self): 
        return self.raw.property("class") or ""

    @className.setter
    def className(self, value):
        self.raw.setProperty("class", str(value))
        # Force Qt to instantly refresh the CSS paint job!
        self.raw.style().unpolish(self.raw)
        self.raw.style().polish(self.raw)
        self.raw.update()

    # ========================================== #
    # HTML DOM Standard: Title (Tooltip)
    # ========================================== #
    @property
    def title(self): 
        return getattr(self, "_title", "")

    @title.setter
    def title(self, text):
        self._title = str(text)
        self._update_tooltip()

    @property
    def titleFontSize(self): 
        return getattr(self, "_title_font_size", "14px") # Default is larger than HTML!

    @titleFontSize.setter
    def titleFontSize(self, size):
        # Safely handle if a user types 18 or "18px"
        val = str(size)
        if val.isdigit(): val += "px"
        
        self._title_font_size = val
        self._update_tooltip()
        
    def _update_tooltip(self):
        """Secretly wraps the tooltip in HTML so Qt renders it with a custom font size."""
        if not getattr(self, "_title", ""):
            self.raw.setToolTip("")
            return
            
        size = self.titleFontSize
        text = self._title
        
        # Qt natively parses this inline HTML!
        rich_tooltip = f'<span style="font-size: {size};">{text}</span>'
        self.raw.setToolTip(rich_tooltip)

    def append(self, child_element):
        """
        Mimics JavaScript's element.append(child)
        Because 'self' is the parent, we just pass both to your existing 'ba' function!
        """
        ba(child_element, self)

    def remove(self):
        """
        Mimics JavaScript's element.remove()
        Safely deletes the widget from the screen and clears it from memory.
        """
        self.raw.setParent(None)
        self.raw.deleteLater()

    @property
    def textContent(self):
        if hasattr(self.raw, "text"): return self.raw.text()
        return ""

    @textContent.setter
    def textContent(self, value):
        if hasattr(self.raw, "setText"): 
            self.raw.setText(str(value))
            
        elif self.tag in ("div", "scroll_div", "row_div"):
            # If the secret text node doesn't exist yet, create it!
            if not hasattr(self, "_secret_text_node"):
                self._secret_text_node = ce('text')
                # Force it to be perfectly transparent so it blends into the div
                self._secret_text_node.raw.setStyleSheet("background: transparent; border: none; margin: 0px; padding: 0px;")
                self.append(self._secret_text_node)
            
            # Update the existing secret text node
            self._secret_text_node.textContent = str(value)

    @property
    def innerHTML(self):
        if hasattr(self.raw, "text"): return self.raw.text()
        return ""

    @innerHTML.setter
    def innerHTML(self, value):
        if hasattr(self.raw, "setText"):
            if isinstance(self.raw, (QLabel, QTextBrowser)):
                if isinstance(self.raw, QLabel):
                    self.raw.setTextFormat(Qt.TextFormat.RichText)
                html_str = str(value)
                if "<table" in html_str and "<style>" not in html_str:
                    default_table_css = """
                    <style>
                        table { border-collapse: collapse; margin-top: 10px; }
                        th, td { padding: 6px 12px; border: 1px solid #777; }
                        th { background-color: #333333; color: #00ffcc; font-weight: bold; }
                    </style>
                    """
                    html_str = default_table_css + html_str
                self.raw.setText(html_str)
            else:
                self.raw.setText(str(value))
                
        elif self.tag in ("div", "scroll_div", "row_div"):
            # Same safety check for innerHTML!
            if not hasattr(self, "_secret_text_node"):
                self._secret_text_node = ce('text')
                self._secret_text_node.raw.setStyleSheet("background: transparent; border: none; margin: 0px; padding: 0px;")
                self.append(self._secret_text_node)
                
            self._secret_text_node.innerHTML = str(value)

    @property
    def value(self):
        if isinstance(self.raw, QLineEdit): return self.raw.text()
        elif isinstance(self.raw, QPlainTextEdit): return self.raw.toPlainText() 
        elif isinstance(self.raw, QSlider): return self.raw.value() / 10.0
        elif isinstance(self.raw, QComboBox): return self.raw.currentText()
        return None

    @value.setter
    def value(self, val):
        if isinstance(self.raw, QLineEdit): self.raw.setText(str(val))
        elif isinstance(self.raw, QPlainTextEdit): self.raw.setPlainText(str(val))
        elif isinstance(self.raw, QSlider): self.raw.setValue(int(float(val) * 10))
        elif isinstance(self.raw, QComboBox): self.raw.setCurrentText(str(val))

    @property
    def src(self): return self._src if hasattr(self, "_src") else ""

    @src.setter
    def src(self, file_path):
        self._src = file_path
        if isinstance(self.raw, QLabel) and self.tag == "img":
            self.raw.setPixmap(QPixmap(str(file_path)))
        elif self.tag == "video" and hasattr(self, "player"):
            if str(file_path).startswith("http"):
                self.player.setSource(QUrl(file_path))
            else:
                self.player.setSource(QUrl.fromLocalFile(os.path.abspath(file_path)))

    @property
    def width(self): return self.raw.width()

    @width.setter
    def width(self, val):
        val = int(val)
        self.raw.setFixedWidth(val)
        if self.tag == "img" and self.raw.pixmap():
            orig_w = self.raw.pixmap().width()
            orig_h = self.raw.pixmap().height()
            if orig_w > 0: self.raw.setFixedHeight(int(val * (orig_h / orig_w)))

    @property
    def height(self): return self.raw.height()

    @height.setter
    def height(self, val):
        val = int(val)
        self.raw.setFixedHeight(val)
        if self.tag == "img" and self.raw.pixmap():
            orig_w = self.raw.pixmap().width()
            orig_h = self.raw.pixmap().height()
            if orig_h > 0: self.raw.setFixedWidth(int(val * (orig_w / orig_h)))

    @property
    def placeholder(self):
        return self.raw.placeholderText() if hasattr(self.raw, "placeholderText") else ""

    @placeholder.setter
    def placeholder(self, text):
        if hasattr(self.raw, "setPlaceholderText"): self.raw.setPlaceholderText(str(text))

    # ===
    # HTML DOM Standard: Anchor Tags
    # ===
    @property
    def href(self): return getattr(self, "_href", "")

    @href.setter
    def href(self, url):
        self._href = url
        # The Magic: Override the mouse click to open the computer's real web browser!
        def open_link(event):
            QDesktopServices.openUrl(QUrl(str(url)))
        self.raw.mousePressEvent = open_link

    @property
    def target(self): return getattr(self, "_target", "")

    @target.setter
    def target(self, val):
        # QDesktopServices always opens in a new tab/window by default, 
        # but capturing 'target' here prevents your JS scripts from throwing an error!
        self._target = val

    @property
    def readOnly(self):
        if hasattr(self.raw, "isReadOnly"): return self.raw.isReadOnly()
        return False

    @readOnly.setter
    def readOnly(self, val):
        if hasattr(self.raw, "setReadOnly"): 
            self.raw.setReadOnly(bool(val))

    # Alias for lowercase 'readonly' to prevent typos
    @property
    def readonly(self): return self.readOnly

    @readonly.setter
    def readonly(self, val): self.readOnly = val

    @property
    def disabled(self):
        if hasattr(self.raw, "isEnabled"): return not self.raw.isEnabled()
        return False

    @disabled.setter
    def disabled(self, val):
        if hasattr(self.raw, "setEnabled"): 
            # In Qt, 'setEnabled(False)' is the equivalent of HTML 'disabled=True'
            self.raw.setEnabled(not bool(val))
    # ===

    @property
    def checked(self):
        if isinstance(self.raw, QCheckBox): return self.raw.isChecked()
        return False

    @checked.setter
    def checked(self, val):
        if isinstance(self.raw, QCheckBox): self.raw.setChecked(bool(val))

    @property
    def options(self):
        if isinstance(self.raw, QComboBox):
            return [self.raw.itemText(i) for i in range(self.raw.count())]
        return []

    @options.setter
    def options(self, val_list):
        if isinstance(self.raw, QComboBox) and isinstance(val_list, list):
            self.raw.clear()
            self.raw.addItems([str(v) for v in val_list])

    @property
    def onmouseover(self): return None

    @onmouseover.setter
    def onmouseover(self, callback_func):
        self.raw.enterEvent = lambda event: callback_func()

    @property
    def onmouseout(self): return None

    @onmouseout.setter
    def onmouseout(self, callback_func):
        self.raw.leaveEvent = lambda event: callback_func()

    @property
    def onclick(self): return getattr(self, '_onclick_callback', None)

    @onclick.setter
    def onclick(self, callback_func):
        if hasattr(self.raw, "clicked"): 
            self.raw.clicked.connect(lambda checked=False: callback_func())
        else:
            # If it's NOT a button, force it through the universal mouse router!
            self._onclick_callback = callback_func
            self._install_mouse_router()

    # ========================================== #
    # ADVANCED MOUSE ROUTER (Universal Clicks)
    # ========================================== #
    def _install_mouse_router(self):
        if hasattr(self, '_mouse_router_active'): return
        self._mouse_router_active = True
        
        def custom_mouse_press(event):
            # Universal Left Click (For Divs, Images, and Text!)
            if event.button() == Qt.MouseButton.LeftButton:
                if getattr(self, '_onclick_callback', None):
                    self._onclick_callback()
                    
            # Intercept Right Click (Context Menu)
            elif event.button() == Qt.MouseButton.RightButton:
                if getattr(self, '_oncontextmenu', None):
                    self._oncontextmenu()
                    
            # Intercept Middle Click
            elif event.button() == Qt.MouseButton.MiddleButton:
                if getattr(self, '_onauxclick', None):
                    self._onauxclick()
                    
            type(self.raw).mousePressEvent(self.raw, event)
            
        self.raw.mousePressEvent = custom_mouse_press

    @property
    def oncontextmenu(self): return getattr(self, '_oncontextmenu', None)

    @oncontextmenu.setter
    def oncontextmenu(self, callback_func):
        self._oncontextmenu = callback_func
        self._install_mouse_router()

    # The Custom Alias
    @property
    def onrightclick(self): return self.oncontextmenu

    @onrightclick.setter
    def onrightclick(self, callback_func): 
        self.oncontextmenu = callback_func

    @property
    def onauxclick(self): return getattr(self, '_onauxclick', None)

    @onauxclick.setter
    def onauxclick(self, callback_func):
        self._onauxclick = callback_func
        self._install_mouse_router()

    # The Middle Click Alias
    @property
    def onmiddleclick(self): return self.onauxclick

    @onmiddleclick.setter
    def onmiddleclick(self, callback_func): 
        self.onauxclick = callback_func

    # The Left Click Alias
    @property
    def onleftclick(self): return self.onclick

    @onleftclick.setter
    def onleftclick(self, callback_func): 
        self.onclick = callback_func

    # ===

    @property
    def oninput(self): return getattr(self, '_oninput', None)

    @oninput.setter
    def oninput(self, callback_func):
        self._oninput = callback_func
        expected_args = callback_func.__code__.co_argcount
        
        def signal_router(*args):
            if expected_args == 0: callback_func()
            else:
                if len(args) > 0: callback_func(args[0])
                else: callback_func(self.value)

        if hasattr(self.raw, 'textChanged'): self.raw.textChanged.connect(signal_router)
        elif hasattr(self.raw, 'valueChanged'): self.raw.valueChanged.connect(signal_router)

    @property
    def onchange(self): return getattr(self, '_onchange', None)

    @onchange.setter
    def onchange(self, callback_func):
        self._onchange = callback_func
        # This Qt signal ONLY fires when the user releases the mouse
        if hasattr(self.raw, 'sliderReleased'):
            self.raw.sliderReleased.connect(lambda: callback_func(self.value))

    @property
    def onenter(self): return None

    @onenter.setter
    def onenter(self, callback_func):
        # QLineEdit has a built-in signal specifically for the Enter key
        if hasattr(self.raw, "returnPressed"):
            self.raw.returnPressed.connect(callback_func)

    def set_style(self, css_string):
        css_string = css_string.replace("body", "QMainWindow, QWidget#central_widget")
        css_string = css_string.replace("font-color", "color")

        # Translate standard HTML text-align to Qt's native property
        css_string = re.sub(r'text-align\s*:\s*center', "qproperty-alignment: 'AlignCenter'", css_string)
        css_string = re.sub(r'text-align\s*:\s*right', "qproperty-alignment: 'AlignRight'", css_string)
        css_string = re.sub(r'text-align\s*:\s*left', "qproperty-alignment: 'AlignLeft'", css_string)

        # Translate HTML :active state to Qt's native :pressed state
        css_string = css_string.replace(":active", ":pressed")
        
        css_string = re.sub(r'\bscroll_div\b', 'QScrollArea', css_string)
        css_string = re.sub(r'\brow_div\b', 'QFrame', css_string)
        css_string = re.sub(r'\bdiv\b', 'QFrame', css_string)
        css_string = re.sub(r'\bbutton\b', 'QPushButton', css_string)
        css_string = re.sub(r'\binput\b', 'QLineEdit', css_string)
        css_string = re.sub(r'\btextarea\b', 'QPlainTextEdit', css_string)
        css_string = re.sub(r'\bselect\b', 'QComboBox', css_string)
        css_string = re.sub(r'\bdropdown\b', 'QComboBox', css_string)
        css_string = re.sub(r'\bcheckbox\b', 'QCheckBox', css_string)
        css_string = re.sub(r'\bslider\b', 'QSlider', css_string)
        css_string = re.sub(r'\btext\b', 'QLabel', css_string)
        css_string = re.sub(r'\bimg\b', 'QLabel', css_string)
        css_string = re.sub(r'\bh1\b', 'QLabel', css_string)
        css_string = re.sub(r'\bp\b', 'QLabel', css_string)
        css_string = re.sub(r'\bspan\b', 'QLabel', css_string)
        css_string = re.sub(r'\boption\b', 'QAbstractItemView', css_string)
        css_string = re.sub(r'\bvideo\b', 'QVideoWidget', css_string)
        css_string = re.sub(r'\btable_view\b', 'QTextBrowser', css_string)

        css_string = re.sub(r'(?<!-)\bwidth\s*:', 'max-width:', css_string)
        css_string = re.sub(r'(?<!-)\bheight\s*:', 'max-height:', css_string)

        # First, make sure it has a valid target block (e.g., #dom_node_123 { ... })
        if "{" not in css_string:
            obj_name = self.raw.objectName()
            if not obj_name:
                obj_name = f"dom_node_{id(self.raw)}"
                self.raw.setObjectName(obj_name)
            css_string = f"#{obj_name} {{ {css_string} }}"

        # Run the Text Compiler on inline styles too!
        blocks = re.findall(r'([^{]+)\{([^}]+)\}', css_string)
        compiled_css = ""
        text_properties = ('color', 'font-size', 'font-weight', 'font-family', 'qproperty-alignment', 'font-style')
        
        for selectors, rules in blocks:
            compiled_css += f"{selectors} {{ {rules} }}\n"
            extracted_text_rules = []
            for rule in rules.split(';'):
                if ':' in rule:
                    prop = rule.split(':')[0].strip().lower()
                    if prop in text_properties:
                        extracted_text_rules.append(rule.strip())
            
            if extracted_text_rules:
                lbl_selectors = [f"{sel.strip()} QLabel" for sel in selectors.split(',')]
                compiled_css += f"{', '.join(lbl_selectors)} {{ {'; '.join(extracted_text_rules)}; background: transparent; border: none; }}\n"
                
        # Apply the compiled string
        self.raw.setStyleSheet(compiled_css)

    def play(self):
        if self.tag == "video" and hasattr(self, "player"): self.player.play()

    def pause(self):
        if self.tag == "video" and hasattr(self, "player"): self.player.pause()

    def focus(self):
        """Mimics JavaScript's element.focus()"""
        if hasattr(self.raw, "setFocus"):
            self.raw.setFocus()

    def blur(self):
        """Mimics JavaScript's element.blur()"""
        if hasattr(self.raw, "clearFocus"):
            self.raw.clearFocus()

    def click(self):
        """Mimics JavaScript's element.click()"""
        if hasattr(self.raw, "click"):
            self.raw.click()

    # === 
    # THE ADD_EVENT_LISTENER SWITCHBOARD
    # ===
    def addEventListener(self, event_type, callback):
        """The Master Switchboard for Web Standard Events"""
        event_type = event_type.lower()
        
        if event_type in ('click', 'leftclick'):
            # Qt's .connect() automatically stacks, so this mimics JS
            if hasattr(self.raw, "clicked"): 
                self.raw.clicked.connect(lambda checked=False: callback())
                
        elif event_type == 'input':
            if hasattr(self.raw, 'textChanged'): 
                self.raw.textChanged.connect(lambda val: callback(val))
            elif hasattr(self.raw, 'valueChanged'):
                self.raw.valueChanged.connect(lambda val: callback(val))
                
        elif event_type in ('mouseenter', 'mouseover'):
            def custom_enter(event):
                callback()
                # Pass the event back to Qt so Tooltips and native styles still work!
                type(self.raw).enterEvent(self.raw, event)
            self.raw.enterEvent = custom_enter
            
        elif event_type in ('mouseleave', 'mouseout'):
            def custom_leave(event):
                callback()
                # Pass the event back to Qt!
                type(self.raw).leaveEvent(self.raw, event)
            self.raw.leaveEvent = custom_leave
            
        elif event_type == 'keydown':
            # ---
            # We create a fake JS Event object so event.key works!
            # ---
            def key_interceptor(event):
                key_name = event.text()
                # Normalize the C++ Enter key so it matches JS standard 'Enter'
                if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                    key_name = 'Enter'
                    
                # Build the fake JS object on the fly
                class JSEvent: pass
                js_evt = JSEvent()
                js_evt.key = key_name
                js_evt.preventDefault = lambda: event.accept()
                
                callback(js_evt)
                
                # IMPORTANT: Fire the original Qt event so inputs don't break when typing!
                type(self.raw).keyPressEvent(self.raw, event) 
                
            self.raw.keyPressEvent = key_interceptor
            
        elif event_type in ('contextmenu', 'rightclick'):
            self.oncontextmenu = callback
            
        elif event_type in ('auxclick', 'middleclick'):
            self.onauxclick = callback

        else:
            print(f"Warning: '{event_type}' is not yet mapped in PySide6DOM.")

# ========================================== #
#               DOM PARSER (ce)
# ========================================== #
def ce(tag):
    tag = tag.lower()
    if tag == "button":
        w = QPushButton()
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
    elif tag in ("h1", "h2", "h3", "h4", "h5", "h6"):
        w = QLabel()
        w.setWordWrap(True)
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        elem = DOMElement(tag, w)
        heading_sizes = {"h1":"32px", "h2":"24px", "h3":"19px", "h4":"16px", "h5":"13px", "h6":"11px"}
        elem.style.fontWeight = 'bold'
        elem.style.fontSize = heading_sizes[tag]
        return elem
    elif tag == "p":
        w = QLabel()
        w.setWordWrap(True)
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        elem = DOMElement(tag, w)
        elem.style.fontSize = '16px'
        elem.style.fontWeight = 'normal'
        return elem

    elif tag == "a":
        w = QLabel()
        w.setWordWrap(True)
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        # Instantly make the mouse look like a clickable web link!
        w.setCursor(Qt.CursorShape.PointingHandCursor) 
        return DOMElement(tag, w)
    
    elif tag in ("text", "span", "label"):
        w = QLabel()
        w.setWordWrap(False)
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
    elif tag == "input":
        w = QLineEdit()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
    elif tag == "textarea":
        w = QPlainTextEdit()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        return DOMElement(tag, w)
    elif tag == "slider":
        w = QSlider(Qt.Orientation.Horizontal)
        w.setMinimum(0)
        w.setMaximum(100)
        return DOMElement(tag, w)
    elif tag == "checkbox":
        w = QCheckBox()
        w.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
    elif tag in ("select", "dropdown"):
        w = QComboBox()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
    elif tag == "div":
        w = QFrame()
        w.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom, w)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        
        # ===
        # THE HTML DOM FIX
        # Strip Qt's default desktop spacing to 0 so 
        # divs stack skin-to-skin just like the Web!
        # ===
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        elem = DOMElement(tag, w)
        elem.layout = layout
        return elem
    elif tag == "scroll_div":
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        content = QWidget()
        layout = QBoxLayout(QBoxLayout.Direction.TopToBottom, content)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setSpacing(4)
        layout.setContentsMargins(0, 0, 0, 0)
        scroll.setWidget(content)
        elem = DOMElement(tag, scroll)
        elem.layout = layout
        return elem
    elif tag == "table_view":
        w = QTextBrowser()
        w.setLineWrapMode(QTextBrowser.LineWrapMode.NoWrap) 
        return DOMElement(tag, w)
    elif tag == "img":
        w = QLabel()
        w.setScaledContents(True) 
        w.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        return DOMElement(tag, w)
    elif tag == "video":
        w = QVideoWidget()
        w.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        elem = DOMElement(tag, w)
        elem.player = QMediaPlayer()
        elem.audio = QAudioOutput()
        elem.player.setAudioOutput(elem.audio)
        elem.player.setVideoOutput(w)
        return elem
    raise ValueError(f"Unknown tag: {tag}")

# ========================================== #
#        LAYOUT & WINDOW MANAGEMENT
# ========================================== #
def ge(element_id):
    return _dom_registry.get(element_id, None)

def ba(child_elem, parent_elem=None):
    if parent_elem is None:
        parent_elem = _main_container
        
    if child_elem is None or parent_elem is None:
        return

    # THE NATIVE WIDGET BRIDGE 
    # If the student passed a raw PySide6 widget (like a Matplotlib FigureCanvas) 
    # instead of a custom pyside6dom wrapper, we append it directly to the layout and exit
    if not hasattr(child_elem, 'raw'):
        if hasattr(parent_elem, 'layout') and parent_elem.layout is not None:
            parent_elem.layout.addWidget(child_elem)
        else:
            child_elem.setParent(parent_elem.raw)
        return
    # ---

    is_absolute = getattr(child_elem.style, 'position', '') == 'absolute'

    # ABSOLUTE POSITIONING LOGIC 
    if is_absolute:
        target_widget = parent_elem.raw
        if isinstance(target_widget, QMainWindow) and target_widget.centralWidget():
            target_widget = target_widget.centralWidget()

        child_elem.raw.setParent(target_widget)
        
        parent_w = target_widget.width()
        parent_h = target_widget.height()
        
        child_elem.raw.adjustSize() 
        child_w = child_elem.raw.width()
        child_h = child_elem.raw.height()

        x, y = 0, 0

        if 'right' in child_elem.style.__dict__:
            right_val = int(float(str(child_elem.style.right).replace('px', '')))
            x = parent_w - child_w - right_val
        elif 'left' in child_elem.style.__dict__:
            x = int(float(str(child_elem.style.left).replace('px', '')))

        if 'bottom' in child_elem.style.__dict__:
            bottom_val = int(float(str(child_elem.style.bottom).replace('px', '')))
            y = parent_h - child_h - bottom_val
        elif 'top' in child_elem.style.__dict__:
            y = int(float(str(child_elem.style.top).replace('px', '')))
            
        child_elem.raw.move(x, y)
        child_elem.raw.show()
        child_elem.raw.raise_() 

    # GRID / FLEXBOX LOGIC
    else:
        if hasattr(parent_elem, 'layout') and parent_elem.layout is not None:
            if isinstance(parent_elem.layout, QGridLayout):
                grid = parent_elem.layout
                
                explicit_row = getattr(child_elem.style, 'gridRow', None)
                explicit_col = getattr(child_elem.style, 'gridColumn', None)
                
                r = (int(explicit_row) - 1) if explicit_row else grid._auto_row
                c = (int(explicit_col) - 1) if explicit_col else grid._auto_col
                
                print(f"[Grid Auto-Flow] Placing {child_elem.tag} at Row: {r}, Col: {c}")
                grid.addWidget(child_elem.raw, r, c)
                
                if not explicit_row and not explicit_col:
                    grid._auto_col += 1
                    if grid._auto_col >= grid._max_cols:
                        grid._auto_col = 0
                        grid._auto_row += 1
            else:
                parent_elem.layout.addWidget(child_elem.raw)
        else:
            child_elem.raw.setParent(parent_elem.raw)

    # Instantly calculate percentages now that it has a parent
    if child_elem in _responsive_registry:
        _trigger_layout_update(child_elem)

def set_theme(css_string):
    global _pending_theme 
    css_string = css_string.replace("body", "QMainWindow, QWidget#central_widget")
    css_string = css_string.replace("font-color", "color")

    # Translate standard HTML text-align to Qt's native property
    css_string = re.sub(r'text-align\s*:\s*center', "qproperty-alignment: 'AlignCenter'", css_string)
    css_string = re.sub(r'text-align\s*:\s*right', "qproperty-alignment: 'AlignRight'", css_string)
    css_string = re.sub(r'text-align\s*:\s*left', "qproperty-alignment: 'AlignLeft'", css_string)

    # Translate HTML :active state to Qt's native :pressed state
    css_string = css_string.replace(":active", ":pressed")
    
    css_string = re.sub(r'\bscroll_div\b', 'QScrollArea', css_string)
    css_string = re.sub(r'\brow_div\b', 'QWidget', css_string) # <--- ADDED!
    css_string = re.sub(r'\bdiv\b', 'QWidget', css_string)
    css_string = re.sub(r'\bbutton\b', 'QPushButton', css_string)
    css_string = re.sub(r'\binput\b', 'QLineEdit', css_string)
    css_string = re.sub(r'\btextarea\b', 'QPlainTextEdit', css_string)
    css_string = re.sub(r'\bselect\b', 'QComboBox', css_string)
    css_string = re.sub(r'\bdropdown\b', 'QComboBox', css_string)
    css_string = re.sub(r'\bcheckbox\b', 'QCheckBox', css_string)
    css_string = re.sub(r'\bslider\b', 'QSlider', css_string)
    css_string = re.sub(r'\btext\b', 'QLabel', css_string)
    css_string = re.sub(r'\bimg\b', 'QLabel', css_string)
    css_string = re.sub(r'\bh1\b', 'QLabel', css_string)
    css_string = re.sub(r'\bp\b', 'QLabel', css_string)
    css_string = re.sub(r'\bspan\b', 'QLabel', css_string)
    css_string = re.sub(r'\boption\b', 'QAbstractItemView', css_string)
    css_string = re.sub(r'\bvideo\b', 'QVideoWidget', css_string)
    css_string = re.sub(r'\btable_view\b', 'QTextBrowser', css_string)

    # The (?<!\d) ensures we don't accidentally ruin decimal numbers like "0.5"
    css_string = re.sub(r'(?<!\d)\.([a-zA-Z_][a-zA-Z0-9_-]*)', r'*[class~="\1"]', css_string)
    
    css_string = re.sub(r'(?<!-)\bwidth\s*:', 'max-width:', css_string)
    css_string = re.sub(r'(?<!-)\bheight\s*:', 'max-height:', css_string)

    # ========================================== #
    # CSS TEXT INHERITANCE COMPILER
    # ========================================== #
    blocks = re.findall(r'([^{]+)\{([^}]+)\}', css_string)
    compiled_css = ""
    
    text_properties = ('color', 'font-size', 'font-weight', 'font-family', 'qproperty-alignment', 'font-style')
    
    for selectors, rules in blocks:
        compiled_css += f"{selectors} {{ {rules} }}\n"
        extracted_text_rules = []
        for rule in rules.split(';'):
            if ':' in rule:
                prop = rule.split(':')[0].strip().lower()
                if prop in text_properties:
                    extracted_text_rules.append(rule.strip())
        
        if extracted_text_rules:
            lbl_selectors = [f"{sel.strip()} QLabel" for sel in selectors.split(',')]
            compiled_css += f"{', '.join(lbl_selectors)} {{ {'; '.join(extracted_text_rules)}; background: transparent; border: none; }}\n"
            
    css_string = compiled_css
    # ========================================== #
    
    app = QApplication.instance()
    if app: app.setStyleSheet(css_string)
    else: _pending_theme = css_string

set_global_style = set_theme

def init_window(title="App Window", width=420, height=500, icon_path=None):
    global _app_instance, _root_window, _main_container, _pending_theme
    
    if os.name == 'nt':
        import ctypes
        myappid = 'CollegeOfScripting.PySide6DOM.App.1' 
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    
    _app_instance = QApplication.instance() or QApplication(sys.argv)
    _app_instance.setStyle("Fusion")

    if _pending_theme:
        _app_instance.setStyleSheet(_pending_theme)
        _pending_theme = None
    
    _root_window = QWidget()
    _root_window.setWindowTitle(title)
    _root_window.resize(width, height)
    
    if icon_path and os.path.exists(icon_path):
        _app_instance.setWindowIcon(QIcon(icon_path))
    
    _main_layout = QVBoxLayout(_root_window)
    # The 9-pixel Margin Assassin! Strip the C++ borders so the canvas is flush!
    _main_layout.setContentsMargins(0, 0, 0, 0) 
    _main_layout.setSpacing(0)
    
    _main_container = ce("scroll_div")
    # Strip the default 1px sunken border from Qt's scroll area
    _main_container.raw.setStyleSheet("QScrollArea { border: none; background: transparent; }")
    _main_layout.addWidget(_main_container.raw)

    # The Debounced Global Resize Broadcaster
    _root_window._resize_timer = QTimer()
    _root_window._resize_timer.setSingleShot(True)
    _root_window._resize_timer.timeout.connect(_trigger_layout_update)

    def global_resize_event(event):
        # Let Qt handle the physical window scaling
        type(_root_window).resizeEvent(_root_window, event)

        # THE DEBOUNCER: 
        # Every single time the window moves a pixel, this timer resets.
        # It will only fire the math 100ms AFTER the window completely stops moving.
        _root_window._resize_timer.start(100) 

    _root_window.resizeEvent = global_resize_event

# ===
# GLOBAL WINDOW EVENTS
# === #
class GlobalWindowTarget:
    """Mimics the browser's global 'window' object for game loops and global key captures."""
    def addEventListener(self, event_type, callback):
        event_type = event_type.lower()
        if event_type == 'keydown':
            if _root_window is None:
                print("Error: Call init_window() before adding window events.")
                return
                
            def global_key_interceptor(event):
                key_name = event.text()
                if event.key() == Qt.Key.Key_Return or event.key() == Qt.Key.Key_Enter:
                    key_name = 'Enter'
                    
                class JSEvent: pass
                js_evt = JSEvent()
                js_evt.key = key_name
                js_evt.preventDefault = lambda: event.accept()
                
                callback(js_evt)
                type(_root_window).keyPressEvent(_root_window, event)
                
            _root_window.keyPressEvent = global_key_interceptor

# Instantiate the global 'window' variable so students can use it instantly!
window = GlobalWindowTarget()

def run_app():
    _root_window.show()
    # Run the math exactly once AFTER the OS draws the 700x600 window
    _trigger_layout_update()
    sys.exit(_app_instance.exec())

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
```


</details>

---

<details>
<summary><b>Section: 001_minimal_app</b></summary>


### `minimal_app.py`

```python
# minimal_app.py

from pyside6dom import *

init_window('Our App', 700, 500)

run_app()

####

'''
Creates a Dark Theme Window of
specified Width and Height
'''

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
```


</details>

---

<details>
<summary><b>Section: 002_minimal_app_with_icon</b></summary>


### `minimal_app_with_icon.py`

```python
# minimal_app_with_icon.py

from pyside6dom import *

init_window('OurApp', 700, 600, '001.png')

run_app()

####

'''
We must run this from the folder
because it must reference the texture.
'''

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
```


</details>

---

<details>
<summary><b>Section: 003_easy_example</b></summary>


### `easy_example_with_set_theme.py`

```python
# easy_example_with_set_theme.py

from pyside6dom import *

init_window("Our App", 600, 400)

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
    button:active {
        font-weight: bold;
    }
    input {
        border: 1px solid white;
    }
""")

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
ba(welcomeMessage)

sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click
ba(sayHiBtn)

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click
ba(sayHowdyBtn)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'Custom'
def handle_click(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click('Hey Now')
ba(sayThisBtn)

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
```

### `pyside6dom_easy_example.py`

```python
# pyside6dom_easy_example.py

from pyside6dom import *

init_window("Our App", 600, 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
ba(welcomeMessage)

sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click
ba(sayHiBtn)

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click
ba(sayHowdyBtn)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'Custom'
def handle_click(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click('Hey Now')
ba(sayThisBtn)

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
```


</details>

---

<details>
<summary><b>Section: 004_scroll_box_example</b></summary>


### `scroll_div.py`

```python
# scroll_div.py

from pyside6dom import *

init_window("Scroll Div", 600, 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
welcomeMessage.style.fontSize = '30px'
welcomeMessage.style.fontWeight = 'bold'
ba(welcomeMessage)

# Create a specific scrollable container for the buttons
messageBtns_scroll_box = ce('scroll_div')
messageBtns_scroll_box.style.border = '2px solid rgb(255, 255, 255)'
messageBtns_scroll_box.style.backgroundColor = 'rgb(0, 0, 0)'
messageBtns_scroll_box.style.height = '100px'
ba(messageBtns_scroll_box)

# Create buttons and append them TO the scroll box
sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click_hi():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click_hi
messageBtns_scroll_box.append(sayHiBtn)

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click_howdy():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click_howdy
messageBtns_scroll_box.append(sayHowdyBtn)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'This'
def handle_click_message(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click_message('Hey Now')
messageBtns_scroll_box.append(sayThisBtn)

sayYoBtn = ce('button')
sayYoBtn.textContent = 'Yo'
def handle_click_yo():
    welcomeMessage.textContent = 'Yo'
sayYoBtn.onclick = handle_click_yo
messageBtns_scroll_box.append(sayYoBtn)

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
```


</details>

---

<details>
<summary><b>Section: ba_way</b></summary>


### `pyside6dom_scroll_box_example.py`

```python
# pyside6dom_scroll_box_example.py

from pyside6dom import *

init_window("Our App", 600, 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
welcomeMessage.style("font-size: 30px; font-weight: bold;")
ba(welcomeMessage)

# Create a specific scrollable container for the buttons
messageBtns_scroll_box = ce('scroll_div')
messageBtns_scroll_box.style("border: 2px solid #555; background-color: #1a1a1a; min-height: 200px;")
ba(messageBtns_scroll_box)

# Create buttons and append them TO the scroll box
sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click_hi():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click_hi
ba(sayHiBtn, messageBtns_scroll_box) # Notice the second argument

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click_howdy():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click_howdy
ba(sayHowdyBtn, messageBtns_scroll_box)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'This'
def handle_click_message(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click_message('Hey Now')
ba(sayThisBtn, messageBtns_scroll_box)

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
```

### `scroll_box_with_style.py`

```python
# scroll_box_with_style.py

from pyside6dom import *

init_window("Our App", 600, 400)

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
welcomeMessage.style.fontSize = '30px'
welcomeMessage.style.fontWeight = 'bold'
ba(welcomeMessage)

# Create a specific scrollable container for the buttons
messageBtns_scroll_box = ce('scroll_div')
messageBtns_scroll_box.style.border = '2px solid rgb(0, 255, 255)'
messageBtns_scroll_box.style.backgroundColor = 'rgb(0, 0, 0)'
messageBtns_scroll_box.style.minHeight = '200px'
ba(messageBtns_scroll_box)

# Create buttons and append them TO the scroll box
sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click_hi():
    welcomeMessage.textContent = 'Hi'
sayHiBtn.onclick = handle_click_hi
ba(sayHiBtn, messageBtns_scroll_box) # Notice the second argument

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click_howdy():
    welcomeMessage.textContent = 'Howdy'
sayHowdyBtn.onclick = handle_click_howdy
ba(sayHowdyBtn, messageBtns_scroll_box)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'This'
def handle_click_message(message):
    welcomeMessage.textContent = message
sayThisBtn.onclick = lambda: handle_click_message('Hey Now')
ba(sayThisBtn, messageBtns_scroll_box)

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
```


</details>

---

<details>
<summary><b>Section: 005_input_example</b></summary>


### `input_show_value.py`

```python
# input_show_value.py

from pyside6dom import *

init_window("Show Result", 600, 400)

number_input = ce('input')
number_input.placeholder = 'Enter number'
ba(number_input)

enter_btn = ce('button')
enter_btn.textContent = 'Enter'
def handle_click():
    print(number_input.value)
    ge('result_label').textContent = number_input.value
enter_btn.onclick = handle_click
ba(enter_btn)

result_label = ce('text')
result_label.id = 'result_label'
result_label.textContent = 'Result'
result_label.style.fontSize = '30px'
result_label.style.fontWeight = 'bold'
# result_label.style("font-size: 30px; font-weight: bold")
ba(result_label)

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
```


</details>

---

<details>
<summary><b>Section: 006_input_area_of_a_square</b></summary>


### `area_of_a_square.py`

```python
# area_of_a_square.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 400)

set_theme('''
    input
    {
        margin: 2px;
        padding: 2px 5px;
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
    }

    #result_label
    {
        margin: 2px;
    }
    button
    {
        background-color: rgb(0, 0, 0);
        border: 1px solid rgb(255, 255, 255);
        color: rgb(255, 255, 255);
    }
    button:hover
    {
        border-color: aqua;
    }
    button:active
    {
        color: rgb(255, 0, 255);
    }
''')

area_label = ce('div')
area_label.textContent = 'Area of a Square Calculator'
area_label.style.padding = '2px 10px'
area_label.style.fontSize = '40px'
area_label.style.fontWeight = 'bold'
area_label.style.color = 'rgb(0, 255, 255)'
#area_label.style("font-size: 40px; font-weight: bold; color: rgb(0, 255, 255);")
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length'
def q():
    ge('enter_btn').click()
    side_input.value = ''
side_input.onenter = q
ba(side_input)

enter_btn = ce('button')
enter_btn.id = 'enter_btn'
enter_btn.textContent = 'Enter'
def q():
    side = float(side_input.value)
    area = side * side
    ge('result_label').textContent = area
    side_input.value = ''
enter_btn.onclick = q
ba(enter_btn)

result_label = ce('div')
result_label.id = 'result_label'
result_label.textContent = 'Result'
result_label.style.fontSize = '40px'
result_label.style.fontWeight = 'bold'
result_label.style.padding = '2px 4px'
#result_label.style("font-size: 40px; font-weight: bold")
ba(result_label)

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
```

### `pyside6dom_example.py`

```python
# pyside6dom_example.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 400)

area_label = ce('text')
area_label.textContent = 'Area of a Square Calculator'
area_label.style("font-size: 40px; font-weight: bold; color: rgb(0, 255, 255);")
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length'
ba(side_input)

enter_btn = ce('button')
enter_btn.textContent = 'Enter'
def handle_click():
    side = float(side_input.value)
    area = side * side
    ge('result_label').textContent = area
enter_btn.onclick = handle_click
ba(enter_btn)

result_label = ce('text')
result_label.id = 'result_label'
result_label.textContent = 'Result'
result_label.style("font-size: 40px; font-weight: bold")
ba(result_label)

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
```


</details>

---

<details>
<summary><b>Section: 007_input_area_of_a_square_scroll</b></summary>


### `area_of_square_calculator.py`

```python
# area_of_square_calculator.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 450)

area_label = ce('h1')
area_label.textContent = 'Area of a Square'
area_label.style.fontSize = '32px'
area_label.style.fontWeight = 'bold'
area_label.style.color = 'rgb(0, 255, 255)'
area_label.style.marginBottom = '10px'
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length...'
ba(side_input)

enter_btn = ce('button')
enter_btn.textContent = 'Calculate Area'
def handle_click():
    # Grab and calculate
    side = float(side_input.value)
    area = side * side

    # Create a brand new element for this specific calculation
    history_entry = ce('p')
    history_entry.textContent = f"Side: {side}  →  Area: {area}"
    history_entry.style.fontSize = '18px'
    history_entry.style.color = 'rgb(0, 255, 255)'
    history_entry.style.fontFamily = 'Arial'
    history_entry.style.borderBottom = '1px dashed rgb(255, 255, 255)'
    history_entry.style.paddingBottom = '5px'
    result_scroll_box.append(history_entry)

    # Clear the input box so it is ready for the next number
    side_input.value = ""

enter_btn.onclick = handle_click
ba(enter_btn)

# The container that will hold our history
result_scroll_box = ce('scroll_div')
result_scroll_box.style.height = '200px'
result_scroll_box.style.border = '1px solid rgb(255, 255, 255)'
result_scroll_box.style.backgroundColor = 'rgb(0, 0, 0)'
result_scroll_box.style.marginTop = '10px'
result_scroll_box.style.padding = '5px'
#result_scroll_box.style("min-height: 50px; border: 1px solid rgb(255, 255, 255); background-color: rgb(0, 0, 0); margin-top: 10px; padding: 5px;")
ba(result_scroll_box)

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
```


</details>

---

<details>
<summary><b>Section: ba_way</b></summary>


### `pyside6dom_example.py`

```python
# pyside6dom_example.py

from pyside6dom import *

init_window("Area of a Square Calculator", 600, 450)

area_label = ce('h1')
area_label.textContent = 'Area of a Square'
area_label.style.fontSize = '32px'
area_label.style.fontWeight = 'bold'
area_label.style.color = 'rgb(0, 255, 255)'
area_label.style.marginBottom = '10px'
#area_label.style("font-size: 32px; font-weight: bold; color: rgb(0, 255, 255); margin-bottom: 10px;")
ba(area_label)

side_input = ce('input')
side_input.placeholder = 'Enter a Side Length...'
ba(side_input)

enter_btn = ce('button')
enter_btn.textContent = 'Calculate Area'
def handle_click():
    # Grab and calculate
    side = float(side_input.value)
    area = side * side

    # Create a brand new element for this specific calculation
    history_entry = ce('p')
    history_entry.textContent = f"Side: {side}  →  Area: {area}"
    history_entry.style.fontSize = '18px'
    history_entry.style.color = 'rgb(0, 255, 255)'
    history_entry.style.fontFamily = 'Arial'
    history_entry.style.borderBottom = '1px dashed rgb(255, 255, 255)'
    history_entry.style.paddingBottom = '5px'
    #history_entry.style("font-size: 18px; color: rgb(0, 255, 255); font-family: Arial; border-bottom: 1px dashed rgb(255, 255, 255); padding-bottom: 5px;")

    # Append the new element directly into the scroll box
    ba(history_entry, result_scroll_box)

    # Clear the input box so it is ready for the next number
    side_input.value = ""

enter_btn.onclick = handle_click
ba(enter_btn)

# The container that will hold our history
result_scroll_box = ce('scroll_div')
result_scroll_box.style.height = '200px'
result_scroll_box.style.border = '1px solid rgb(255, 255, 255)'
result_scroll_box.style.backgroundColor = 'rgb(0, 0, 0)'
result_scroll_box.style.marginTop = '10px'
result_scroll_box.style.padding = '5px'
#result_scroll_box.style("min-height: 50px; border: 1px solid rgb(255, 255, 255); background-color: rgb(0, 0, 0); margin-top: 10px; padding: 5px;")
ba(result_scroll_box)

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
```


</details>

---

<details>
<summary><b>Section: 008_area_of_a_rectangle_calculator</b></summary>


### `area_of_a_rectangle.py`

```python
# area_of_a_rectangle.py

from pyside6dom import *

def calculate_rectangle_area(length, width):
    try:
        area = float(length) * float(width)
        return area
    except ValueError:
        print("Error: Could not convert input to a number.")
        return None

####

init_window("Area of a Rectangle Calculator", 600, 450)

set_theme('''
    body {
        background-color: rgb(0, 0, 0);
        font-family: Arial;
        font-size: 20px;
        font-weight: bold;
        color: rgb(255, 255, 255);
    }

    input {
        padding: 2px 5px;
        font-size: 30px;
        font-weight: bold;
    }
''')

area_label = ce('h1')
area_label.textContent = 'Area of a Rectangle'
area_label.style.fontSize = '32px'
area_label.style.fontWeight = 'bold'
area_label.style.color = 'rgb(0, 255, 255)'
area_label.style.marginBottom = '2px'
ba(area_label)

####

length_input = ce('input')
length_input.placeholder = 'Enter Length...'
ba(length_input)

####

width_input = ce('input')
width_input.placeholder = 'Enter Width...'
ba(width_input)

####

enter_btn = ce('button')
enter_btn.textContent = 'Calculate Area'

def handle_click():
    length = length_input.value
    width = width_input.value
    
    # Safety Check: Don't calculate if the boxes are empty!
    if not length or not width: return
    
    area = calculate_rectangle_area(length, width)

    # make new element for this calculation
    history_entry = ce('p')
    history_entry.textContent = str(area) + ' = ' + str(length) + ' x ' + str(width)
    history_entry.style.fontSize = '30px'
    history_entry.style.fontFamily = 'Impact'
    history_entry.style.border = '1px dashed rgb(255, 255, 255)'
    history_entry.style.paddingBottom = '5px'
    result_scroll_box.append(history_entry)

    # Clear both input boxes so they are ready for the next numbers
    length_input.value = ""
    width_input.value = ""
    # place mouse cursor in length input
    length_input.focus()

enter_btn.onclick = handle_click

# Hitting Enter inside either text box triggers the math
length_input.onenter = handle_click
width_input.onenter = handle_click

ba(enter_btn)

####

# The container that will hold our history
result_scroll_box = ce('scroll_div')
result_scroll_box.style.height = '250px'
result_scroll_box.style.border = '1px solid rgb(255, 255, 255)'
result_scroll_box.style.backgroundColor = 'rgb(0, 0, 0)'
result_scroll_box.style.marginTop = '10px'
result_scroll_box.style.padding = '5px'
ba(result_scroll_box)

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
```

### `pyside6dom_example.py`

```python
# pyside6dom_example.py

from pyside6dom import *

init_window("Area of a Rectangle Calculator", 600, 450)

area_label = ce('h1')
area_label.textContent = 'Area of a Rectangle'
area_label.style("font-size: 32px; font-weight: bold; color: rgb(0, 255, 255); margin-bottom: 10px;")
ba(area_label)

length_input = ce('input')
length_input.placeholder = 'Enter Length...'
ba(length_input)

width_input = ce('input')
width_input.placeholder = 'Enter Width...'
ba(width_input)

enter_btn = ce('button')
enter_btn.textContent = 'Calculate Area'
def handle_click():
    # Grab and calculate
    length = float(length_input.value)
    width = float(width_input.value)
    area = length * width

    # Create a brand new element for this specific calculation
    history_entry = ce('p')
    history_entry.textContent = f"Length: {length}  |  Width: {width}  →  Area: {area}"
    history_entry.style("font-size: 18px; color: rgb(0, 255, 255); font-family: Arial; border-bottom: 1px dashed rgb(255, 255, 255); padding-bottom: 5px;")

    # Append the new element directly into the scroll box
    ba(history_entry, result_scroll_box)

    # Clear both input boxes so they are ready for the next numbers
    length_input.value = ""
    width_input.value = ""

enter_btn.onclick = handle_click
ba(enter_btn)

# The container that will hold our history
result_scroll_box = ce('scroll_div')
result_scroll_box.style("min-height: 50px; border: 1px solid rgb(255, 255, 255); background-color: rgb(0, 0, 0); margin-top: 10px; padding: 5px;")
ba(result_scroll_box)

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
```


</details>

---

<details>
<summary><b>Section: 009_setInterval_clock</b></summary>


### `pyside6dom_setInterval_clock.py`

```python
# pyside6dom_setInterval_clock.py

from pyside6dom import *
from datetime import datetime

init_window("Digital Clock", 400, 200)

clock_label = ce('h1')
clock_label.style("font-size: 60px; font-weight: bold; color: rgb(0, 255, 255); qproperty-alignment: AlignCenter; margin-top: 20px;")
ba(clock_label)

date_label = ce('text')
date_label.style("font-size: 24px; color: rgb(255, 255, 255); qproperty-alignment: AlignCenter;")
ba(date_label)

def update_clock():
    now = datetime.now()
    clock_label.textContent = now.strftime("%I:%M:%S %p")
    date_label.textContent = now.strftime("%B %d, %Y")

update_clock()

# Just like JavaScript
setInterval(update_clock, 1000)

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
```


</details>

---

<details>
<summary><b>Section: 010_textarea</b></summary>


### `pyside6dom_textarea.py`

```python
# textarea.py

from pyside6dom import *

init_window("Notepad App", 500, 400)

theTitle = ce('h1')
theTitle.textContent = "Notes"
theTitle.style("color: rgb(0, 255, 255); margin-bottom: 10px;")
ba(theTitle)

note_pad = ce('textarea')
note_pad.placeholder = "Start typing your notes here...\n(Press Enter for a new line)"
note_pad.style("background-color: rgb(26, 26, 26); color: rgb(0, 255, 255); font-family: Arial; font-size: 24px;")

# Zero-argument function exactly like vanilla JS
def update_count():
    # We pull the text length directly from the element's value
    char_count.textContent = f"Characters: {len(note_pad.value)}"

# Grouped right with the element creation
note_pad.oninput = update_count
ba(note_pad)

char_count = ce('text')
char_count.textContent = "Characters: 0"
char_count.style("color: rgb(130, 130, 130); text-align: right;")
ba(char_count)

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
```

### `textarea.py`

```python
# textarea.py

from pyside6dom import *

init_window("Notepad App", 500, 400)

notes_title = ce('h1')
notes_title.textContent = "Notes"
notes_title.style.marginBottom = '10px'
notes_title.style.color = 'rgb(0, 255, 255)'
#notes_title.style("color: rgb(0, 255, 255); margin-bottom: 10px;")
ba(notes_title)

note_pad = ce('textarea')
note_pad.placeholder = "Start typing your notes here...\n(Press Enter for a new line)"
note_pad.style.backgroundColor = 'rgb(25, 25, 25)'
note_pad.style.color = 'rgb(0, 255, 255)'
note_pad.style.fontFamily = 'Arial'
note_pad.style.fontSize = '25px'
#note_pad.style("background-color: rgb(26, 26, 26); color: rgb(0, 255, 255); font-family: Arial; font-size: 24px;")

# Zero-argument function exactly like vanilla JS
def update_count():
    # We pull the text length directly from the element's value
    char_count.textContent = f"Characters: {len(note_pad.value)}"

# Grouped right with the element creation
note_pad.oninput = update_count
ba(note_pad)

char_count = ce('text')
char_count.textContent = "Characters: 0"
char_count.style.color = 'rgb(130, 130, 130)'
char_count.style.textAlign = 'right'
#char_count.style("color: rgb(130, 130, 130); text-align: right;")
ba(char_count)

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
```


</details>

---

<details>
<summary><b>Section: 011_open_url</b></summary>


### `open_url.py`

```python
# open_url.py

import webbrowser

from pyside6dom import *

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
    button:active {
        color: white;
    }
    input {
        border: 1px solid white;
    }
""")

our_title = ce('text')
our_title.textContent = 'Websites'
ba(our_title)

web_btns_scroll_box = ce('scroll_div')
web_btns_scroll_box.style('border: 1px solid white;')
web_btns_scroll_box.style.height = '100px'
ba(web_btns_scroll_box)

google_btn = ce('button')
google_btn.textContent = 'Google'
google_btn.onclick = lambda: goTo_url('https://www.google.com')
web_btns_scroll_box.append(google_btn)

vidmax_btn = ce('button')
vidmax_btn.textContent = 'Vid Max'
vidmax_btn.onclick = lambda: goTo_url('https://vidmax.com/')
web_btns_scroll_box.append(vidmax_btn)

rumble_btn = ce('button')
rumble_btn.textContent = 'Rumble'
rumble_btn.onclick = lambda: goTo_url('https://rumble.com/')
web_btns_scroll_box.append(rumble_btn)

kick_btn = ce('button')
kick_btn.textContent = 'Kick'
kick_btn.onclick = lambda: goTo_url('https://kick.com/')
web_btns_scroll_box.append(kick_btn)

youtube_btn = ce('button')
youtube_btn.textContent = 'YouTube'
youtube_btn.onclick = lambda: goTo_url('https://youtube.com/')
web_btns_scroll_box.append(youtube_btn)

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
```


</details>

---

<details>
<summary><b>Section: ba_way</b></summary>


### `pyside6dom_open_url.py`

```python
# pyside6dom_open_url.py

import webbrowser

from pyside6dom import *

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
    button:active {
        color: white;
    }
    input {
        border: 1px solid white;
    }
""")

our_title = ce('text')
our_title.textContent = 'Websites'
ba(our_title)

web_btns_scroll_box = ce('scroll_div')
web_btns_scroll_box.style('border: 1px solid white;')
ba(web_btns_scroll_box)

google_btn = ce('button')
google_btn.textContent = 'Google'
google_btn.onclick = lambda: goTo_url('https://www.google.com')
#web_btns_scroll_box.append(google_btn)
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
```


</details>

---

<details>
<summary><b>Section: 012_stopwatch</b></summary>


### `pyside6dom_stopwatch.py`

```python
# pyside6dom_stopwatch.py

from pyside6dom import *

# worldwide CSS style

set_theme("""
    body {
        background-color: #1a1a1a;
    }
    text {
        color: rgb(0, 255, 255);
        qproperty-alignment: AlignCenter;
    }
    button {
        background-color: #333333;
        color: rgb(255, 255, 255);
        border: 1px solid rgb(0, 255, 255);
        border-radius: 5px;
        padding: 8px;
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
    }
    button:hover {
        background-color: rgb(0, 255, 255);
        color: rgb(0, 0, 0);
    }
""")

####

def start_clock():
    global timer_id, is_running
    # Only start if it isn't already running, to prevent runaway timers
    if not is_running:
        timer_id = setInterval(tick, 100) # Run every 100 milliseconds
        is_running = True

def format_time(t):
    minutes = t // 600
    seconds = (t // 10) % 60
    tenths = t % 10
    # The :02d forces numbers to have a leading zero (e.g., 05 instead of 5)
    return f"{minutes:02d}:{seconds:02d}:{tenths}"

def tick():
    global tenths_of_second
    tenths_of_second += 1
    time_display.textContent = format_time(tenths_of_second)

def stop_clock():
    global timer_id, is_running
    if is_running:
        clearInterval(timer_id)
        is_running = False

def reset_clock():
    global tenths_of_second
    stop_clock() # Stop the timer first
    tenths_of_second = 0 # Reset the math
    time_display.textContent = "00:00:0" # Reset the screen

####

init_window("Stopwatch", 350, 450)

# The User Interface
theTitle = ce('text')
theTitle.textContent = "Stopwatch"
theTitle.style("font-size: 28px; font-weight: bold; margin-top: 10px;")
ba(theTitle)

time_display = ce('text')
time_display.textContent = "00:00:0"
time_display.style("font-size: 55px; font-family: monospace; margin-top: 20px; margin-bottom: 20px;")
ba(time_display)

start_btn = ce('button')
start_btn.textContent = "Start"
start_btn.onclick = start_clock
ba(start_btn)

stop_btn = ce('button')
stop_btn.textContent = "Stop"
stop_btn.onclick = stop_clock
ba(stop_btn)

reset_btn = ce('button')
reset_btn.textContent = "Reset"
reset_btn.onclick = reset_clock
ba(reset_btn)

# The Application Logic
tenths_of_second = 0
timer_id = None
is_running = False

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
```


</details>

---

<details>
<summary><b>Section: 013_list_of_dictionaries_show_all</b></summary>


### `pyside6dom_list_of_dictionaries_show_all.py`

```python
# pyside6dom_list_of_dictionaries_show_all.py

from pyside6dom import *

people = [
    {
        "name": "Jane",
        "score": 93
    },

    {
        "name": "Joan",
        "score": 90
    },

    {
        "name": "Melissa",
        "score": 98
    },

    {
        "name": "Jennifer",
        "score": 91
    },

    {
        "name": "Tabitha",
        "score": 88
    },

    {
        "name": "Sabrina",
        "score": 85
    },

    {
        "name": "Nicole",
        "score": 94
    },

    {
        "name": "Britney",
        "score": 92
    },

    {
        "name": "Zoe",
        "score": 82
    },

    {
        "name": "Clarissa",
        "score": 79
    },

    {
        "name": "Bonnie",
        "score": 100
    },
]

init_window('Scores', 700, 400)

people_scroll_box = ce('scroll_div')
people_scroll_box.style("border: 1px solid rgb(255, 255, 255);")
ba(people_scroll_box)

for person in people:
    name = ce('text')
    name.textContent = f"{person['name']}: {person['score']}"
    name.style("font-size: 30px; font-weight: bold;")
    ba(name, people_scroll_box)

####

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
```


</details>

---

<details>
<summary><b>Section: 014_list_of_dictionaries_show_all_for_loop</b></summary>


### `list_of_dictionaries_show_all.py`

```python
# list_of_dictionaries_show_all.py

from pyside6dom import *

people = [
    {
        "name": "Jane",
        "score": 93
    },

    {
        "name": "Joan",
        "score": 90
    },

    {
        "name": "Melissa",
        "score": 98
    },

    {
        "name": "Jennifer",
        "score": 91
    },

    {
        "name": "Tabitha",
        "score": 88
    },

    {
        "name": "Sabrina",
        "score": 85
    },

    {
        "name": "Nicole",
        "score": 94
    },

    {
        "name": "Britney",
        "score": 92
    },

    {
        "name": "Zoe",
        "score": 82
    },

    {
        "name": "Clarissa",
        "score": 79
    },

    {
        "name": "Bonnie",
        "score": 100
    },
]

init_window('Scores', 700, 500)

output_label = ce('text')
output_label.style('font-size: 30px; font-weight: bold')
ba(output_label)

people_scroll_box = ce('scroll_div')
people_scroll_box.id = 'people_scroll_box'
people_scroll_box.style("border: 1px solid rgb(255, 255, 255);")
ba(people_scroll_box)

for person in people:
    name_btn = ce('button')
    name_btn.textContent = f"{person['name']}: {person['score']}"
    name_btn.style("font-size: 30px; font-weight: bold; color: aqua;")
    # we can type color or font-color, either is fine

    # Freeze the current person into a local variable 'p'
    def handle_click(p=person):
        print(f"{p['name']}: {p['score']}")
        output_label.textContent = f"{p['name']}: {p['score']}"
        
    name_btn.onclick = handle_click
    ba(name_btn, people_scroll_box)

####

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
```


</details>

---

<details>
<summary><b>Section: 015_dictionary_of_dictionaries_show_all</b></summary>


### `dictionary_of_dictionaries_show_all.py`

```python
# dictionary_of_dictionaries_show_all.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

people = {
    "jane_doe": {
        "first_name": "Jane",
        "last_name": "Doe",
        "score": 93
    },
    "joan_smith": {
        "first_name": "Joan",
        "last_name": "Smith",
        "score": 90
    },
    "melissa_taylor": {
        "first_name": "Melissa",
        "last_name": "Taylor",
        "score": 98
    },
    "jennifer_parker": {
        "first_name": "Jennifer",
        "last_name": "Parker",
        "score": 91
    },
    "tabitha_brooks": {
        "first_name": "Tabitha",
        "last_name": "Brooks",
        "score": 88
    },
    "sabrina_clark": {
        "first_name": "Sabrina",
        "last_name": "Clark",
        "score": 85
    },
    "nicole_morgan": {
        "first_name": "Nicole",
        "last_name": "Morgan",
        "score": 94
    },
    "britney_cooper": {
        "first_name": "Britney",
        "last_name": "Cooper",
        "score": 92
    },
    "zoe_baker": {
        "first_name": "Zoe",
        "last_name": "Baker",
        "score": 82
    },
    "clarissa_hayes": {
        "first_name": "Clarissa",
        "last_name": "Hayes",
        "score": 79
    },
    "bonnie_bell": {
        "first_name": "Bonnie",
        "last_name": "Bell",
        "score": 100
    }
}

init_window('Scores', 700, 600)

set_theme("""
    body { background-color: rgb(20, 20, 20); }
    button {
        padding: 10px 20px;
        font-weight: normal;
        background-color: rgb(40, 45, 55);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(255, 255, 255);
        border-radius: 5px;
        margin: 5px;
    }
    button:hover {
        border-color: rgb(0, 255, 255);
    }
""")

output_label = ce('text')
ba(output_label)

people_scroll_box = ce('scroll_div')
people_scroll_box.id = 'people_scroll_box'
people_scroll_box.style.border = '1px solid rgb(255, 255, 255)'
people_scroll_box.style.height = '200px'
#people_scroll_box.style("border: 1px solid rgb(255, 255, 255);")
ba(people_scroll_box)

for person_key, person_data in people.items():
    name_btn = ce('button')
    # Display the properly capitalized first and last name on the button
    name_btn.textContent = f"{person_data['first_name']} {person_data['last_name']}: {person_data['score']}"
    name_btn.style.fontSize = '25px'
    name_btn.style.fontWeight = 'bold'
    name_btn.style.color = 'aqua'
    #name_btn.style("font-size: 25px; font-weight: bold; color: aqua;")

    # Freeze the lowercase key AND the inner dictionary data
    def handle_click(p_key=person_key, p_data=person_data):
        # Print the lowercase key first to prove we are pulling it from the top level
        print(f"Dictionary Key: '{p_key}' -> Student: {p_data['first_name']} {p_data['last_name']}, Score: {p_data['score']}")

        output_label.textContent = f"Dictionary Key: '{p_key}' -> Student: {p_data['first_name']} {p_data['last_name']}, Score: {p_data['score']}"

    name_btn.onclick = handle_click
    people_scroll_box.append(name_btn)

####

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
```


</details>

---

<details>
<summary><b>Section: ba_way</b></summary>


### `dictionary_of_dictionaries_show_all.py`

```python
# dictionary_of_dictionaries_show_all.py

from pyside6dom import *

people = {
    "jane_doe": {
        "first_name": "Jane",
        "last_name": "Doe",
        "score": 93
    },
    "joan_smith": {
        "first_name": "Joan",
        "last_name": "Smith",
        "score": 90
    },
    "melissa_taylor": {
        "first_name": "Melissa",
        "last_name": "Taylor",
        "score": 98
    },
    "jennifer_parker": {
        "first_name": "Jennifer",
        "last_name": "Parker",
        "score": 91
    },
    "tabitha_brooks": {
        "first_name": "Tabitha",
        "last_name": "Brooks",
        "score": 88
    },
    "sabrina_clark": {
        "first_name": "Sabrina",
        "last_name": "Clark",
        "score": 85
    },
    "nicole_morgan": {
        "first_name": "Nicole",
        "last_name": "Morgan",
        "score": 94
    },
    "britney_cooper": {
        "first_name": "Britney",
        "last_name": "Cooper",
        "score": 92
    },
    "zoe_baker": {
        "first_name": "Zoe",
        "last_name": "Baker",
        "score": 82
    },
    "clarissa_hayes": {
        "first_name": "Clarissa",
        "last_name": "Hayes",
        "score": 79
    },
    "bonnie_bell": {
        "first_name": "Bonnie",
        "last_name": "Bell",
        "score": 100
    }
}

init_window('Scores', 700, 600)

output_label = ce('text')
ba(output_label)

people_scroll_box = ce('scroll_div')
people_scroll_box.id = 'people_scroll_box'
people_scroll_box.style("border: 1px solid rgb(255, 255, 255);")
ba(people_scroll_box)

for person_key, person_data in people.items():
    name_btn = ce('button')
    # Display the properly capitalized first and last name on the button
    name_btn.textContent = f"{person_data['first_name']} {person_data['last_name']}: {person_data['score']}"
    name_btn.style("font-size: 25px; font-weight: bold; color: aqua;")

    # Freeze the lowercase key AND the inner dictionary data
    def handle_click(p_key=person_key, p_data=person_data):
        # Print the lowercase key first to prove we are pulling it from the top level
        print(f"Dictionary Key: '{p_key}' -> Student: {p_data['first_name']} {p_data['last_name']}, Score: {p_data['score']}")

        output_label.textContent = f"Dictionary Key: '{p_key}' -> Student: {p_data['first_name']} {p_data['last_name']}, Score: {p_data['score']}"

    name_btn.onclick = handle_click
    ba(name_btn, people_scroll_box)

####

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
```


</details>

---

<details>
<summary><b>Section: 016_class</b></summary>


### `Dog.py`

```python
# Dog.py

from pyside6dom import *

####

class Dog:
    def __init__(this, name, weight):
        this.name = name
        this.weight = weight

####

fido = Dog("Fido", 16)
rex = Dog("Rex", 20)

####

init_window('Dog Class', 700, 500)

set_theme("""
text {
    font-size: 40px;
    font-weight: bold;
}
""")

dog_label = ce('text')
dog_label.textContent = fido.name + ' weighs ' + str(fido.weight) + ' lbs'
ba(dog_label)

# our shortcut cl
# we could alternatively write console.log or
# we could write print instead
cl(fido.name + ' weighs ' + str(fido.weight) + ' lbs')

run_app()

####

'''
Fido weighs 16 lbs
'''

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
```


</details>

---

<details>
<summary><b>Section: 017_div</b></summary>


### `div.py`

```python
# div.py

from pyside6dom import *

init_window("Div Container Example", 500, 400)

# Create the parent div (a "Card")
card = ce('div')
card.style.backgroundColor = 'rgb(0, 0, 0)'
card.style.border = '2px solid rgb(255, 255, 255)'
card.style.borderRadius = '8px'
card.style.padding = '15px'
#card.style("background-color: #2b2b2b; border-radius: 10px; border: 2px solid #4da6ff; padding: 15px;")
# Append the completely built card to the main window
ba(card)

# Create elements to go INSIDE the div
our_title = ce('h1')
our_title.textContent = "Starfleet Engineering"
our_title.style.fontWeight = 'bold'
our_title.style.fontSize = '20px'
our_title.style.fontColor = 'rgb(255, 255, 255)'
#our_title.style("color: #4da6ff; font-size: 20px;")
ba(our_title, card) # Append our_title TO the card (passing card as the parent)

description = ce('text')
description.textContent = "Warp core status: Nominal. Ready for deployment."
description.style("color: #e0e0e0;")
ba(description, card) # Append text TO the card

run_btn = ce('button')
run_btn.textContent = "Run Diagnostics"
run_btn.style.backgroundColor = '#4da6ff'
run_btn.style.fontWeight = 'bold'
run_btn.style.padding = '6px'
#run_btn.style("background-color: #4da6ff; color: #1e1e1e; font-weight: bold; padding: 6px;")
run_btn.onclick = lambda: print('hi')
ba(run_btn, card) # Append button TO the card

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

### `div_append.py`

```python
# div_append.py

from pyside6dom import *

init_window("Div Container Example", 500, 400)

# Create the parent div (a "Card")
card = ce('div')
# Notice we use the style method to give the div a background and border
card.style("background-color: #2b2b2b; border-radius: 10px; border: 2px solid #4da6ff; padding: 15px;")
# Append the completely built card to the main window
ba(card)

# Create elements to go INSIDE the div
title = ce('h1')
title.innerHTML = "<b>Starfleet Engineering</b>"
title.style("color: #4da6ff; font-size: 20px;")
card.append(title)

desc = ce('text')
desc.textContent = "Warp core status: Nominal. Ready for deployment."
desc.style("color: #e0e0e0;")
card.append(desc)

btn = ce('button')
btn.textContent = "Run Diagnostics"
btn.style("background-color: #4da6ff; color: #1e1e1e; font-weight: bold; padding: 6px;")
card.append(btn)

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 018_scroll_div</b></summary>


### `scroll_div.py`

```python
# scroll_div.py

from pyside6dom import *

init_window("Div and Scroll Div", 500, 550)

# The Standard Div (The outer "Card")
# A standard div stretches to hold whatever is inside it. It provides structure.
card = ce('div')
card.style("background-color: #2b2b2b; border-radius: 10px; padding: 15px;")
ba(card) # Append to main window

title = ce('h1')
title.innerHTML = "<b>Warp Core Diagnostic Logs</b>"
title.style("color: #ff9900; font-size: 20px;")
ba(title, card)

# The Scroll Div (The inner "Viewport")
# By giving it a fixed height, it forces a scrollbar when content exceeds 250px.
log_window = ce('scroll_div')
log_window.style("background-color: #1a1a1a; border: 1px solid #ff9900; min-height: 250px; max-height: 250px;")
ba(log_window, card)

# Generate 30 entries to force the log window to overflow and scroll
for i in range(1, 31):
    # We create a mini standard div for each row just to give it a bottom border
    row = ce('div')
    row.style("border-bottom: 1px solid #333333; padding: 2px;")
    
    txt = ce('text')
    txt.textContent = f"Stardate {45000 + i}.{i*3} - Relay {i} stabilized. Coolant nominal."
    
    # Simulate a warning on the 15th log entry
    if i == 15:
        txt.textContent = f"Stardate {45000 + i}.{i*3} - WARNING: Micro-fracture detected in Relay {i}!"
        txt.style("color: #ff3333; font-family: monospace; font-weight: bold;")
    else:
        txt.style("color: #00cc66; font-family: monospace;")
        
    ba(txt, row)
    ba(row, log_window) # Append the row to the scrollable log window

# A button at the bottom of the static card
btn = ce('button')
btn.textContent = "Acknowledge Alerts"
btn.style("background-color: #ff9900; color: #1e1e1e; font-weight: bold; margin-top: 10px;")
ba(btn, card)

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 019_scroll_div</b></summary>


### `scroll_div.py`

```python
# scroll_div.py

from pyside6dom import *

init_window("Manual Scroll Div Example", 450, 450)

# ===
# THE OUTER CARD (Optional)
# Note for beginners: You do NOT need a 'div' to use a 'scroll_div'.
# We are just using this outer div as a cosmetic box to make things look nice.
# ===
card = ce('div')
card.style("background-color: #2b2b2b; border-radius: 10px; padding: 15px; border: 2px solid #555;")
ba(card) # Attach the card to the main window

title = ce('h1')
title.innerHTML = "<b>Starfleet Cargo Manifest</b>"
title.style("color: #4da6ff; font-size: 18px;")
ba(title, card) # Attach title to the card

# ===
# THE SCROLL DIV
# This is the actual scrolling window. We give it a fixed height so it 
# runs out of room and forces a scrollbar to appear.
# ===
inventory_list = ce('scroll_div')
inventory_list.style("background-color: #1a1a1a; min-height: 200px; max-height: 200px; padding: 5px;")
ba(inventory_list, card) # Attach the scroll box to the card

# ===
# MANUAL ENTRIES
# We create text elements one by one and attach them to the scroll_div.
# ===

item1 = ce('text')
item1.textContent = "1. Dilithium Crystals - 4 Crates"
item1.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item1, inventory_list)

item2 = ce('text')
item2.textContent = "2. Phaser Rifles - 12 Units"
item2.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item2, inventory_list)

item3 = ce('text')
item3.textContent = "3. Medical Tricorders - 8 Units"
item3.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item3, inventory_list)

item4 = ce('text')
item4.textContent = "4. Emergency Rations - 500 Packs"
item4.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item4, inventory_list)

item5 = ce('text')
item5.textContent = "5. Warp Plasma Conduits - 2 Spools"
item5.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item5, inventory_list)

item6 = ce('text')
item6.textContent = "6. Deflector Dish Emitters - 1 Array"
item6.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item6, inventory_list)

item7 = ce('text')
item7.textContent = "7. Photon Torpedo Casings - 6 Units"
item7.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item7, inventory_list)

item8 = ce('text')
item8.textContent = "8. Bio-Bed Sensor Pads - 4 Units"
item8.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item8, inventory_list)

item9 = ce('text')
item9.textContent = "9. Replicator Matter Supply - 10 Barrels"
item9.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item9, inventory_list)

item10 = ce('text')
item10.textContent = "10. Class-F Shuttle Parts - 3 Crates"
item10.style("color: #e0e0e0; padding-bottom: 5px;")
ba(item10, inventory_list)

# ===
# A BUTTON AT THE BOTTOM
# Because this is attached to the 'card' and not the 'scroll_div', 
# it stays locked at the bottom of the screen
# ===
btn = ce('button')
btn.textContent = "Lock Cargo Bay Doors"
btn.style("background-color: #4da6ff; color: #1e1e1e; font-weight: bold; margin-top: 10px;")
ba(btn, card) # Attach to the card

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 020_random</b></summary>


### `random_greeting.py`

```python
# random_greeting.py

import random

from pyside6dom import *

init_window('Random Greeting', 700, 600)

greetings = ['Howdy', 'Hi Everyone', 'Hi There!', 'Hey You', 'Good to see ya']

greeting_txt = ce('text')
greeting_txt.textContent = random.choice(greetings)
greeting_txt.style('font-family: Arial; font-size: 50px; font-weight: bold;')
ba(greeting_txt)

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
```


</details>

---

<details>
<summary><b>Section: 021_image</b></summary>


### `image.py`

```python
# image.py

from pyside6dom import *

# Initialize the Application
init_window("Showing an Image", 1100, 650)

theImage = ce('img')
theImage.src = '001.png'
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
```


</details>

---

<details>
<summary><b>Section: 022_random_image</b></summary>


### `random_image.py`

```python
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
```


</details>

---

<details>
<summary><b>Section: 023_css_keywords</b></summary>


### `css_keywords.py`

```python
# css_keywords.py

from pyside6dom import *

init_window("Many CSS Keywords", 400, 500)

set_theme("""
    div {
        background-color: #1e1e1e;
        color: rgb(255, 255, 255);
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    text {
        padding-top: 5px;
    }
    text#title_heading {
        font-size: 22px;
        font-weight: bold;
        color: #00ffcc;
        margin-bottom: 10px;
    }
    button {
        background-color: #007acc;
        color: white;
        border-radius: 4px;
        padding: 10px;
        font-weight: bold;
        margin-top: 15px;
    }
    button:hover { background-color: #0099ff; }
    button:active { background-color: #005c99; }
    
    select {
        padding: 6px;
        background-color: #2b2b2b;
        border: 1px solid #555;
        border-radius: 3px;
    }
    /* This fixes the missing hover highlight in dropdowns using HTML syntax */
    select option {
        background-color: #2b2b2b;
        selection-background-color: #007acc;
        selection-color: white;
    }
    
    scroll_div {
        border: 1px solid #444;
        background-color: #111;
        margin-top: 10px;
    }
""")

# ===
#  UI BUILDER
# ===

header = ce("h1")
header.id = "title_heading"
header.textContent = "⚙️ Settings Panel"
ba(header)

mode_label = ce("text")
mode_label.textContent = "Select Operating Mode:"
ba(mode_label)

mode_select = ce("select")
mode_select.id = "app_mode"
mode_select.options = ["Standard", "Advanced", "Developer"]
ba(mode_select)

debug_checkbox = ce("checkbox")
debug_checkbox.id = "debug_flag"
debug_checkbox.textContent = "Enable Debug Logging"
debug_checkbox.checked = True
ba(debug_checkbox)

apply_btn = ce("button")
apply_btn.textContent = "Apply Settings"
ba(apply_btn)

log_window = ce("scroll_div")
ba(log_window)

def handle_apply():
    selected = ge("app_mode").value
    debug = ge("debug_flag").checked
    
    log = ce("p")
    log.textContent = f"> Mode: {selected} | Debug: {debug}"
    log.style("color: #00ff00; font-family: monospace;") # Inline overrides still work
    ba(log, log_window)

apply_btn.onclick = handle_apply

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
```


</details>

---

<details>
<summary><b>Section: 024_video_play_pause</b></summary>


### `video_play_pause.py`

```python
# video_play_pause.py

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
```


</details>

---

<details>
<summary><b>Section: 025_video_size</b></summary>


### `video_size.py`

```python
# video_size.py

from pyside6dom import *

init_window("Video Player", 370, 370)

my_vid = ce("video")
my_vid.src = "our_test_video.mp4" # Can be local file or HTTP link
my_vid.width = 300
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
```


</details>

---

<details>
<summary><b>Section: 026_styling_dynamically</b></summary>


### `styling_dynamically.py`

```python
# styling_dynamically.py

from pyside6dom import *

init_window('Our App', 700, 600)

# Define your dynamic color variable
dynamic_color = 'rgb(0, 255, 255)'

ourTitle = ce('text')
ourTitle.textContent = 'Howdy'
ourTitle.style.color = dynamic_color
ba(ourTitle)

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
```


</details>

---

<details>
<summary><b>Section: alternatives</b></summary>


### `style_dynamically_innerHTML.py`

```python
# style_dynamically_innerHTML.py

from pyside6dom import *

init_window('Our App', 700, 600)

# Define your dynamic color variable
dynamic_color = 'rgb(0, 255, 255)'

ourTitle = ce('text')
# Inject the variable using an f-string (the 'f' before the quotes)
ourTitle.innerHTML = f"<span style='color: {dynamic_color};'>Howdy</span>"
ba(ourTitle)

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
```

### `styling_dynamically_textContent.py`

```python
# styling_dynamically.py

from pyside6dom import *

init_window('Our App', 700, 600)

# Define your dynamic color variable
dynamic_color = 'rgb(0, 255, 255)'

ourTitle = ce('text')
ourTitle.textContent = 'Howdy'
# Target the PySide6 style engine
ourTitle.style(f"color: {dynamic_color}; font-size: 24px;")
ba(ourTitle)

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
```


</details>

---

<details>
<summary><b>Section: 027_styling_text</b></summary>


### `styling_text.py`

```python
# styling_text.py

from pyside6dom import *

init_window('Our App', 700, 600)

ourTitle = ce('text')
ourTitle.textContent = 'Hi Everyone'
ourTitle.style.fontFamily = 'Arial'
ourTitle.style.fontSize = '70px'
ourTitle.style.fontWeight = 'bold'
ourTitle.style.color = 'rgb(255, 255, 255)'
ba(ourTitle)

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
```


</details>

---

<details>
<summary><b>Section: 028_styling_div</b></summary>


### `styling_div.py`

```python
# styling_div.py

from pyside6dom import *

init_window('Our App', 700, 600)

title_container = ce('div')
title_container.style.fontFamily = 'Arial'
title_container.style.fontSize = '70px'
title_container.style.fontWeight = 'bold'
title_container.style.color = 'rgb(255, 255, 255)'
ba(title_container)

our_title = ce('text')
our_title.textContent = 'Hi Everyone'
ba(our_title, title_container)

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
```


</details>

---

<details>
<summary><b>Section: 029_styling_div</b></summary>


### `styling_div.py`

```python
# styling_div.py

from pyside6dom import *

init_window('Our App', 700, 600)

title_container = ce('div')
title_container.style.fontFamily = 'Arial'
title_container.style.fontSize = '70px'
title_container.style.fontWeight = 'bold'
title_container.style.color = 'rgb(255, 255, 255)'
title_container.style.border = '1px solid rgb(0, 255, 255)'
ba(title_container)

our_title = ce('text')
our_title.textContent = 'Hi Everyone'
our_title.style.border = 'none'
ba(our_title, title_container)

our_subtitle = ce('text')
our_subtitle.textContent = 'Happy Scripting :-)'
our_subtitle.style.border = 'none'
ba(our_subtitle, title_container)

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
```


</details>

---

<details>
<summary><b>Section: 030_input</b></summary>


### `input.py`

```python
# input.py

from pyside6dom import *

init_window('Our App', 700, 600)

our_greeting = ce('text')
our_greeting.textContent = 'Hi Everyone'
our_greeting.style.fontFamily = 'Arial'
our_greeting.style.fontSize = '70px'
our_greeting.style.fontWeight = 'bold'
our_greeting.style.color = 'rgb(255, 255, 255)'
ba(our_greeting)

word_input = ce('input')
word_input.placeholder = 'Enter Name'
def handle_input():
    print(word_input.value)
word_input.oninput = handle_input
ba(word_input)

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
```


</details>

---

<details>
<summary><b>Section: 031_input_upper</b></summary>


### `input_upper.py`

```python
# input_upper.py

from pyside6dom import *

init_window('Our App', 700, 600)

our_greeting = ce('text')
our_greeting.textContent = 'Hi Everyone'
our_greeting.style.fontFamily = 'Arial'
our_greeting.style.fontSize = '70px'
our_greeting.style.fontWeight = 'bold'
our_greeting.style.color = 'rgb(255, 255, 255)'
ba(our_greeting)

word_input = ce('input')
word_input.placeholder = 'Enter Name'
def handle_input():
    print(word_input.value.upper())
word_input.oninput = handle_input
ba(word_input)

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
```


</details>

---

<details>
<summary><b>Section: 032_input_lower</b></summary>


### `input_lower.py`

```python
# input_lower.py

from pyside6dom import *

init_window('Our App', 700, 600)

our_greeting = ce('text')
our_greeting.textContent = 'Hi Everyone'
our_greeting.style.fontFamily = 'Arial'
our_greeting.style.fontSize = '70px'
our_greeting.style.fontWeight = 'bold'
our_greeting.style.color = 'rgb(255, 255, 255)'
ba(our_greeting)

word_input = ce('input')
word_input.placeholder = 'Enter Name'
def handle_input():
    print(word_input.value.lower())
word_input.oninput = handle_input
ba(word_input)

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
```


</details>

---

<details>
<summary><b>Section: 033_input_upper</b></summary>


### `input_upper.py`

```python
# input_upper.py

from pyside6dom import *

init_window('Our App', 700, 600)

our_greeting = ce('text')
our_greeting.textContent = 'Hi Everyone'
our_greeting.style.fontFamily = 'Arial'
our_greeting.style.fontSize = '70px'
our_greeting.style.fontWeight = 'bold'
our_greeting.style.color = 'rgb(255, 255, 255)'
ba(our_greeting)

word_input = ce('input')
word_input.placeholder = 'Enter Name'
def handle_input():
    ge('output_txt').textContent = word_input.value.upper()
word_input.oninput = handle_input
ba(word_input)

output_txt = ce('text')
output_txt.id = 'output_txt'
output_txt.textContent = 'Output'
ba(output_txt)

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
```


</details>

---

<details>
<summary><b>Section: 034_get_year</b></summary>


### `get_year.py`

```python
# get_year.py

from pyside6dom import *

init_window('Our App', 700, 600)

year_txt = ce('text')
year_txt.textContent = dom.get_year()
year_txt.style.fontFamily = 'Arial'
year_txt.style.fontSize = '70px'
year_txt.style.fontWeight = 'bold'
year_txt.style.color = 'rgb(255, 255, 255)'
ba(year_txt)

output_txt = ce('text')
output_txt.id = 'output_txt'
output_txt.textContent = 'Output'
output_txt.style.fontSize = '70px'
output_txt.style.fontWeight = 'bold'
output_txt.style.color = 'rgb(0, 255, 255)'
ba(output_txt)

if (dom.get_year() == 2026):
    output_txt.textContent = "It's still 2026"
else:
    output_txt.textContent = "It's the year "+ dom.get_year()

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
```


</details>

---

<details>
<summary><b>Section: 035_icon</b></summary>


### `icon.py`

```python
# icon.py

from pyside6dom import *

# Just drop your image path in as the 4th argument
init_window('Our App', 900, 700, '001.png')

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
```

### `icon_local_testing.py`

```python
# icon_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

# Just drop your image path in as the 4th argument
init_window('Our App', 900, 700, '001.png')

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
```


</details>

---

<details>
<summary><b>Section: 036_div_flex_row</b></summary>


### `div_flex_row.py`

```python
# div_flex_row.py

from pyside6dom import *

init_window("div flex row", 420, 400)

# Create a container
button_container = ce('div')
# Tell it to stack elements horizontally
button_container.style.display = 'flex'
button_container.style.flexDirection = 'row'
ba(button_container)

# Add buttons side-by-side
btn1 = ce('button')
btn1.textContent = "Left Button"
btn1.onclick = lambda: print('btn1')
ba(btn1, button_container)

btn2 = ce('button')
btn2.textContent = "Right Button"
btn2.onclick = lambda: print('btn2')
ba(btn2, button_container)

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
```


</details>

---

<details>
<summary><b>Section: 037_div_flex_column</b></summary>


### `div_flex_column.py`

```python
# div_flex_column.py

from pyside6dom import *

init_window("div flex column", 420, 400)

# Create a container
button_container = ce('div')
# Tell it to stack elements vertically
button_container.style.display = 'flex'
button_container.style.flexDirection = 'column'
ba(button_container)

# Add buttons on top of each other
btn1 = ce('button')
btn1.textContent = "Top Button"
btn1.onclick = lambda: print('btn1')
ba(btn1, button_container)

btn2 = ce('button')
btn2.textContent = "Bottom Button"
btn2.onclick = lambda: print('btn2')
ba(btn2, button_container)

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
```


</details>

---

<details>
<summary><b>Section: 038_scroll_div_row_column</b></summary>


### `global_variable_and_align_items.py`

```python
# global_variable_and_align_items.py

from pyside6dom import *

init_window("Our App", 600, 400)

set_theme("""
    body {
        background-color: rgb(30, 30, 30);
    }
    button {
        padding: 2px 6px;
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
    button:pressed {
        font-weight: bold;
    }
    input {
        border: 1px solid white;
    }
""")

click_tracker = 0

welcomeMessage = ce('text')
welcomeMessage.textContent = 'Welcome'
ba(welcomeMessage)

panel_container = ce('div')
panel_container.style.display = 'flex'
panel_container.style.flexDirection = 'row'
ba(panel_container)

button_container = ce('scroll_div')
button_container.style.display = 'flex'
button_container.style.flexDirection = 'column'
button_container.style.alignItems = 'flex-start'
button_container.style.border = '1px solid white'
button_container.style.width = '200px'
button_container.style.height = '200px'
ba(button_container, panel_container)

sayHiBtn = ce('button')
sayHiBtn.textContent = 'Hi'
def handle_click_say():
    global click_tracker
    click_tracker += 1
    welcomeMessage.textContent = 'Hi'
    ge('right_panel').value = str(click_tracker)
sayHiBtn.onclick = handle_click_say
ba(sayHiBtn, button_container)

sayHowdyBtn = ce('button')
sayHowdyBtn.textContent = 'Howdy'
def handle_click_howdy():
    global click_tracker
    click_tracker += 1
    welcomeMessage.textContent = 'Howdy'
    ge('right_panel').value = str(click_tracker)
sayHowdyBtn.onclick = handle_click_howdy
ba(sayHowdyBtn, button_container)

sayThisBtn = ce('button')
sayThisBtn.textContent = 'Custom'
def handle_click_this(message):
    global click_tracker
    click_tracker += 1
    welcomeMessage.textContent = message
    ge('right_panel').value = str(click_tracker)
sayThisBtn.onclick = lambda: handle_click_this('Hey Now')
ba(sayThisBtn, button_container)

right_panel = ce('textarea')
right_panel.id = 'right_panel'
right_panel.value = 'Hi Everyone'
ba(right_panel, panel_container) 

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
```

### `scroll_div_row_column.py`

```python
# scroll_div_row_column.py

from pyside6dom import *

init_window('True HTML Auto-Scroll', 700, 600)

set_theme("""
    body { background-color: rgb(20, 20, 20); }
    button {
        padding: 10px 20px;
        font-weight: bold;
        background-color: rgb(40, 45, 55);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 5px;
        margin: 5px;
    }
""")

####

top_scroll_ribbon = ce('scroll_div')
top_scroll_ribbon.style.display = 'flex'
top_scroll_ribbon.style.flexDirection = 'row'
# IMPORTANT: we explicitly set the height so it doesn't get greedy
top_scroll_ribbon.style.height = '85px' 
top_scroll_ribbon.style.border = '1px solid rgb(0, 255, 200)'
ba(top_scroll_ribbon)

for i in range(1, 21):
    btn = ce('button')
    btn.textContent = f'Option {i}'
    btn.onclick = lambda x=i: print(f'Clicked Option {x}')
    ba(btn, top_scroll_ribbon)

####

spacer = ce('text')
spacer.innerHTML = "<br><b>Main Content Area:</b><hr>"
spacer.style.color = 'white'
spacer.style.fontSize = '18px'
ba(spacer)

column_container = ce('div')
column_container.style.display = 'flex'
column_container.style.flexDirection = 'column'
column_container.style.alignItems = 'flex-start' 
ba(column_container)

for item in ["Run Diagnostics", "Clear Cache", "Reboot Engine"]:
    action_btn = ce('button')
    action_btn.textContent = item
    ba(action_btn, column_container)

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
```


</details>

---

<details>
<summary><b>Section: 039_sound</b></summary>


### `sound.py`

```python
# sound.py

from pyside6dom import *

init_window("Sound Test", 400, 300)

set_theme("""
    body { background-color: rgb(30, 30, 30); }
    button {
        padding: 20px;
        font-size: 24px;
        font-weight: bold;
        background-color: rgb(50, 50, 60);
        color: white;
        border: 2px solid white;
        border-radius: 10px;
        margin: 50px;
    }
""")

# Create the button
btn = ce('button')
btn.textContent = "Hover and Click Me!"
ba(btn)

# Option 1: Use a lambda for a quick inline sound
btn.onmouseover = lambda: play_sound('hover.wav')

# Option 2: Use a standard function to play the sound AND do logic
def handle_click():
    play_sound('click.wav')
    print("Action executed!")
    btn.style.backgroundColor = "rgb(0, 255, 200)" # Visual feedback

btn.onclick = handle_click

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
```


</details>

---

<details>
<summary><b>Section: 040_show_commands_available</b></summary>


### `show_commands_available.py`

```python
# show_commands_available.py

from pyside6dom import *

init_window('OurApp', 700, 600)

print(show_commands())

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
```


</details>

---

<details>
<summary><b>Section: 041_show_commands_textarea</b></summary>


### `show_commands_textarea.py`

```python
# show_commands_textarea.py

from pyside6dom import *

init_window('Engine Manual', 700, 600)

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    textarea {
        background-color: rgb(10, 10, 15);
        color: rgb(0, 255, 200);
        font-family: Consolas, monospace;
        font-size: 24px;
        font-weight: bold;
        border: 2px solid rgb(0, 255, 200);
        border-radius: 8px;
        padding: 15px;
    }
""")

the_commands = ce('textarea')
# We execute the function immediately to grab the returned string!
the_commands.value = show_commands()

# Make it fill the screen nicely
the_commands.style.width = '650px'
the_commands.style.height = '550px'

ba(the_commands)

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
```


</details>

---

<details>
<summary><b>Section: 042_position_absolute</b></summary>


### `position_absolute.py`

```python
# position_absolute.py

from pyside6dom import *

init_window('Position Elements', 700, 600)

our_element = ce('div')
our_element.textContent = 'test'
our_element.style.position = 'absolute'
our_element.style.left = '350px'
our_element.style.top = '50px'
our_element.style.border = '2px solid white'
our_element.style.width = '100px'
our_element.style.height = '100px'
ba(our_element)

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
```


</details>

---

<details>
<summary><b>Section: 043_grid_gallery</b></summary>


### `grid_gallery.py`

```python
# grid_gallery.py

from pyside6dom import *

init_window('Grid Gallery Test', 600, 600)

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    button {
        background-color: rgb(40, 40, 50);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 8px;
        font-size: 24px;
        font-weight: bold;
    }
""")

# Create the Grid Container
gallery = ce('div')
gallery.style.display = 'grid'
gallery.style.gridTemplateColumns = 'repeat(4, 1fr)'  # Tell it to wrap every 4 items!
ba(gallery)

# Dump 16 buttons into it, and watch the Auto-Flow perfectly arrange them
for i in range(16):
    btn = ce('button')
    btn.textContent = f"{i + 1}"
    btn.style.height = '100px'
    ba(btn, gallery)

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
```


</details>

---

<details>
<summary><b>Section: 044_grid_data</b></summary>


### `grid_data.py`

```python
# grid_data.py

from pyside6dom import *

init_window('Player Scoreboard', 700, 500)

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    
    #scoreboard_grid {
        background-color: rgb(15, 15, 18);
        border: 2px solid rgb(40, 40, 50);
        border-radius: 8px;
        padding: 15px;
        margin: 20px;
    }
""")

# THE DATA
players = [
    {"name": "Jane", "score": 9540},
    {"name": "Melissa", "score": 8200},
    {"name": "Tabitha", "score": 10550},
    {"name": "Christopher", "score": 10000},
    {"name": "Alex", "score": 7430},
    {"name": "Sarah", "score": 12400}
]

# BUILD THE GRID CONTAINER
grid_container = ce('div')
grid_container.id = 'scoreboard_grid'
grid_container.style.display = 'grid'
# Auto-wrap into 3 columns
grid_container.style.gridTemplateColumns = 'repeat(3, 1fr)' 
ba(grid_container)

####

# POPULATE THE DATA
for p in players:
    # The Outer Card (Flex Column)
    card = ce('div')
    card.style.display = 'flex'
    card.style.flexDirection = 'column'
    card.style.alignItems = 'center'
    card.style.backgroundColor = 'rgb(30, 30, 40)'
    card.style.border = '1px solid rgb(50, 50, 70)'
    card.style.borderRadius = '6px'
    ba(card, grid_container)

    # The Name Label
    name_lbl = ce('text')
    name_lbl.textContent = p["name"]
    name_lbl.style.color = 'rgb(0, 255, 200)'
    name_lbl.style.fontSize = '18px'
    name_lbl.style.fontWeight = 'bold'
    ba(name_lbl, card)

    # The Score Label
    score_lbl = ce('text')
    score_lbl.textContent = str(p["score"])
    score_lbl.style.color = 'white'
    score_lbl.style.fontSize = '24px'
    score_lbl.style.fontWeight = 'bold'
    ba(score_lbl, card)

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
```


</details>

---

<details>
<summary><b>Section: 045_grid_data_className</b></summary>


### `grid_data_className.py`

```python
# grid_data_className.py

from pyside6dom import *

init_window('Player Scoreboard', 700, 500)

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    
    #scoreboard_grid {
        background-color: rgb(15, 15, 18);
        border: 2px solid rgb(40, 40, 50);
        border-radius: 8px;
        padding: 15px;
        margin: 20px;
    }
    
    /* The Engine now utilizes the .class syntax */
    .player_card {
        background-color: rgb(30, 30, 40);
        border: 1px solid rgb(50, 50, 70);
        border-radius: 6px;
        padding: 15px;
    }
    
    /* We can even add Qt's built-in hover states */
    .player_card:hover {
        border: 1px solid rgb(0, 255, 200);
        background-color: rgb(40, 40, 50);
    }
    
    .player_name {
        color: rgb(0, 255, 200);
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 10px;
    }
    
    .player_score {
        color: white;
        font-size: 24px;
        font-weight: bold;
        text-align: center;
    }
""")

players = [
    {"name": "Jane", "score": 92},
    {"name": "Melissa", "score": 95},
    {"name": "Tabitha", "score": 93},
    {"name": "Christopher", "score": 90},
    {"name": "Alex", "score": 85},
    {"name": "Sarah", "score": 97}
]

grid = ce('div')
grid.id = 'scoreboard_grid' # Uses the #id CSS rule!
grid.style.display = 'grid'
grid.style.gridTemplateColumns = 'repeat(3, 1fr)' 
ba(grid)

# Look how clean this loop is now!
for p in players:
    card = ce('div')
    card.className = 'player_card'
    card.style.display = 'flex'
    card.style.flexDirection = 'column'
    card.style.alignItems = 'center'
    ba(card, grid)
    
    name_lbl = ce('text')
    name_lbl.className = 'player_name'
    name_lbl.textContent = p["name"]
    ba(name_lbl, card)
    
    score_lbl = ce('text')
    score_lbl.className = 'player_score'
    score_lbl.textContent = str(p["score"])
    #score_lbl.style.textAlign = 'center'
    ba(score_lbl, card)

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
```


</details>

---

<details>
<summary><b>Section: 048_div_append</b></summary>


### `div_append.py`

```python
# div_append.py

from pyside6dom import *

init_window('Our App', 400, 300)

# Use ba() to attach the main container to the window (just like document.body.append)
main_panel = ce('div')
ba(main_panel)

# attach our_title to the main_panel
our_title = ce('text')
our_title.textContent = "Welcome to the App"
main_panel.append(our_title) 

# attach hi_btn to the main_panel
hi_btn = ce('button')
hi_btn.textContent = "Click Me"
hi_btn.onclick = lambda: print('hi')
main_panel.append(hi_btn)

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
```


</details>

---

<details>
<summary><b>Section: 049_div_remove</b></summary>


### `div_remove.py`

```python
# div_remove.py

from pyside6dom import *

init_window('Our App', 400, 300)

# Use ba() to attach the main container to the window (just like document.body.append)
main_panel = ce('div')
ba(main_panel)

# attach our_title to the main_panel
our_title = ce('text')
our_title.textContent = "Welcome to the App"
main_panel.append(our_title) 

# attach hi_btn to the main_panel
# when clicked it removes our_title div
hi_btn = ce('button')
hi_btn.textContent = "Click Me"
hi_btn.onclick = lambda: our_title.remove()
main_panel.append(hi_btn)

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
```


</details>

---

<details>
<summary><b>Section: 050_div_textContent</b></summary>


### `div_textContent.py`

```python
# div_textContent.py

from pyside6dom import *

init_window('OurApp', 700, 600)

our_txt_div = ce('div')
our_txt_div.textContent = 'Howdy'
ba(our_txt_div)

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
```


</details>

---

<details>
<summary><b>Section: 051_div_innerHTML</b></summary>


### `div_innerHTML.py`

```python
# div_innerHTML.py

from pyside6dom import *

init_window('OurApp', 700, 600)

our_txt_div = ce('div')
our_txt_div.innerHTML = 'Howdy'
ba(our_txt_div)

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
```


</details>

---

<details>
<summary><b>Section: 052_growing_shrinking_div</b></summary>


### `growing_shrinking_div.py`

```python
# growing_shrinking_div.py

from pyside6dom import *

init_window('OurApp', 700, 600)

energy_bar = ce('div')
energy_bar.id = 'energy_bar'
energy_bar.style.border = '1px solid rgb(255, 255, 255)'
energy_bar.style.width = 100
energy_bar.style.height = 100
ba(energy_bar)

size_btn_container = ce('div')
size_btn_container.style.display = 'flex'
size_btn_container.style.flexDirection = 'row'
ba(size_btn_container)

shrink_btn = ce('button')
shrink_btn.textContent = 'Shrink'
def handle_shrink():
    energy_bar.width -= 1
shrink_btn.onclick = handle_shrink
size_btn_container.append(shrink_btn)

grow_btn = ce('button')
grow_btn.textContent = 'Grow'
def handle_grow():
    energy_bar.width += 1
grow_btn.onclick = handle_grow
size_btn_container.append(grow_btn)

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
```


</details>

---

<details>
<summary><b>Section: 053_move_div_left_right</b></summary>


### `move_div_left_right.py`

```python
# move_div_left_right.py

from pyside6dom import *

init_window('OurApp', 700, 600)

player = ce('div')
player.id = 'player'
player.style.border = '1px solid rgb(255, 255, 255)'
player.style.width = 100
player.style.height = 100
player.style.position = 'absolute'
player.style.left = 0
player.style.top = 100
ba(player)

move_btn_container = ce('div')
move_btn_container.style.display = 'flex'
move_btn_container.style.flexDirection = 'row'
ba(move_btn_container)

move_left_btn = ce('button')
move_left_btn.textContent = 'Left'
def move_left():
    player.style.left -= 1
move_left_btn.onclick = move_left
move_btn_container.append(move_left_btn)

move_right_btn = ce('button')
move_right_btn.textContent = 'Right'
def move_right():
    player.style.left += 1
move_right_btn.onclick = move_right
move_btn_container.append(move_right_btn)

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
```


</details>

---

<details>
<summary><b>Section: 054_append_to_list</b></summary>


### `append_to_list.py`

```python
# append_to_list.py

from pyside6dom import *

init_window('Append to List', 700, 600)

set_theme('''
    input {
        padding: 4px;
        font-family: Arial;
        font-size: 25px;
    }
''')

people = []

name_input = ce('input')
name_input.placeholder = 'Enter Name'
ba(name_input)

enter_btn = ce('button')
enter_btn.textContent = 'Enter'
def add_to_list():
    people.append(name_input.value)
    ge('output_txt').value = people
    name_input.value = ''
enter_btn.onclick = add_to_list
ba(enter_btn)

output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.style.fontSize = '40px'
ba(output_txt)

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
```


</details>

---

<details>
<summary><b>Section: 055_insert_entry_to_dictionary</b></summary>


### `insert_entry_to_dictionary.py`

```python
# insert_entry_to_dictionary.py

from pyside6dom import *

init_window('Append to List', 700, 600)

set_theme('''
    input {
        padding: 4px;
        font-family: Arial;
        font-size: 25px;
    }
''')

people = {}

name_input = ce('input')
name_input.placeholder = 'Enter Name'
ba(name_input)

enter_btn = ce('button')
enter_btn.textContent = 'Enter'
def add_to_dictionary():
    people[name_input.value] = 'Online'
    ge('output_txt').value = people
    name_input.value = ''
    name_input.focus()
enter_btn.onclick = add_to_dictionary
ba(enter_btn)

name_input.onenter = add_to_dictionary

output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.style.fontSize = '40px'
ba(output_txt)

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
```


</details>

---

<details>
<summary><b>Section: 056_list_of_dictionaries</b></summary>


### `list_of_dictionaries.py`

```python
# list_of_dictionaries.py

from pyside6dom import *

init_window('List of Dictionaries (lod)', 700, 600)

set_theme('''
    input {
        padding: 6px;
        font-family: Arial;
        font-size: 20px;
        margin-right: 10px;
    }
    button {
        padding: 6px 15px;
        font-size: 20px;
        background-color: rgb(0, 150, 200);
        color: white;
        border-radius: 4px;
    }
''')

# we make an empty list
people = []

# Input: Name
name_input = ce('input')
name_input.placeholder = 'Enter Name'
ba(name_input)

# Input: Role
role_input = ce('input')
role_input.placeholder = 'Enter Role (e.g. Admin)'
ba(role_input)

enter_btn = ce('button')
enter_btn.textContent = 'Add Person'

def add_to_list():
    # Only add if they actually typed something!
    if name_input.value == '' or role_input.value == '':
        # If they hit enter while empty, remove focus (blur) so they know it failed
        name_input.blur() 
        role_input.blur()
        return

    # Create the "Object" (Dictionary)
    new_person = {
        "name": name_input.value,
        "role": role_input.value
    }
    
    # Push it to the list
    people.append(new_person)
    
    # Format it beautifully as a string with indents
    pretty_json = json.dumps(people, indent=4)
    ge('output_txt').value = pretty_json
    
    # Clear inputs and return focus
    name_input.value = ''
    role_input.value = ''
    #name_input.raw.setFocus()
    name_input.focus()

enter_btn.onclick = add_to_list
ba(enter_btn)

# Output Box
output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.style.marginTop = '15px'
output_txt.style.fontSize = '20px'
output_txt.style.height = '400px'
#output_txt.raw.setReadOnly(True)
output_txt.readOnly = 'true'
ba(output_txt)

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
```


</details>

---

<details>
<summary><b>Section: 057_how_many_in_list</b></summary>


### `how_many_in_list.py`

```python
# how_many_in_list.py

from pyside6dom import *

init_window('OurApp', 700, 600)

set_theme('''
    div {
        padding: 2px 5px;
        font-family: Arial;
        font-size: 40px;
        font-weight: bold;
    }
''')

people = [
    "Jane",
    "Joan",
    "Melissa",
    "Tabitha"
]

how_many_here = ce('div')
how_many_here.textContent = str(len(people)) + ' people are here'
ba(how_many_here)

who_is_here = ce('div')
who_is_here.textContent = people
ba(who_is_here)

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
```


</details>

---

<details>
<summary><b>Section: 058_class_inspect</b></summary>


### `class_inspect.py`

```python
# class_inspect.py

import inspect
from pyside6dom import *

init_window('Inspect DOMStyle File', 800, 600)

result_txt = ce('textarea')
result_txt.id = 'result_txt'
result_txt.style.fontSize = '24px' 
result_txt.style.fontFamily = 'Arial'
result_txt.style.width = '700'
result_txt.style.height = '500'
result_txt.style.backgroundColor = '#1e1e1e'
result_txt.style.color = '#569cd6'
#result_txt.raw.setReadOnly(True)
result_txt.readOnly = 'true'
ba(result_txt)

# Get the file path
our_query = inspect.getfile(DOMStyle)

# Read the file and populate the element
if os.path.isfile(our_query):
    with open(our_query, 'r') as file:
        content = file.read()
        result_txt.value = content 
else:
    result_txt.value = "File not found."

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
```


</details>

---

<details>
<summary><b>Section: 059_class_inspect_DOMStyle</b></summary>


### `class_inspect_DOMStyle.py`

```python
# class_inspect_DOMStyle.py

import inspect
from pyside6dom import *

init_window('Class Inspector', 800, 600)

# Create the UI
result_txt = ce('textarea')
result_txt.id = 'result_txt'
result_txt.style.fontSize = '24px' 
result_txt.style.fontFamily = 'Arial'
result_txt.style.width = '700'
result_txt.style.height = '500'
result_txt.style.backgroundColor = '#1e1e1e'
result_txt.style.color = '#569cd6'
#result_txt.raw.setReadOnly(True)
result_txt.readOnly = 'true'
ba(result_txt)

# Extract ONLY the target class
try:
    # This single line grabs the exact source code for the DOMStyle class
    class_code = inspect.getsource(DOMStyle)
    result_txt.value = class_code
except Exception as err:
    result_txt.value = f"Error extracting code: {err}"

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
```


</details>

---

<details>
<summary><b>Section: 060_inspect_XOR</b></summary>


### `inspect_XOR.py`

```python
# inspect_XOR.py

import inspect
from pyside6dom import *

init_window('Function Inspector', 800, 600)

# Create the UI
result_txt = ce('textarea')
result_txt.id = 'result_txt'
result_txt.style.fontSize = '24px' 
result_txt.style.fontFamily = 'Arial'
result_txt.style.width = '700'
result_txt.style.height = '500'
result_txt.style.backgroundColor = '#1e1e1e'
result_txt.style.color = '#569cd6'
#result_txt.raw.setReadOnly(True)
result_txt.readOnly = 'true'
ba(result_txt)

# Extract ONLY the target function
try:
    # This single line grabs the exact source code for the XOR function
    function_code = inspect.getsource(XOR)
    result_txt.value = function_code
except Exception as err:
    result_txt.value = f"Error extracting code: {err}"

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
```


</details>

---

<details>
<summary><b>Section: 061_list_of_dictionaries_onenter</b></summary>


### `list_of_dictionaries_onenter.py`

```python
# list_of_dictionaries_onenter.py

from pyside6dom import *

init_window('List of Dictionaries (lod)', 700, 600)

set_theme('''
    input {
        padding: 6px;
        font-family: Arial;
        font-size: 20px;
        margin-right: 10px;
    }
    button {
        padding: 6px 15px;
        font-size: 20px;
        background-color: rgb(0, 150, 200);
        color: white;
        border-radius: 4px;
    }
''')

# we make an empty list
people = []

# Input: Name
name_input = ce('input')
name_input.placeholder = 'Enter Name'
ba(name_input)

# Input: Role
role_input = ce('input')
role_input.placeholder = 'Enter Role (e.g. Admin)'
ba(role_input)

enter_btn = ce('button')
enter_btn.textContent = 'Add Person'

def add_to_list():
    # Only add if they actually typed something!
    if name_input.value == '' or role_input.value == '':
        # If they hit enter while empty, remove focus (blur) so they know it failed
        name_input.blur() 
        role_input.blur()
        return

    # Create the "Object" (Dictionary)
    new_person = {
        "name": name_input.value,
        "role": role_input.value
    }
    
    # Push it to the list
    people.append(new_person)
    
    # Format it beautifully as a string with indents
    pretty_json = json.dumps(people, indent=4)
    ge('output_txt').value = pretty_json
    
    # Clear inputs and return focus
    name_input.value = ''
    role_input.value = ''
    name_input.focus()

# The Button submits
enter_btn.onclick = add_to_list

# Hitting Enter on the Name box jumps the cursor to the Role box
name_input.onenter = role_input.focus 

# Hitting Enter on the Role box submits the data
role_input.onenter = add_to_list
ba(enter_btn)

# Output Box
output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.style.marginTop = '15px'
output_txt.style.fontSize = '20px'
output_txt.style.height = '400px'
output_txt.readOnly = 'true'
ba(output_txt)

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
```


</details>

---

<details>
<summary><b>Section: 062_password_generator</b></summary>


### `password_generator.py`

```python
# password_generator.py

from pyside6dom import *

init_window('Password Generator', 700, 600)

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

symbols = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')','_']

def generate_password():
    all = letters + numbers + symbols

    password = random.sample(all, 12)

    password_string = ", ".join(map(str, password))

    password = password_string.replace(",", "")    
    return password


password_div = ce('input')
password_div.value = generate_password()
password_div.style.fontSize = '30px'
password_div.style.fontWeight = 'bold'
password_div.readOnly = 'false'
ba(password_div)

random_password_btn = ce('button')
random_password_btn.textContent = 'Random'
def handle_click():
    password_div.value = generate_password()
random_password_btn.onclick = handle_click
ba(random_password_btn)

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
```


</details>

---

<details>
<summary><b>Section: 063_is_target_date</b></summary>


### `is_target_date.py`

```python
# is_target_date.py

from pyside6dom import *

init_window('OurApp', 700, 500)

result = ce('div')
result.textContent = dom.is_target_date('2026-10-05')
ba(result)

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
```


</details>

---

<details>
<summary><b>Section: 064_password_generator_with_length</b></summary>


### `password_generator_with_length.py`

```python
# password_generator_with_length.py

from pyside6dom import *
import random

init_window('Password Generator', 700, 600)

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('~!@#$%^&*()_')

def generate_password():
    all_chars = letters + numbers + symbols
    
    # Grab the length directly from the input box right now.
    try:
        current_length = int(password_length_input.value)
    except ValueError:
        current_length = 12 # Fallback if the user typed a letter by accident
        
    password_list = random.choices(all_chars, k=current_length)
    return "".join(map(str, password_list))

password_div = ce('input')
password_div.style.fontSize = '30px'
password_div.style.fontWeight = 'bold'
password_div.readOnly = True
ba(password_div)

password_length_input = ce('input')
password_length_input.value = 12 
ba(password_length_input)

# Boot up the first password AFTER the input box is created
password_div.value = generate_password()

random_password_btn = ce('button')
random_password_btn.textContent = 'Random'

def handle_click():
    # When clicked, generate_password() fires and immediately reads the new input value
    password_div.value = generate_password()

random_password_btn.onclick = handle_click
ba(random_password_btn)

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
```


</details>

---

<details>
<summary><b>Section: 065_password_generator_with_slider</b></summary>


### `password_generator_with_slider.py`

```python
# password_generator_with_slider.py

from pyside6dom import *
import random

init_window('Password Generator', 700, 600)

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('~!@#$%^&*()_')
all_chars = letters + numbers + symbols

def generate_password(length):
    password_list = random.choices(all_chars, k=int(length))
    return "".join(map(str, password_list))

# ===
# PASSWORD DISPLAY 
# ===
password_div = ce('input')
password_div.id = "password_display"
password_div.style("font-size: 30px; font-weight: bold;")
password_div.readOnly = True
ba(password_div)

# ===
# NUMBER INPUT BLOCK
# ===
password_length_input = ce('input')
password_length_input.id = "length_input"
password_length_input.value = "12"

def sync_from_input():
    try:
        current_val = int(ge("length_input").value)

        if current_val < 4: current_val = 4
        if current_val > 64: current_val = 64

        # MAP BACKWARD: Convert 4-64 scale into a 0.0-10.0 scale for the slider
        slider_target = ((current_val - 4) / 60.0) * 10.0
        
        ge("length_slider").value = slider_target
        ge("password_display").value = generate_password(current_val)
    except ValueError:
        pass 

password_length_input.oninput = sync_from_input
ba(password_length_input)

# ===
# SLIDER
# ===
length_slider = ce('slider')
length_slider.id = "length_slider"
# We don't try to set .min or .max here anymore, we accept the engine's 0-10 default

def sync_from_slider():
    # Grab the engine's raw 0.0 to 10.0 value
    raw_slider = float(ge("length_slider").value)
    
    # MAP FORWARD: Translate the 0-10 position into a 4-64 character length
    percentage = raw_slider / 10.0
    current_val = int(4 + (percentage * 60))
    
    ge("length_input").value = current_val
    ge("password_display").value = generate_password(current_val)

length_slider.oninput = sync_from_slider
ba(length_slider)

# ===
# RANDOM BUTTON BLOCK
# ===
random_btn = ce('button')
random_btn.id = "random_btn"
random_btn.textContent = "Random"

def handle_click():
    current_val = int(ge("length_input").value)
    ge("password_display").value = generate_password(current_val)

random_btn.onclick = handle_click
ba(random_btn)

# ===
# BOOT INITIALIZATION
# ===
# Set input to 12
ge("length_input").value = 12
# Set slider to the mathematical equivalent of 12 (which is 1.33 on the 0-10 scale)
ge("length_slider").value = ((12 - 4) / 60.0) * 10.0
# Generate initial password
ge("password_display").value = generate_password(12)

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
```


</details>

---

<details>
<summary><b>Section: 066_wasd_player_addEventListener</b></summary>


### `wasd_player_addEventListener.py`

```python
# wasd_player_addEventListener.py

from pyside6dom import *

init_window('WASD Player with addEventListener', 600, 600)

set_theme('''
    body { 
        background-color: rgb(30, 30, 30); 
        color: white; 
        font-family: Arial; 
    }
    .player_box {
        background-color: #00ffcc;
        border-radius: 8px;
        border: 2px solid white;
    }
    .control_btn {
        background-color: #555;
        color: white;
        padding: 10px;
        font-size: 16px;
        border-radius: 4px;
        font-weight: bold;
    }
''')

# ===
# STATE VARIABLES
# ===
player_x = 250
player_y = 250
speed = 25

# ===
# BUILD THE UI
# ===
# The UI wrapper for our controls
ui_layer = ce('div')
ui_layer.style.padding = 20
ba(ui_layer)

instruction_lbl = ce('h2')
instruction_lbl.textContent = "Use W, A, S, D to Move. Hit 'Enter' to reset."
ba(instruction_lbl, ui_layer)

reset_btn = ce('button')
reset_btn.className = 'control_btn'
reset_btn.textContent = 'Reset Position'
ba(reset_btn, ui_layer)

# The Player Cube (Absolute Positioned)
player = ce('div')
player.className = 'player_box'
player.style.position = 'absolute'
player.style.width = 50
player.style.height = 50
player.style.left = player_x
player.style.top = player_y
ba(player)

# ===
# LOGIC & EVENT SWITCHBOARD
# ===

def reset_position():
    global player_x, player_y
    player_x = 250
    player_y = 250
    player.style.left = player_x
    player.style.top = player_y

# FEATURE 1: Stacking Events on a single Element 
def hover_in(): 
    reset_btn.style.backgroundColor = '#ff0055'

def hover_out(): 
    reset_btn.style.backgroundColor = '#555'

# Notice how we stack three completely different listeners on ONE button!
# This is impossible with standard '.onclick'
reset_btn.addEventListener('click', reset_position)
reset_btn.addEventListener('mouseenter', hover_in)
reset_btn.addEventListener('mouseleave', hover_out)

# FEATURE 2: Global Window Keyboard Capture
def handle_keys(event):
    global player_x, player_y
    
    # We use event.key exactly like JavaScript
    key = event.key.lower()
    
    if key == 'w': player_y -= speed
    elif key == 's': player_y += speed
    elif key == 'a': player_x -= speed
    elif key == 'd': player_x += speed
    
    # We intercept your normalized 'Enter' key
    elif key == 'enter': 
        reset_position()
        return # Skip the movement logic
        
    # Apply the new coordinates to the engine
    player.style.left = player_x
    player.style.top = player_y

# Attach the keyboard listener to the whole window
window.addEventListener('keydown', handle_keys)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 067_anchor_hyperlink</b></summary>


### `anchor_hyperlink.py`

```python
# anchor_hyperlink.py

from pyside6dom import *

init_window('anchor hyperlink', 700, 600)

theTitle = ce('a')
theTitle.id = 'theTitle'
theTitle.href = 'https://github.com/ChristopherAndrewTopalian/CATopalian_NWJS_Add_to_Array'
theTitle.target = '_blank'
theTitle.textContent = 'CATopalian NWJS Add to Array'
theTitle.style.fontSize = '30px'
theTitle.style.fontWeight = 'bold'
theTitle.style.fontFamily = 'Arial'
theTitle.style.textDecoration = 'none'
theTitle.style.color = 'rgb(170, 170, 170)'
ba(theTitle)

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
```

### `anchor_hyperlink_css.py`

```python
# anchor_hyperlink_css.py

from pyside6dom import *

init_window('anchor hyperlink', 700, 600)

set_theme('''
    a {
        text-decoration: none;
    }
''')

theTitle = ce('a')
theTitle.id = 'theTitle'
theTitle.href = 'https://github.com/ChristopherAndrewTopalian/CATopalian_NWJS_Add_to_Array'
theTitle.target = '_blank'
theTitle.textContent = 'CATopalian NWJS Add to Array'
theTitle.style.fontSize = '30px'
theTitle.style.fontWeight = 'bold'
theTitle.style.fontFamily = 'Arial'
#theTitle.style.textDecoration = 'none'
theTitle.style.color = 'rgb(170, 170, 170)'
ba(theTitle)

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
```


</details>

---

<details>
<summary><b>Section: 068_append_to_list</b></summary>


### `append_to_list.py`

```python
# append_to_list.py

from pyside6dom import *

init_window('Append to List', 600, 500)

set_theme('''
    body {
        background-color: rgb(30, 30, 30); color: white; font-family: Arial; padding: 24px;
    }
    input, textarea {
        background-color: #222;
        color: #00ffcc;
        border: 1px solid #555;
        padding: 5px; font-size: 22px;
    }
    button {
        background-color: rgb(0, 150, 200); color: white; font-size: 16px; padding: 5px 15px;
        border-radius: 4px;
    }
''')

people = []

# ---
# THE TITLE
# ---
theTitle = ce('a')
theTitle.id = 'theTitle'
theTitle.href = 'https://github.com/ChristopherAndrewTopalian/pyside6dom'
theTitle.target = '_blank'
theTitle.textContent = 'pyside6dom'
theTitle.style.fontSize = '20px'
theTitle.style.fontWeight = 'bold'
theTitle.style.textDecoration = 'none'
theTitle.style.color = 'rgb(170, 170, 170)'
ba(theTitle)

# An empty div to act like an <hr> or <br>
spacer = ce('div')
spacer.style.height = '20px'
ba(spacer)

# ---
# THE INPUT SANDWICH
# ---
name_input = ce('input')
name_input.id = 'name_input'
name_input.placeholder = 'Enter Name'

def _(event):
    if event.key == 'Enter':
        event.preventDefault()
        # We use ge() to find the button because it hasn't been drawn yet!
        # .click() perfectly mimics the JS button.click() function
        ge('enter_btn').click()
        
name_input.addEventListener('keydown', _)
ba(name_input)

spacer2 = ce('div')
spacer2.style.height = '20px'
ba(spacer2)

# ---
# THE BUTTON
# ---
enter_btn = ce('button')
enter_btn.id = 'enter_btn' # Assign the ID so the input above can find it!
enter_btn.textContent = 'Enter'

def _():
    if name_input.value.strip() == '': return # Prevent empty clicks
    
    people.append(name_input.value)
    ge('output_txt').value = json.dumps(people, indent=2)
    name_input.value = ''
    name_input.focus()
    
enter_btn.onclick = _
ba(enter_btn)

spacer3 = ce('div')
spacer3.style.height = '20px'
ba(spacer3)

# ---
# THE OUTPUT
# ---
output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.readOnly = True
output_txt.style.width = '400px'
output_txt.style.height = '200px'
ba(output_txt)

# Auto-focus the input when the app launches
name_input.focus()

run_app()

####

'''
We use _ as our 'anon function' style, but we can choose any name we want, such as:
handle_click or something like that.
We can use the same name over and over, without conflict.
'''

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
```


</details>

---

<details>
<summary><b>Section: 072_types_of_clicks</b></summary>


### `types_of_clicks.py`

```python
# types_of_clicks.py

from pyside6dom import *

init_window('Types of Clicks', 700, 600)

howdy_btn = ce('button')
howdy_btn.textContent = 'Howdy'
howdy_btn.onclick = lambda: print('Left Click')
howdy_btn.oncontextmenu = lambda: print('Right Click')
howdy_btn.onauxclick = lambda: print('Middle Button Click')
ba(howdy_btn)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 073_types_of_clicks_easy_names</b></summary>


### `types_of_clicks_easy_names.py`

```python
# types_of_clicks_easy_names.py

from pyside6dom import *

init_window('Types of Clicks with Easy Names', 700, 600)

howdy_btn = ce('button')
howdy_btn.textContent = 'Howdy'
howdy_btn.onleftclick = lambda: print('Left Click')
howdy_btn.onrightclick = lambda: print('Right Click')
howdy_btn.onmiddleclick = lambda: print('Middle Button Click')
ba(howdy_btn)

run_app()

####

'''
we can say onclick or onleftclick
we can say oncontextmenu or onrightclick
we can say onauxclick or onmiddleclick
'''

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
```


</details>

---

<details>
<summary><b>Section: 074_title_attribute</b></summary>


### `title_attribute.py`

```python
# title_attribute.py

from pyside6dom import *

init_window('Title Attribute', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Howdy'
howdy_btn.title = 'Click to see a message in console'
howdy_btn.onclick = lambda: print('Howdy')
ba(howdy_btn)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 075_title_attribute_titleFontSize</b></summary>


### `title_attribute_titleFontSize.py`

```python
# title_attribute_titleFontSize.py

from pyside6dom import *

init_window('Title Attribute titleFontSize', 700, 500)

howdy_btn = ce('button')
howdy_btn.textContent = 'Howdy'
howdy_btn.title = 'Click to see a message in console'
howdy_btn.titleFontSize = "24px"
howdy_btn.onclick = lambda: print('Howdy')
ba(howdy_btn)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 076_notebook</b></summary>


### `notebook.py`

```python
# notebook.py

from pyside6dom import *

init_window('Notebook', 700, 600)

output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.placeholder = 'Type Here'
output_txt.style.fontSize = '24px'
ba(output_txt)

save_btn = ce('button')
save_btn.textContent = 'Save'
def q():
    with open("our_notes.txt", "a", encoding="utf-8") as file:
        file.write(output_txt.value + '\n')
save_btn.onclick = q
ba(save_btn)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 077_notebook_read_and_write</b></summary>


### `notebook_read_and_write.py`

```python
# notebook_read_and_write.py

from pyside6dom import *

init_window('Notebook', 700, 600)

output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.placeholder = 'Type Here'
output_txt.style.fontSize = '24px'
output_txt.style.backgroundColor = 'rgb(30, 30, 30)'
output_txt.style.color = 'rgb(255, 255, 255)'
ba(output_txt)

# Read the file on startup (if it exists) to populate the textarea
if os.path.exists("our_notes.txt"):
    with open("our_notes.txt", "r", encoding="utf-8") as file:
        output_txt.value = file.read()

save_btn = ce('button')
save_btn.textContent = 'Save'

# Overwrite the file with the complete, updated textarea value
def q():
    with open("our_notes.txt", "w", encoding="utf-8") as file:
        file.write(output_txt.value)
save_btn.onclick = q
ba(save_btn)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 078_notebook_read_write_name</b></summary>


### `notebook_read_write_name.py`

```python
# notebook_read_write_name.py

import os
from pyside6dom import *

init_window('Notebook', 700, 650)

# The Filename Input
file_input = ce('input')
file_input.value = 'our_notes.txt'  # Default filename
file_input.style.fontSize = '20px'
file_input.style.marginBottom = '10px'
file_input.style.marginRight = '10px'
ba(file_input)

# The Load Button
load_btn = ce('button')
load_btn.textContent = 'Load File'
ba(load_btn)

# The Text Area
output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.placeholder = 'Type Here'
output_txt.style.fontSize = '24px'
output_txt.style.backgroundColor = 'rgb(30, 30, 30)'
output_txt.style.color = 'rgb(255, 255, 255)'
output_txt.style.height = '450px'
output_txt.style.marginTop = '10px'
ba(output_txt)

# The Save Button
save_btn = ce('button')
save_btn.textContent = 'Save'
save_btn.style.marginTop = '10px'
ba(save_btn)

# The Status Message Label (Starts empty)
status_lbl = ce('label')
status_lbl.textContent = ''
status_lbl.style.marginLeft = '15px'
status_lbl.style.color = 'rgb(0, 255, 150)' # A nice neon green
status_lbl.style.fontSize = '18px'
ba(status_lbl)

# Application Logic

def load_file():
    filename = file_input.value
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            output_txt.value = file.read()
        status_lbl.textContent = f"Loaded '{filename}' successfully."
    else:
        output_txt.value = ""
        status_lbl.textContent = f"Ready to create new file: '{filename}'"

# Run load_file once on startup to grab the default file
load_file()
load_btn.onclick = load_file

def save_file():
    filename = file_input.value
    with open(filename, "w", encoding="utf-8") as file:
        file.write(output_txt.value)
    status_lbl.textContent = f"Saved to '{filename}'!"

save_btn.onclick = save_file

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 079_wasd_keydown</b></summary>


### `wasd_keydown.py`

```python
# wasd_keydown.py

from pyside6dom import *

init_window('Our App', 700, 600)

output_txt = ce('div')
output_txt.id = 'output_txt'
output_txt.textContent = 'output'
output_txt.style.fontSize = '50px'
ba(output_txt)

def handle_keys(event):
    key = event.key.lower()

    if key == 'w':
        output_txt.textContent = 'w pressed'
    elif key == 's':
        output_txt.textContent = 's pressed'
    elif key == 'a':
        output_txt.textContent = 'a pressed'
    elif key == 'd':
        output_txt.textContent = 'd pressed'


# Attach the keyboard listener to the whole window
window.addEventListener('keydown', handle_keys)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 080_notebook_files_from_folder</b></summary>


### `notebook_files_from_folder.py`

```python
# notebook_files_from_folder.py

import os
from pyside6dom import *

TEXT_DIR = 'text'
if not os.path.exists(TEXT_DIR):
    os.makedirs(TEXT_DIR)

init_window('Notebook Opens Files in Text Folder', 900, 650)
current_file = ""

# Layout Containers
main_container = ce('div')
main_container.style.display = 'flex'
main_container.style.flexDirection = 'row'
main_container.style.height = '600px'
ba(main_container)

sidebar = ce('scroll_div') 
sidebar.style.width = '250px'
sidebar.style.height = '500px'
sidebar.style.backgroundColor = 'rgb(40, 40, 40)'
sidebar.style.padding = '10px'
main_container.append(sidebar)

editor_panel = ce('div')
editor_panel.style.padding = '10px'
main_container.append(editor_panel)

# Editor Panel UI
status_lbl = ce('label')
status_lbl.textContent = 'Select a file to edit...'
status_lbl.style.color = 'rgb(0, 255, 150)'
status_lbl.style.fontSize = '18px'
editor_panel.append(status_lbl)

output_txt = ce('textarea')
output_txt.id = 'output_txt'
output_txt.style.width = '600px'
output_txt.style.height = '500px'
output_txt.style.marginTop = '10px'
output_txt.style.fontSize = '20px'
output_txt.style.backgroundColor = 'rgb(30, 30, 30)'
output_txt.style.color = 'rgb(255, 255, 255)'
editor_panel.append(output_txt)

save_btn = ce('button')
save_btn.textContent = 'Save Current File'
save_btn.style.marginTop = '10px'
save_btn.style.fontSize = '18px'
editor_panel.append(save_btn)

# Application Logic
def load_file(filename):
    global current_file
    current_file = filename
    filepath = os.path.join(TEXT_DIR, filename)

    with open(filepath, "r", encoding="utf-8") as file:
        output_txt.value = file.read()

    status_lbl.textContent = f"Editing: {filename}"

def save_file():
    if current_file == "":
        status_lbl.textContent = "No file selected!"
        return

    filepath = os.path.join(TEXT_DIR, current_file)
    with open(filepath, "w", encoding="utf-8") as file:
        file.write(output_txt.value)

    status_lbl.textContent = f"Saved: {current_file}!"

save_btn.onclick = save_file

# Dynamic Sidebar Generation
def build_sidebar():
    sidebar.innerHTML = "" 

    title = ce('h3')
    title.textContent = 'My Files'
    title.style.color = 'white'
    sidebar.append(title)

    all_files = os.listdir(TEXT_DIR)
    text_files = [f for f in all_files if f.endswith('.txt')]
    
    for filename in text_files:
        btn = ce('button')
        btn.textContent = filename
        btn.style.marginBottom = '5px'
        btn.onclick = lambda f=filename: load_file(f)
        sidebar.append(btn)

build_sidebar()

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 081_width_height_percentage</b></summary>


### `width_height_percentage.py`

```python
# width_height_percentage.py

from pyside6dom import *

init_window('width height percentage', 700, 600)

our_div = ce('div')
our_div.style.border = '1px solid rgb(255, 255, 255)'
our_div.style.width = '100%'
our_div.style.height = '100%'
our_div.style.backgroundColor = 'rgb(0, 100, 100)'
ba(our_div)

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 082_width_height_percentage_bottom_right</b></summary>


### `width_height_percentage_bottom_right.py`

```python
# width_height_percentage_bottom_right.py

from pyside6dom import *

init_window('CATopalian Responsive Engine Test', 800, 600)

set_theme('''
    body {
        background-color: #1e1e1e;
        margin: 0px;
        padding: 0px;
    }
    
    .hero_panel {
        background-color: #2d2d30;
        border: 2px solid #00ffcc;
    }
    
    .floating_btn {
        background-color: #ff3333;
        color: white;
        font-weight: bold;
        font-size: 16px;
        border-radius: 25px; /* Rounded pill button */
        border: 2px solid white;
    }
    
    .floating_btn:hover {
        background-color: #ff6666;
    }
''')

# ===
# The 100% Fluid Container
# ===
hero = ce('div')
hero.className = 'hero_panel'
# These will now dynamically recalculate on every window resize
hero.style.width = '100%'
hero.style.height = '100%'
ba(hero)

title = ce('h1')
title.textContent = "Responsive Layouts in PySide6DOM"
title.style.color = "white"
title.style.padding = "40px"
hero.append(title)

# ===
# The Bottom-Right Floating Button
# ===
help_btn = ce('button')
help_btn.className = 'floating_btn'
help_btn.textContent = "💬 Help"

help_btn.style.position = 'absolute'
help_btn.style.width = '120px'
help_btn.style.height = '50px'

# Pin it exactly 20 pixels away from the bottom and right edges
help_btn.style.bottom = '20px'
help_btn.style.right = '20px'
ba(help_btn)

def clicked_help():
    title.textContent = "You clicked the floating button!"
    title.style.color = "#00ffcc"
    
help_btn.onclick = clicked_help

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 083_overflow_hidden</b></summary>


### `overflow_hidden.py`

```python
# overflow_hidden.py

from pyside6dom import *

init_window('CATopalian Overflow Test', 500, 600)

set_theme('''
    body {
        background-color: rgb(0, 50, 50); 
        padding: 20px;
        font-family: 'Segoe UI', Arial; 
        color: white;
    }
    
    .viewport {
        border: 3px solid #00ffcc;
        background-color: rgb(0, 50, 50);
    }
    
    .giant_content {
        background-color: rgb(0, 50, 50);
        font-size: 24px;
        font-weight: bold;
        padding: 20px;
    }
    
    button {
        background-color: rgb(0, 0, 0);
        color: white;
        padding: 10px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 5px;
        border: 2px solid white;
        margin-bottom: 20px;
    }
    button:hover {
        background-color: #555; 
        border-color: #00ffcc;
    }
''')

# ===
# The Toggle Button
# ===
toggle_btn = ce('button')
toggle_btn.textContent = "State: overflow: hidden 👁️"
ba(toggle_btn)

# ===
# The Restricted Container (400x400)
# ===
box = ce('scroll_div')
box.className = 'viewport'
box.style.width = '400px'
box.style.height = '400px'
# Start with scrollbars hidden
box.style.overflow = 'hidden' 
ba(box)

# ===
# The Giant Content (800x800)
# ===
giant = ce('div')
giant.className = 'giant_content'
giant.style.width = '800px'
giant.style.height = '800px'
giant.textContent = "Top Left Corner... (Scroll to see more!)"
box.append(giant)

marker = ce('text')
marker.textContent = "Bottom Right Corner!"
marker.style.position = 'absolute'
marker.style.right = '20px'
marker.style.bottom = '20px'
giant.append(marker)

# ===
# The Real-Time Toggle Logic
# ===
def toggle_overflow():
    if box.style.overflow == 'hidden':
        box.style.overflow = 'auto'
        toggle_btn.textContent = "State: overflow: auto (Scrollbars ON)"
        toggle_btn.style.borderColor = "rgb(0, 150, 150)"
    else:
        box.style.overflow = 'hidden'
        toggle_btn.textContent = "State: overflow: hidden (Scrollbars OFF)"
        toggle_btn.style.borderColor = "white"

toggle_btn.onclick = toggle_overflow

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
#
# Google Sites: https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 001_pyside6dom_modular</b></summary>


### `app.py`

```python
# app.py

# Import the custom DOM engine
from pyside6dom import ce, ge, ba, init_window, run_app

# Initialize the App
init_window("Command Center", width=440, height=520)

# Create a Header
header = ce("text")
header.id = "main_heading"
header.textContent = "Telemetry Link Online"
header.style("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
ba(header)

# Create an Input
command_input = ce("input")
command_input.id = "user_input"
command_input.placeholder = "Enter station parameter..."
ba(command_input)

# Create a Float Slider
frequency_slider = ce("slider")
frequency_slider.id = "freq_ctrl"
frequency_slider.value = 5.0

def handle_slider(val):
    target = ge("status_display")
    if target:
        target.textContent = f"Current Frequency: {val:.1f} MHz"

frequency_slider.oninput = handle_slider
ba(frequency_slider)

# Status Output Text
status_label = ce("text")
status_label.id = "status_display"
status_label.textContent = "Current Frequency: 5.0 MHz"
status_label.style("color: #76c7c0; margin-top: 5px;")
ba(status_label)

# Create a Button
submit_btn = ce("button")
submit_btn.id = "transmit_btn"
submit_btn.textContent = "Transmit Command"

def handle_click():
    txt = ge("user_input").value
    freq = ge("freq_ctrl").value
    ge("status_display").textContent = f"Transmitted: '{txt}' at {freq:.1f} MHz"

submit_btn.onclick = handle_click
ba(submit_btn)

# Launch
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
```

### `pyside6dom.py`

```python
# pyside6dom.py

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, 
    QLineEdit, QLabel, QSlider, QScrollArea
)
from PySide6.QtCore import Qt

_dom_registry = {}
_app_instance = None
_root_window = None
_main_container = None

class DOMElement:
    def __init__(self, tag, qt_widget):
        self.tag = tag
        self.raw = qt_widget
        self._id = ""
        self._children = []

    @property
    def id(self): return self._id

    @id.setter
    def id(self, value):
        self._id = value
        _dom_registry[value] = self

    @property
    def textContent(self):
        if hasattr(self.raw, "text"): return self.raw.text()
        return ""

    @textContent.setter
    def textContent(self, value):
        if hasattr(self.raw, "setText"): self.raw.setText(str(value))

    @property
    def value(self):
        if isinstance(self.raw, QLineEdit): return self.raw.text()
        elif isinstance(self.raw, QSlider): return self.raw.value() / 10.0
        return None

    @value.setter
    def value(self, val):
        if isinstance(self.raw, QLineEdit): self.raw.setText(str(val))
        elif isinstance(self.raw, QSlider): self.raw.setValue(int(float(val) * 10))

    @property
    def placeholder(self):
        return self.raw.placeholderText() if hasattr(self.raw, "placeholderText") else ""

    @placeholder.setter
    def placeholder(self, text):
        if hasattr(self.raw, "setPlaceholderText"): self.raw.setPlaceholderText(str(text))

    @property
    def onclick(self): return None

    @onclick.setter
    def onclick(self, callback_func):
        if hasattr(self.raw, "clicked"): self.raw.clicked.connect(callback_func)

    @property
    def oninput(self): return None

    @oninput.setter
    def oninput(self, callback_func):
        if isinstance(self.raw, QLineEdit):
            self.raw.textChanged.connect(lambda text: callback_func(text))
        elif isinstance(self.raw, QSlider):
            self.raw.valueChanged.connect(lambda val: callback_func(val / 10.0))

    def style(self, css_string):
        self.raw.setStyleSheet(css_string)


def ce(tag):
    tag = tag.lower()
    if tag == "button":
        w = QPushButton()
        w.setStyleSheet("padding: 8px 14px; background-color: #2b2b2b; color: white; border-radius: 4px;")
        return DOMElement(tag, w)
    elif tag in ("text", "p", "span", "h1"):
        w = QLabel()
        w.setStyleSheet("color: #ffffff; font-size: 14px;")
        return DOMElement(tag, w)
    elif tag == "input":
        w = QLineEdit()
        w.setStyleSheet("padding: 6px; background-color: #1a1a1a; color: white; border: 1px solid #444;")
        return DOMElement(tag, w)
    elif tag == "slider":
        w = QSlider(Qt.Orientation.Horizontal)
        w.setMinimum(0)
        w.setMaximum(100)
        return DOMElement(tag, w)
    elif tag == "div":
        w = QWidget()
        layout = QVBoxLayout(w)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(5, 5, 5, 5)
        elem = DOMElement(tag, w)
        elem.layout = layout
        return elem
    elif tag == "scroll_div":
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setWidget(content)
        elem = DOMElement(tag, scroll)
        elem.layout = layout
        return elem
    raise ValueError(f"Unknown tag: {tag}")

def ge(element_id):
    return _dom_registry.get(element_id, None)

def ba(child, parent=None):
    target = parent if parent is not None else _main_container
    if hasattr(target, "layout") and target.layout is not None:
        target.layout.addWidget(child.raw)
    elif isinstance(target, QVBoxLayout):
        target.addWidget(child.raw)

def init_window(title="App Window", width=420, height=500):
    global _app_instance, _root_window, _main_container
    _app_instance = QApplication(sys.argv)
    _app_instance.setStyle("Fusion")
    _root_window = QWidget()
    _root_window.setWindowTitle(title)
    _root_window.resize(width, height)
    _root_window.setStyleSheet("background-color: rgb(30, 30, 30);")
    _main_layout = QVBoxLayout(_root_window)
    _main_container = ce("scroll_div")
    _main_layout.addWidget(_main_container.raw)

def run_app():
    _root_window.show()
    sys.exit(_app_instance.exec())

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
```


</details>

---

<details>
<summary><b>Section: 002_pyside6dom_single_file</b></summary>


### `catopalian_py_pyside6_pyside6dom.py`

```python
# catopalian_py_pyside6_pyside6dom.py

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, 
    QLineEdit, QLabel, QSlider, QScrollArea
)
from PySide6.QtCore import Qt

# ----
# CORE DOM BRIDGE LAYER
# ----

_dom_registry = {}
_app_instance = None
_root_window = None
_main_container = None

class DOMElement:
    """Wrapper that translates standard DOM properties to PySide6 Qt methods."""
    def __init__(self, tag, qt_widget):
        self.tag = tag
        self.raw = qt_widget  # The underlying PySide6 widget
        self._id = ""
        self._children = []

    # Property: id
    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value
        _dom_registry[value] = self

    # Property: textContent
    @property
    def textContent(self):
        if hasattr(self.raw, "text"):
            return self.raw.text()
        return ""

    @textContent.setter
    def textContent(self, value):
        if hasattr(self.raw, "setText"):
            self.raw.setText(str(value))

    # Property: value (for inputs and sliders)
    @property
    def value(self):
        if isinstance(self.raw, QLineEdit):
            return self.raw.text()
        elif isinstance(self.raw, QSlider):
            return self.raw.value() / 10.0  # Decimals supported
        return None

    @value.setter
    def value(self, val):
        if isinstance(self.raw, QLineEdit):
            self.raw.setText(str(val))
        elif isinstance(self.raw, QSlider):
            self.raw.setValue(int(float(val) * 10))

    # Property: placeholder
    @property
    def placeholder(self):
        return self.raw.placeholderText() if hasattr(self.raw, "placeholderText") else ""

    @placeholder.setter
    def placeholder(self, text):
        if hasattr(self.raw, "setPlaceholderText"):
            self.raw.setPlaceholderText(str(text))

    # Event: onclick
    @property
    def onclick(self):
        return None

    @onclick.setter
    def onclick(self, callback_func):
        if hasattr(self.raw, "clicked"):
            self.raw.clicked.connect(callback_func)

    # Event: onchange / oninput
    @property
    def oninput(self):
        return None

    @oninput.setter
    def oninput(self, callback_func):
        if isinstance(self.raw, QLineEdit):
            self.raw.textChanged.connect(lambda text: callback_func(text))
        elif isinstance(self.raw, QSlider):
            self.raw.valueChanged.connect(lambda val: callback_func(val / 10.0))

    # Method: style
    def style(self, css_string):
        self.raw.setStyleSheet(css_string)


# ----
# HELPER FUNCTIONS (ce, ge, ba)
# ----

def ce(tag):
    """Create Element: ce('button'), ce('div'), ce('input'), ce('slider'), ce('text')"""
    tag = tag.lower()
    if tag == "button":
        w = QPushButton()
        w.setStyleSheet("padding: 8px 14px; background-color: #2b2b2b; color: white; border-radius: 4px;")
        return DOMElement(tag, w)
    
    elif tag in ("text", "p", "span", "h1"):
        w = QLabel()
        w.setStyleSheet("color: #ffffff; font-size: 14px;")
        return DOMElement(tag, w)
        
    elif tag == "input":
        w = QLineEdit()
        w.setStyleSheet("padding: 6px; background-color: #1a1a1a; color: white; border: 1px solid #444;")
        return DOMElement(tag, w)
        
    elif tag == "slider":
        w = QSlider(Qt.Orientation.Horizontal)
        w.setMinimum(0)
        w.setMaximum(100) # 0.0 to 10.0
        return DOMElement(tag, w)
        
    elif tag == "div":
        w = QWidget()
        layout = QVBoxLayout(w)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        layout.setContentsMargins(5, 5, 5, 5)
        elem = DOMElement(tag, w)
        elem.layout = layout
        return elem
        
    elif tag == "scroll_div":
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        content = QWidget()
        layout = QVBoxLayout(content)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        scroll.setWidget(content)
        elem = DOMElement(tag, scroll)
        elem.layout = layout
        return elem

    raise ValueError(f"Unknown tag: {tag}")


def ge(element_id):
    """Get Element by ID: ge('my_button')"""
    return _dom_registry.get(element_id, None)


def ba(child, parent=None):
    """Body Append / Append Child: ba(child) or ba(child, parent)"""
    target = parent if parent is not None else _main_container
    
    if hasattr(target, "layout") and target.layout is not None:
        target.layout.addWidget(child.raw)
    elif isinstance(target, QVBoxLayout):
        target.addWidget(child.raw)


def init_window(title="App Window", width=420, height=500):
    """Initializes the base dark window and body layout."""
    global _app_instance, _root_window, _main_container
    
    _app_instance = QApplication(sys.argv)
    _app_instance.setStyle("Fusion")
    
    _root_window = QWidget()
    _root_window.setWindowTitle(title)
    _root_window.resize(width, height)
    _root_window.setStyleSheet("background-color: rgb(30, 30, 30);")
    
    _main_layout = QVBoxLayout(_root_window)
    _main_container = ce("scroll_div")
    _main_layout.addWidget(_main_container.raw)


def run_app():
    """Starts the application loop."""
    _root_window.show()
    sys.exit(_app_instance.exec())


# ----
# MAIN APPLICATION
# ----

init_window("Command Center", width=440, height=520)

# Create a Header
header = ce("text")
header.id = "main_heading"
header.textContent = "Telemetry Link Online"
header.style("font-size: 18px; font-weight: bold; margin-bottom: 10px;")
ba(header)

# Create an Input
command_input = ce("input")
command_input.id = "user_input"
command_input.placeholder = "Enter station parameter..."
ba(command_input)

# Create a Float Slider (0.0 to 10.0 with 0.1 increments)
frequency_slider = ce("slider")
frequency_slider.id = "freq_ctrl"
frequency_slider.value = 5.0

def handle_slider(val):
    target = ge("status_display")
    if target:
        target.textContent = f"Current Frequency: {val:.1f} MHz"

frequency_slider.oninput = handle_slider
ba(frequency_slider)

# Status Output Text
status_label = ce("text")
status_label.id = "status_display"
status_label.textContent = "Current Frequency: 5.0 MHz"
status_label.style("color: #76c7c0; margin-top: 5px;")
ba(status_label)

# Create a Button
submit_btn = ce("button")
submit_btn.id = "transmit_btn"
submit_btn.textContent = "Transmit Command"

def handle_click():
    txt = ge("user_input").value
    freq = ge("freq_ctrl").value
    ge("status_display").textContent = f"Transmitted: '{txt}' at {freq:.1f} MHz"

submit_btn.onclick = handle_click
ba(submit_btn)

# Launch
run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 001_pyside6dom_example</b></summary>


### `pyside6dom_example.py`

```python
# pyside6dom_example.py

# after we have installed pyside6dom using
# pip install pyside6dom

from pyside6dom import *

# Initialize the Application
init_window("PySide6DOM Feature Showcase", width=450, height=650)

# Worldwide Header
header = ce("h1")
header.textContent = "🚀 Mission Control"
header.style("font-size: 24px; color: #00ffcc; font-weight: bold; margin-bottom: 20px;")
ba(header)

# Text Input with Real-Time 'oninput' Event
pilot_input = ce("input")
pilot_input.id = "pilot_name"
pilot_input.placeholder = "Enter Pilot Name..."
pilot_input.style("padding: 10px; font-size: 14px; border: 2px solid #555; border-radius: 5px;")
ba(pilot_input)

# Live feedback label for the input
typing_echo = ce("text")
typing_echo.id = "echo_label"
typing_echo.textContent = "Awaiting pilot identification..."
typing_echo.style("color: #aaaaaa; font-style: italic; margin-bottom: 20px;")
ba(typing_echo)

def on_type(text):
    ge("echo_label").textContent = f"Live typing: {text}"
pilot_input.oninput = on_type

# Slider with Real-Time 'oninput' Event
throttle_label = ce("text")
throttle_label.id = "throttle_display"
throttle_label.textContent = "Engine Throttle: 0%"
throttle_label.style("font-size: 16px; font-weight: bold; margin-top: 10px;")
ba(throttle_label)

throttle_slider = ce("slider")
throttle_slider.id = "throttle"
# The slider scales 0-100 under the hood based on our ce() setup
def on_slide(val):
    # val comes in as a float from our parser, we multiply back for display
    ge("throttle_display").textContent = f"Engine Throttle: {int(val * 10)}%"
throttle_slider.oninput = on_slide
ba(throttle_slider)

# Nested Containers (Div) for layout grouping
action_panel = ce("div")
action_panel.style("background-color: #222; border-radius: 8px; padding: 15px; margin-top: 20px;")
ba(action_panel)

# Interactive Button with rich CSS pseudo-states inside the Div
submit_btn = ce("button")
submit_btn.textContent = "ENGAGE THRUSTERS"
submit_btn.style("""
    QPushButton { 
        background-color: #007acc; 
        color: white; 
        border-radius: 6px; 
        padding: 12px; 
        font-size: 16px; 
        font-weight: bold;
    }
    QPushButton:hover { background-color: #0099ff; }
    QPushButton:pressed { background-color: #005c99; }
""")
ba(submit_btn, action_panel) # Appended to action_panel, NOT the main window

# Scrolling Log Window (scroll_div) for dynamic output
log_title = ce("h1")
log_title.textContent = "System Logs:"
log_title.style("margin-top: 20px; font-size: 14px; color: #888;")
ba(log_title)

log_window = ce("scroll_div")
log_window.style("background-color: #0a0a0a; border: 1px solid #333; min-height: 150px;")
ba(log_window)

# Button Click Event (Gathering data via 'ge' and appending to scroll_div)
def handle_engage():
    # Grab values from the registry
    pilot = ge("pilot_name").value or "Unknown Pilot"
    throttle = ge("throttle").value * 10

    # Create a new dynamic log entry
    log_entry = ce("p")
    log_entry.textContent = f"> {pilot} engaged engines at {int(throttle)}%"
    log_entry.style("color: #00ff00; font-family: monospace; font-size: 13px; margin: 2px;")

    # Append the new text directly into the scrolling window
    ba(log_entry, log_window)

submit_btn.onclick = handle_engage

# Launch the App
run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

### `inline_css_example_local_testing.py`

```python
# inline_css_example_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

# Initialize the Application
init_window("PySide6DOM Feature Showcase", 450, 650)

# Worldwide Header
header = ce("h1")
header.textContent = "🚀 Mission Control"
header.style("font-size: 24px; color: #00ffcc; font-weight: bold; margin-bottom: 20px;")
ba(header)

# Text Input with Real-Time 'oninput' Event
pilot_input = ce("input")
pilot_input.id = "pilot_name"
pilot_input.placeholder = "Enter Pilot Name..."
pilot_input.style("padding: 10px; font-size: 14px; border: 2px solid #555; border-radius: 5px;")
ba(pilot_input)

# Live feedback label for the input
typing_echo = ce("text")
typing_echo.id = "echo_label"
typing_echo.textContent = "Awaiting pilot identification..."
typing_echo.style("color: #aaaaaa; font-style: italic; margin-bottom: 20px;")
ba(typing_echo)

def on_type(text):
    ge("echo_label").textContent = f"Live typing: {text}"
pilot_input.oninput = on_type

# Slider with Real-Time 'oninput' Event
throttle_label = ce("text")
throttle_label.id = "throttle_display"
throttle_label.textContent = "Engine Throttle: 0%"
throttle_label.style("font-size: 16px; font-weight: bold; margin-top: 10px;")
ba(throttle_label)

throttle_slider = ce("slider")
throttle_slider.id = "throttle"
# The slider scales 0-100 under the hood based on our ce() setup
def on_slide(val):
    # val comes in as a float from our parser, we multiply back for display
    ge("throttle_display").textContent = f"Engine Throttle: {int(val * 10)}%"
throttle_slider.oninput = on_slide
ba(throttle_slider)

# Nested Containers (Div) for layout grouping
action_panel = ce("div")
action_panel.style("background-color: #222; border-radius: 8px; padding: 15px; margin-top: 20px;")
ba(action_panel)

# Interactive Button with rich CSS pseudo-states inside the Div
submit_btn = ce("button")
submit_btn.textContent = "ENGAGE THRUSTERS"
submit_btn.style("""
    button { 
        background-color: rgb(0, 0, 0); 
        color: white; 
        border-radius: 6px; 
        padding: 12px; 
        font-size: 16px; 
        font-weight: bold;
    }
    button:hover { background-color: rgb(0, 180, 180); }
    button:pressed { background-color: rgb(255, 255, 255); }
""")
ba(submit_btn, action_panel) # Appended to action_panel, NOT the main window

# Scrolling Log Window (scroll_div) for dynamic output
log_title = ce("h1")
log_title.textContent = "System Logs:"
log_title.style("margin-top: 20px; font-size: 14px; color: #888;")
ba(log_title)

log_window = ce("scroll_div")
log_window.style("background-color: #0a0a0a; border: 1px solid #333; min-height: 150px;")
ba(log_window)

# Button Click Event (Gathering data via 'ge' and appending to scroll_div)
def handle_engage():
    # Grab values from the registry
    pilot = ge("pilot_name").value or "Unknown Pilot"
    throttle = ge("throttle").value * 10

    # Create a new dynamic log entry
    log_entry = ce("p")
    log_entry.textContent = f"> {pilot} engaged engines at {int(throttle)}%"
    log_entry.style("color: #00ff00; font-family: monospace; font-size: 13px; margin: 2px;")

    # Append the new text directly into the scrolling window
    ba(log_entry, log_window)

submit_btn.onclick = handle_engage

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
```


</details>

---

<details>
<summary><b>Section: 009_pyside6dom_setInterval_clock</b></summary>


### `pyside6dom_example_local_testing.py`

```python
# pyside6dom_example_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *
from datetime import datetime

init_window("Digital Clock Test", 400, 200)

clock_label = ce('h1')
clock_label.style("font-size: 60px; font-weight: bold; color: rgb(0, 255, 255); qproperty-alignment: AlignCenter; margin-top: 20px;")
ba(clock_label)

date_label = ce('text')
date_label.style("font-size: 24px; color: rgb(255, 255, 255); qproperty-alignment: AlignCenter;")
ba(date_label)

def update_clock():
    now = datetime.now()
    clock_label.textContent = now.strftime("%I:%M:%S %p")
    date_label.textContent = now.strftime("%B %d, %Y")

update_clock()

# Testing our brand new DOM-style interval
# either name is fine set_interval or setInterval
#set_interval(update_clock, 1000)
setInterval(update_clock, 1000)

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
```


</details>

---

<details>
<summary><b>Section: 010_pyside6dom_textarea</b></summary>


### `pyside6dom_textarea_local_testing.py`

```python
# pyside6dom_example.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window("Notepad App", 500, 400)

theTitle = ce('h1')
theTitle.textContent = "Notes"
theTitle.style("color: rgb(0, 255, 255); margin-bottom: 10px;")
ba(theTitle)

note_pad = ce('textarea')
note_pad.placeholder = "Start typing your notes here...\n(Press Enter for a new line)"
note_pad.style("background-color: rgb(26, 26, 26); color: rgb(0, 255, 255); font-family: Arial; font-size: 24px;")

# Zero-argument function exactly like vanilla JS
def update_count():
    # We pull the text length directly from the element's value
    char_count.textContent = f"Characters: {len(note_pad.value)}"

# Grouped right with the element creation
note_pad.oninput = update_count
ba(note_pad)

char_count = ce('text')
char_count.textContent = "Characters: 0"
char_count.style("color: rgb(130, 130, 130); text-align: right;")
ba(char_count)

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
```


</details>

---

<details>
<summary><b>Section: 011_pyside6dom_open_url</b></summary>


### `pyside6dom_open_url_local_testing.py`

```python
# pyside6dom_open_url_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

import webbrowser

from pyside6dom import *

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
```


</details>

---

<details>
<summary><b>Section: 014_list_of_dictionaries_show_all_for_loop</b></summary>


### `list_of_dictionaries_show_all_local_testing.py`

```python
# list_of_dictionaries_show_all_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

people = [
    {
        "name": "Jane",
        "score": 93
    },

    {
        "name": "Joan",
        "score": 90
    },

    {
        "name": "Melissa",
        "score": 98
    },

    {
        "name": "Jennifer",
        "score": 91
    },

    {
        "name": "Tabitha",
        "score": 88
    },

    {
        "name": "Sabrina",
        "score": 85
    },

    {
        "name": "Nicole",
        "score": 94
    },

    {
        "name": "Britney",
        "score": 92
    },

    {
        "name": "Zoe",
        "score": 82
    },

    {
        "name": "Clarissa",
        "score": 79
    },

    {
        "name": "Bonnie",
        "score": 100
    },
]

init_window('Scores', 700, 500)

output_label = ce('text')
output_label.style('font-size: 30px; font-weight: bold')
ba(output_label)

people_scroll_box = ce('scroll_div')
people_scroll_box.id = 'people_scroll_box'
people_scroll_box.style("border: 1px solid rgb(255, 255, 255);")
ba(people_scroll_box)

for person in people:
    name_btn = ce('button')
    name_btn.textContent = f"{person['name']}: {person['score']}"
    name_btn.style("font-size: 30px; font-weight: bold; color: aqua;")
    # we can type color or font-color, either is fine

    # Freeze the current person into a local variable 'p'
    def handle_click(p=person):
        print(f"{p['name']}: {p['score']}")
        output_label.textContent = f"{p['name']}: {p['score']}"
        
    name_btn.onclick = handle_click
    ba(name_btn, people_scroll_box)

####

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
```


</details>

---

<details>
<summary><b>Section: 015_dictionary_of_dictionaries_show_all</b></summary>


### `dictionary_of_dictionaries_show_all_local_testing.py`

```python
# dictionary_of_dictionaries_show_all_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

people = {
    "jane_doe": {
        "first_name": "Jane",
        "last_name": "Doe",
        "score": 93
    },
    "joan_smith": {
        "first_name": "Joan",
        "last_name": "Smith",
        "score": 90
    },
    "melissa_taylor": {
        "first_name": "Melissa",
        "last_name": "Taylor",
        "score": 98
    },
    "jennifer_parker": {
        "first_name": "Jennifer",
        "last_name": "Parker",
        "score": 91
    },
    "tabitha_brooks": {
        "first_name": "Tabitha",
        "last_name": "Brooks",
        "score": 88
    },
    "sabrina_clark": {
        "first_name": "Sabrina",
        "last_name": "Clark",
        "score": 85
    },
    "nicole_morgan": {
        "first_name": "Nicole",
        "last_name": "Morgan",
        "score": 94
    },
    "britney_cooper": {
        "first_name": "Britney",
        "last_name": "Cooper",
        "score": 92
    },
    "zoe_baker": {
        "first_name": "Zoe",
        "last_name": "Baker",
        "score": 82
    },
    "clarissa_hayes": {
        "first_name": "Clarissa",
        "last_name": "Hayes",
        "score": 79
    },
    "bonnie_bell": {
        "first_name": "Bonnie",
        "last_name": "Bell",
        "score": 100
    }
}

init_window('Scores', 700, 600)

output_label = ce('text')
ba(output_label)

people_scroll_box = ce('scroll_div')
people_scroll_box.id = 'people_scroll_box'
people_scroll_box.style("border: 1px solid rgb(255, 255, 255);")
ba(people_scroll_box)

for person_key, person_data in people.items():
    name_btn = ce('button')
    # Display the properly capitalized first and last name on the button
    name_btn.textContent = f"{person_data['first_name']} {person_data['last_name']}: {person_data['score']}"
    name_btn.style("font-size: 25px; font-weight: bold; color: aqua;")

    # Freeze the lowercase key AND the inner dictionary data
    def handle_click(p_key=person_key, p_data=person_data):
        # Print the lowercase key first to prove we are pulling it from the top level
        print(f"Dictionary Key: '{p_key}' -> Student: {p_data['first_name']} {p_data['last_name']}, Score: {p_data['score']}")

        output_label.textContent = f"Dictionary Key: '{p_key}' -> Student: {p_data['first_name']} {p_data['last_name']}, Score: {p_data['score']}"

    name_btn.onclick = handle_click
    ba(name_btn, people_scroll_box)

####

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
```


</details>

---

<details>
<summary><b>Section: 016_class</b></summary>


### `Dog_local_testing.py`

```python
# Dog_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

set_theme("""
text {
    font-size: 40px;
    font-weight: bold;
}
""")

####

class Dog:
    def __init__(this, name, weight):
        this.name = name
        this.weight = weight

####

fido = Dog("Fido", 16)
rex = Dog("Rex", 20)

####

init_window('Dog Class', 700, 500)

dog_label = ce('text')
dog_label.textContent = fido.name + ' weighs ' + str(fido.weight) + ' lbs'
ba(dog_label)

# our shortcut cl
# we could alternatively write console.log or
# we could write print instead
cl(fido.name + ' weighs ' + str(fido.weight) + ' lbs')

run_app()

####

'''
Fido weighs 16 lbs
'''

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
```


</details>

---

<details>
<summary><b>Section: 021_image</b></summary>


### `image_local_testing.py`

```python
# image_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

# Initialize the Application
init_window("Showing an Image", 1100, 650)

theImage = ce('img')
theImage.src = '001.png'
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
```


</details>

---

<details>
<summary><b>Section: 022_random_image</b></summary>


### `random_image_local_testing.py`

```python
# random_image_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

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
```


</details>

---

<details>
<summary><b>Section: 023_css_keywords</b></summary>


### `css_keywords_local_testing.py`

```python
# css_keywords_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window("Many CSS Keywords", 400, 500)

set_theme("""
    div {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    text {
        padding-top: 5px;
    }
    text#title_heading {
        font-size: 22px;
        font-weight: bold;
        color: #00ffcc;
        margin-bottom: 10px;
    }
    button {
        background-color: #007acc;
        color: white;
        border-radius: 4px;
        padding: 10px;
        font-weight: bold;
        margin-top: 15px;
    }
    button:hover { background-color: #0099ff; }
    button:pressed { background-color: #005c99; }
    
    select {
        padding: 6px;
        background-color: #2b2b2b;
        border: 1px solid #555;
        border-radius: 3px;
    }
    /* This fixes the missing hover highlight in dropdowns using HTML syntax */
    select option {
        background-color: #2b2b2b;
        selection-background-color: #007acc;
        selection-color: white;
    }
    
    scroll_div {
        border: 1px solid #444;
        background-color: #111;
        margin-top: 10px;
    }
""")

# ===
#  UI BUILDER
# ===

header = ce("h1")
header.id = "title_heading"
header.textContent = "⚙️ Settings Panel"
ba(header)

mode_label = ce("text")
mode_label.textContent = "Select Operating Mode:"
ba(mode_label)

mode_select = ce("select")
mode_select.id = "app_mode"
mode_select.options = ["Standard", "Advanced", "Developer"]
ba(mode_select)

debug_checkbox = ce("checkbox")
debug_checkbox.id = "debug_flag"
debug_checkbox.textContent = "Enable Debug Logging"
debug_checkbox.checked = True
ba(debug_checkbox)

apply_btn = ce("button")
apply_btn.textContent = "Apply Settings"
ba(apply_btn)

log_window = ce("scroll_div")
ba(log_window)

def handle_apply():
    selected = ge("app_mode").value
    debug = ge("debug_flag").checked
    
    log = ce("p")
    log.textContent = f"> Mode: {selected} | Debug: {debug}"
    log.style("color: #00ff00; font-family: monospace;") # Inline overrides still work
    ba(log, log_window)

apply_btn.onclick = handle_apply

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
```


</details>

---

<details>
<summary><b>Section: 024_video_play_pause</b></summary>


### `video_play_pause_local_testing.py`

```python
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
```


</details>

---

<details>
<summary><b>Section: 026_styling_dynamically</b></summary>


### `styling_dynamically_local_testing.py`

```python
# styling_dynamically_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window('Our App', 700, 600)

# Define your dynamic color variable
dynamic_color = 'rgb(0, 255, 255)'

ourTitle = ce('text')
ourTitle.textContent = 'Howdy'
# Target the PySide6 style engine
ourTitle.style.color = dynamic_color
ba(ourTitle)

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
```


</details>

---

<details>
<summary><b>Section: 030_input</b></summary>


### `input_local_testing.py`

```python
# input_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window('Our App', 700, 600)

our_greeting = ce('text')
our_greeting.textContent = 'Hi Everyone'
our_greeting.style.fontFamily = 'Arial'
our_greeting.style.fontSize = '70px'
our_greeting.style.fontWeight = 'bold'
our_greeting.style.color = 'rgb(255, 255, 255)'
ba(our_greeting)

word_input = ce('input')
word_input.placeholder = 'Enter Name'
def handle_input():
    print(word_input.value)
word_input.oninput = handle_input
ba(word_input)

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
```


</details>

---

<details>
<summary><b>Section: 031_input_upper</b></summary>


### `input_upper_local_testing.py`

```python
# input_upper_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

from pyside6dom import *

init_window('Our App', 700, 600)

our_greeting = ce('text')
our_greeting.textContent = 'Hi Everyone'
our_greeting.style.fontFamily = 'Arial'
our_greeting.style.fontSize = '70px'
our_greeting.style.fontWeight = 'bold'
our_greeting.style.color = 'rgb(255, 255, 255)'
ba(our_greeting)

word_input = ce('input')
word_input.placeholder = 'Enter Name'
def handle_input():
    print(word_input.value.upper())
word_input.oninput = handle_input
ba(word_input)

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
```


</details>

---

<details>
<summary><b>Section: 1.1_read_csv</b></summary>


### `read_csv_show_with_innerHTML_local_testing.py`

```python
# read_csv_show_with_innerHTML_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV File', 700, 400)

output = ce('text')
# Inject the Pandas HTML directly into the text element
output.innerHTML = theData.to_html(index=False, border=1)

ba(output)

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
```


</details>

---

<details>
<summary><b>Section: 1.2_read_csv_len</b></summary>


### `read_csv_len_local_testing.py`

```python
# read_csv_len_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up THREE levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) 
sys.path.insert(0, project_root)
# --------------------------

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

output_text = ce('text')
output_text.innerHTML = theData.to_html(index=False, border=1)
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
4 people
'''

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
```

### `read_csv_len_with_padding_replace_local_testing.py`

```python
# read_csv_len_with_padding_replace_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up THREE levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) 
sys.path.insert(0, project_root)
# --------------------------

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

# Generate the raw HTML string from Pandas
raw_html = theData.to_html(index=False, border=1)

# Inject standard HTML cellpadding directly into the table tag
padded_html = raw_html.replace('<table', '<table cellpadding="8"')

output_text = ce('text')
output_text.innerHTML = padded_html
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
4 people
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
'''

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
```

### `read_csv_len_with_padding_style_local_testing.py`

```python
# read_csv_len_with_padding_style_local_testing.py

import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up THREE levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) 
sys.path.insert(0, project_root)
# --------------------------

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

# Generate the raw HTML string from Pandas (no need to force the border here anymore)
raw_html = theData.to_html(index=False)

# Write pure CSS exactly how a web developer would expect to
table_css = """
<style>
    table {
        border-collapse: collapse;
        margin-top: 10px;
    }
    th, td {
        padding: 8px 15px; 
        border: 1px solid white;
    }
    th {
        background-color: #333333;
        font-weight: bold;
    }
</style>
"""

output_text = ce('text')
# We just glue the CSS and the HTML together, like a real webpage
output_text.innerHTML = table_css + raw_html
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
4 people
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
'''

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
```


</details>

---

<details>
<summary><b>Section: arithmetic</b></summary>


### `calculate_percent.py`

```python
# calculate_percent.py

from pyside6dom import *

def calculate_percent(percent, total):
    return (percent / 100) * total

####

init_window("Percentage Calculator", 400, 350)

set_theme("""
    body {
        background-color: rgb(20, 20, 20);
    }
    input { 
        padding: 10px; 
        font-size: 24px; 
        font-weight: bold;
        border: 2px solid rgb(100, 100, 100); 
        border-radius: 5px; 
        margin-bottom: 10px;
    }
    input:focus {
        border: 2px solid rgb(0, 255, 255);
    }
""")

# Title
app_title = ce('h1')
app_title.textContent = "Percentage Calculator"
app_title.style.fontSize = '30px'
app_title.style.fontWeight = 'bold'
app_title.style.marginBottom = '20px'
app_title.style.color = 'rgb(0, 255, 255)'
#app_title.style("font-size: 30px; font-weight: bold; margin-bottom: 20px; color: rgb(0, 255, 255);")
ba(app_title)

# Input: Percentage
percent_input = ce('input')
percent_input.id = 'percent_val'
percent_input.placeholder = "Enter percentage (e.g., 20)"
def update_result():
    # Grab the raw text from the DOM
    p_text = ge('percent_val').value
    t_text = ge('total_val').value

    # We use a try/except section in case the user types letters or leaves it blank
    try:
        # Convert text to floats (decimals)
        p_num = float(p_text)
        t_num = float(t_text)

        # Pass the numbers to our custom math function
        answer = calculate_percent(p_num, t_num)

        # Display the formatted result
        ge('result_label').textContent = f"{p_num}% of {t_num} is {answer:.2f}"

    except ValueError:
        # If the input isn't a valid number yet, reset the text gracefully
        ge('result_label').textContent = "Waiting for numbers..."
percent_input.oninput = update_result
ba(percent_input)

# Input: Total Amount
total_input = ce('input')
total_input.id = 'total_val'
total_input.placeholder = "Enter total amount (e.g., 150)"
total_input.oninput = update_result
ba(total_input)

result_scroll_div = ce('scroll_div')
result_scroll_div.style.border = '1px solid white'
result_scroll_div.style.padding = '2px'
result_scroll_div.style.width = '350px'
ba(result_scroll_div)

# Result Display
result_display = ce('text')
result_display.id = 'result_label'
result_display.textContent = "Result will appear here..."
result_display.style.border = 'none'
result_display.style.fontSize = '25px'
result_display.style.fontWeight = 'bold'
result_display.style.color = 'rgb(255, 255, 255)'
#result_display.style("font-size: 25px; font-weight: bold; color: rgb(255, 255, 255); margin-top: 20px;")
ba(result_display, result_scroll_div)

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
```


</details>

---

<details>
<summary><b>Section: geometry</b></summary>


### `calculate_circle_metrics.py`

```python
# calculate_circle_metrics.py

import math
from pyside6dom import *

def get_circumference(radius):
    """ C = 2 * Pi * r """
    return 2 * math.pi * radius

def get_area(radius):
    """ A = Pi * r^2 """
    return math.pi * (radius ** 2)

####

init_window("Circle Geometry", 420, 400)

set_theme("""
    body { background-color: rgb(20, 25, 30); }
    input { 
        width: 300px;
        padding: 10px; 
        font-size: 20px; 
        font-weight: bold;
        border: 2px solid rgb(100, 100, 150); 
        border-radius: 5px; 
        margin-bottom: 15px;
        color: rgb(255, 255, 255);
        background-color: rgb(30, 35, 45);
    }
    input:focus { border: 2px solid rgb(255, 100, 255); }
""")

# Title
app_title = ce('h1')
app_title.textContent = "Circle Engine"
app_title.style.color = 'rgb(255, 100, 255)' # Neon Pink/Purple theme for Geometry
ba(app_title)

def update_results():
    r_text = ge('radius_val').value

    try:
        radius_num = float(r_text)
        if radius_num < 0:
            raise ValueError("Radius cannot be negative")

        circ = get_circumference(radius_num)
        area = get_area(radius_num)

        ge('circ_label').textContent = f"Circumference: {circ:.2f}"
        ge('circ_label').style.color = 'rgb(0, 255, 200)'

        ge('area_label').textContent = f"Area: {area:.2f}"
        ge('area_label').style.color = 'rgb(0, 255, 200)'

    except ValueError:
        ge('circ_label').textContent = "Waiting for radius..."
        ge('circ_label').style.color = 'rgb(150, 150, 150)'
        ge('area_label').textContent = "Waiting for radius..."
        ge('area_label').style.color = 'rgb(150, 150, 150)'

# Input: Radius
radius_label = ce('text')
radius_label.textContent = 'Radius (distance from center to edge)'
radius_label.style.fontWeight = 'bold'
ba(radius_label)

radius_input = ce('input')
radius_input.id = 'radius_val'
radius_input.placeholder = "Enter radius (e.g., 5.5)"
radius_input.oninput = update_results
ba(radius_input)

# Display Container
result_box = ce('scroll_div')
result_box.style.border = '1px dashed rgb(100, 100, 150)'
result_box.style.padding = '15px'
# Testing the new engine style interception!
result_box.style.width = '300px'  
ba(result_box)

# Output: Circumference
circ_output = ce('text')
circ_output.id = 'circ_label'
circ_output.textContent = "Waiting for radius..."
circ_output.style.fontSize = '18px'
circ_output.style.fontWeight = 'bold'
ba(circ_output, result_box)

# Output: Area
area_output = ce('text')
area_output.id = 'area_label'
area_output.textContent = "Waiting for radius..."
area_output.style.fontSize = '18px'
area_output.style.fontWeight = 'bold'
ba(area_output, result_box)

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
```


</details>

---

<details>
<summary><b>Section: calculate_speed_generic</b></summary>


### `calculate_speed.py`

```python
# calculate_speed.py

from pyside6dom import *

def calculate_speed(distance, time):
    """
    Calculates velocity/speed given distance and time elapsed.
    Speed = Distance / Time
    """
    if time <= 0:
        raise ValueError("Time must be greater than zero.")
    return distance / time

####

init_window("Speed Calculator", 475, 420)

set_theme("""
    body { background-color: rgb(20, 20, 20); }
    input { 
        width: 400px;
        padding: 10px; 
        font-size: 20px; 
        font-weight: bold;
        border: 2px solid rgb(100, 100, 100); 
        border-radius: 5px; 
        margin-bottom: 12px;
        color: rgb(240, 240, 240);
        background-color: rgb(30, 30, 30);
    }
    input:focus { border: 2px solid rgb(0, 255, 255); }
""")

# Title
app_title = ce('h1')
app_title.textContent = "Speed & Velocity Engine"
app_title.style.fontSize = '26px'
app_title.style.fontWeight = 'bold'
app_title.style.marginBottom = '20px'
app_title.style.color = 'rgb(0, 255, 255)'
ba(app_title)

def update_result():
    d_text = ge('dist_val').value
    t_text = ge('time_val').value

    try:
        dist_num = float(d_text)
        time_num = float(t_text)

        speed = calculate_speed(dist_num, time_num)

        result_box = ge('result_label')
        result_box.textContent = f"Velocity: {speed:.2f} units/hr"
        result_box.style.color = 'rgb(0, 255, 255)'

    except ValueError:
        result_box = ge('result_label')
        if not d_text or not t_text:
            result_box.textContent = "Enter distance and time..."
            result_box.style.color = 'rgb(200, 200, 200)'
        else:
            result_box.textContent = "Time must be > 0"
            result_box.style.color = 'rgb(255, 80, 80)'

distance_label = ce('text')
distance_label.textContent = 'Distance'
ba(distance_label)

# Input: Distance
distance_input = ce('input')
distance_input.id = 'dist_val'
distance_input.placeholder = "Distance (e.g., 300 km or miles)"
distance_input.oninput = update_result
ba(distance_input)

time_label = ce('text')
time_label.textContent = 'Time'
ba(time_label)

# Input: Time
time_input = ce('input')
time_input.id = 'time_val'
time_input.placeholder = "Time elapsed (e.g., 4.5 hours)"
time_input.oninput = update_result
ba(time_input)

# Result Container
result_scroll_div = ce('scroll_div')
result_scroll_div.style.border = '1px solid rgb(80, 80, 80)'
result_scroll_div.style.borderRadius = '5px'
result_scroll_div.style.padding = '10px'
result_scroll_div.style.width = '400px'
ba(result_scroll_div)

# Result Display
result_display = ce('text')
result_display.id = 'result_label'
result_display.textContent = "Enter distance and time..."
#result_display.style.width = '300px'
result_display.style.border = 'none'
result_display.style.fontSize = '22px'
result_display.style.fontWeight = 'bold'
result_display.style.color = 'rgb(200, 200, 200)'
ba(result_display, result_scroll_div)

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
```


</details>

---

<details>
<summary><b>Section: calculate_speed_mph</b></summary>


### `calculate_speed_mph.py`

```python
# calculate_speed_mph.py

from pyside6dom import *

def calculate_speed_mph(distance_miles, time_minutes):
    """
    Calculates Speed in Miles Per Hour (mph).
    Automatically converts minutes into hours behind the scenes!
    """
    if time_minutes <= 0:
        raise ValueError("Time must be greater than zero.")
    
    # Convert minutes to hours
    time_hours = time_minutes / 60.0 
    
    return distance_miles / time_hours

init_window("Speed Calculator", 475, 420)

set_theme("""
    body { background-color: rgb(20, 20, 20); }
    input { 
        width: 400px;
        padding: 10px; 
        font-size: 20px; 
        font-weight: bold;
        border: 2px solid rgb(100, 100, 100); 
        border-radius: 5px; 
        margin-bottom: 12px;
        color: rgb(240, 240, 240);
        background-color: rgb(30, 30, 30);
    }
    input:focus { border: 2px solid rgb(0, 255, 255); }
""")

# Title
app_title = ce('h1')
app_title.textContent = "Commute Speed (MPH)"
app_title.style.fontSize = '26px'
app_title.style.color = 'rgb(0, 255, 255)'
ba(app_title)

def update_result():
    d_text = ge('dist_val').value
    t_text = ge('time_val').value

    try:
        dist_num = float(d_text)
        time_num = float(t_text)

        # Call our updated MPH calculator
        speed = calculate_speed_mph(dist_num, time_num)

        result_box = ge('result_label')
        result_box.textContent = f"Average Speed: {speed:.1f} mph"
        result_box.style.color = 'rgb(0, 255, 255)'

    except ValueError:
        result_box = ge('result_label')
        if not d_text or not t_text:
            result_box.textContent = "Enter miles and minutes..."
            result_box.style.color = 'rgb(200, 200, 200)'
        else:
            result_box.textContent = "Time must be > 0"
            result_box.style.color = 'rgb(255, 80, 80)'

# Distance UI
distance_label = ce('text')
distance_label.textContent = 'Distance (Miles)'
ba(distance_label)

distance_input = ce('input')
distance_input.id = 'dist_val'
distance_input.placeholder = "e.g., 15 (miles)"
distance_input.oninput = update_result
ba(distance_input)

# Time UI
time_label = ce('text')
time_label.textContent = 'Time (Minutes)'
ba(time_label)

time_input = ce('input')
time_input.id = 'time_val'
time_input.placeholder = "e.g., 45 (minutes)"
time_input.oninput = update_result
ba(time_input)

# Result Container
result_scroll_div = ce('scroll_div')
result_scroll_div.style.border = '1px solid rgb(80, 80, 80)'
result_scroll_div.style.borderRadius = '5px'
result_scroll_div.style.padding = '10px'
result_scroll_div.style.width = '400px'
ba(result_scroll_div)

# Result Display
result_display = ce('text')
result_display.id = 'result_label'
result_display.textContent = "Enter miles and minutes..."
result_display.style.border = 'none'
result_display.style.fontSize = '22px'
result_display.style.fontWeight = 'bold'
result_display.style.color = 'rgb(200, 200, 200)'
ba(result_display, result_scroll_div)

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
```


</details>

---

<details>
<summary><b>Section: kinematics_hub_with_slider</b></summary>


### `kinematics_hub_with_slider.py`

```python
# kinematics_hub.py

from pyside6dom import *

init_window("Kinematics Hub", 500, 680) # Made the window slightly taller

set_theme("""
    body { background-color: rgb(20, 20, 25); }
    
    .hub_title {
        color: rgb(0, 255, 255);
        font-size: 28px;
        font-weight: bold;
        text-align: center; 
        margin-bottom: 20px;
    }
    
    .input_box { 
        width: 420px;
        padding: 12px; 
        font-size: 20px; 
        font-weight: bold;
        border: 2px solid rgb(80, 80, 90); 
        border-radius: 6px; 
        margin-bottom: 15px;
        color: white;
        background-color: rgb(30, 30, 40);
    }
    .input_box:focus { border: 2px solid rgb(0, 255, 200); }
    
    .dropdown_menu {
        width: 420px;
        padding: 10px;
        font-size: 18px;
        font-weight: bold;
        background-color: rgb(40, 40, 50);
        color: rgb(0, 255, 200);
        border: 2px solid rgb(0, 255, 200);
        border-radius: 6px;
        margin-bottom: 25px;
    }
    
    .result_container {
        border: 1px solid rgb(60, 60, 80);
        background-color: rgb(15, 15, 18);
        border-radius: 8px;
        padding: 20px;
        width: 420px;
        margin-top: 10px;
    }
    
    .result_text {
        font-size: 24px;
        font-weight: bold;
        color: rgb(200, 200, 200);
        text-align: center; 
    }
    
    /* New Style for the Slider Label */
    .slider_label {
        color: rgb(150, 150, 150);
        font-size: 14px;
        text-align: center;
        margin-top: 20px;
    }
""")

def handle_mode_change():
    mode = ge('mode_select').value
    in1_lbl = ge('input1_label')
    in1 = ge('input1')
    in2_lbl = ge('input2_label')
    in2 = ge('input2')
    res = ge('result_label')
    speed_gauge = ge('speed_slider')

    in1.value = ""
    in2.value = ""
    speed_gauge.value = 0 # Reset the gauge!
    res.textContent = "Enter values to calculate..."
    res.style.color = 'rgb(200, 200, 200)'

    if mode == "Solve for Speed (MPH)":
        in1_lbl.textContent = "Distance (Miles)"
        in1.placeholder = "e.g., 15"
        in2_lbl.textContent = "Time (Minutes)"
        in2.placeholder = "e.g., 45"
    elif mode == "Solve for Distance (Miles)":
        in1_lbl.textContent = "Average Speed (MPH)"
        in1.placeholder = "e.g., 65"
        in2_lbl.textContent = "Time (Minutes)"
        in2.placeholder = "e.g., 120"
    elif mode == "Solve for Time (Minutes)":
        in1_lbl.textContent = "Distance (Miles)"
        in1.placeholder = "e.g., 15"
        in2_lbl.textContent = "Average Speed (MPH)"
        in2.placeholder = "e.g., 45"

def calculate_math():
    mode = ge('mode_select').value
    v1_text = ge('input1').value
    v2_text = ge('input2').value
    res = ge('result_label')
    speed_gauge = ge('speed_slider')

    try:
        val1 = float(v1_text)
        val2 = float(v2_text)
        
        current_speed = 0 # We will use this to set the slider

        if mode == "Solve for Speed (MPH)":
            if val2 <= 0: raise ValueError
            ans = val1 / (val2 / 60.0)
            res.textContent = f"Average Speed: {ans:.1f} mph"
            current_speed = ans
            
        elif mode == "Solve for Distance (Miles)":
            if val2 < 0: raise ValueError
            ans = val1 * (val2 / 60.0)
            res.textContent = f"Total Distance: {ans:.2f} miles"
            current_speed = val1 # The user inputted the speed in box 1
            
        elif mode == "Solve for Time (Minutes)":
            if val2 <= 0: raise ValueError
            total_mins = (val1 / val2) * 60.0
            if total_mins >= 60:
                res.textContent = f"Time: {int(total_mins // 60)} hr {int(total_mins % 60)} min"
            else:
                res.textContent = f"Time: {int(total_mins)} minutes"
            current_speed = val2 # The user inputted the speed in box 2

        res.style.color = 'rgb(0, 255, 200)'
        
        # Cap the visual slider at 120 mph so it doesn't break the UI
        speed_gauge.value = min(current_speed, 120) 

    except ValueError:
        speed_gauge.value = 0
        if not v1_text or not v2_text:
            res.textContent = "Enter values to calculate..."
            res.style.color = 'rgb(200, 200, 200)'
        else:
            res.textContent = "Invalid numbers"
            res.style.color = 'rgb(255, 80, 80)'


# (UI Building Code Stays the Same until the bottom)
title = ce('text')
title.className = 'hub_title'
title.textContent = "Kinematics Command Center"
ba(title)

mode_dropdown = ce('select')
mode_dropdown.id = 'mode_select'
mode_dropdown.className = 'dropdown_menu'
mode_dropdown.options = ["Solve for Speed (MPH)", "Solve for Distance (Miles)", "Solve for Time (Minutes)"]
mode_dropdown.oninput = handle_mode_change
ba(mode_dropdown)

in1_label = ce('text'); in1_label.id = 'input1_label'; in1_label.textContent = "Distance (Miles)"; ba(in1_label)
in1 = ce('input'); in1.id = 'input1'; in1.className = 'input_box'; in1.placeholder = "e.g., 15"; in1.oninput = calculate_math; ba(in1)

in2_label = ce('text'); in2_label.id = 'input2_label'; in2_label.textContent = "Time (Minutes)"; ba(in2_label)
in2 = ce('input'); in2.id = 'input2'; in2.className = 'input_box'; in2.placeholder = "e.g., 45"; in2.oninput = calculate_math; ba(in2)

res_container = ce('scroll_div')
res_container.className = 'result_container'
ba(res_container)

result_txt = ce('text')
result_txt.id = 'result_label'
result_txt.className = 'result_text'
result_txt.textContent = "Enter values to calculate..."
ba(result_txt, res_container)

####

# THE NEW SPEEDOMETER UI
slider_lbl = ce('text')
slider_lbl.className = 'slider_label'
slider_lbl.textContent = "0 mph ------------------------- Visual Speedometer ------------------------ 120 mph"
ba(slider_lbl)

speedometer = ce('slider')
speedometer.id = 'speed_slider'
# We access the raw Qt widget to adjust the max range to handle high speeds!
speedometer.raw.setMaximum(1200) # 1200 / 10 = 120 max value in your engine
speedometer.raw.setEnabled(False) # Prevents the user from manually dragging it
ba(speedometer)

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
```


</details>

---

<details>
<summary><b>Section: class_pokemon_use_method</b></summary>


### `class_pokemon_use_method.py`

```python
# class_pokemon_use_method.py

from pyside6dom import *

init_window('PySide6DOM Pokedex', 800, 600)

set_theme("""
    body { background-color: rgb(25, 25, 30); color: white; font-family: 'Segoe UI', Arial; }
    
    .summon_btn {
        background-color: rgb(50, 50, 60);
        color: white;
        border: 2px solid rgb(100, 100, 120);
        border-radius: 8px;
        padding: 10px;
        font-weight: bold;
        font-size: 16px;
    }
    .summon_btn:hover { background-color: rgb(80, 80, 90); border-color: white; }
    
    .poke_card {
        border-radius: 10px;
        border: 2px solid rgba(255, 255, 255, 0.5);
    }
""")

# ===
# THE CLASS
# ===
class Pokemon:
    def __init__(self, name, kind, hex_color):
        self.name = name
        self.kind = kind
        self.color = hex_color

    def renderCard(self, parent_container):
        """Builds a DOM Div and appends it to the container"""
        card = ce('div')
        card.className = 'poke_card'
        card.style.backgroundColor = self.color
        card.style.display = 'flex'
        card.style.flexDirection = 'column'
        card.style.padding = 15  
        card.style.width = 250
        
        name_lbl = ce('h1')
        name_lbl.textContent = self.name
        name_lbl.style.margin = 0
        name_lbl.style.color = 'white'
        card.append(name_lbl)
        
        kind_lbl = ce('text')
        kind_lbl.textContent = f"Type: {self.kind}"
        kind_lbl.style.fontSize = '18px'
        kind_lbl.style.fontWeight = 'bold'
        kind_lbl.style.color = 'rgba(255, 255, 255, 0.8)'
        card.append(kind_lbl)

        parent_container.append(card)

# ===
# BUILD THE UI LAYOUT
# ===
main_row = ce('div')
main_row.style.display = 'flex'
main_row.style.flexDirection = 'row'
main_row.style.gap = 40  # Our new flex gap!
main_row.style.padding = 30
ba(main_row)

# Left Column: Buttons
controls = ce('div')
controls.style.display = 'flex'
controls.style.flexDirection = 'column'
controls.style.gap = 15
main_row.append(controls)

# Right Column: The Pokedex Screen
pokedex_screen = ce('scroll_div')
pokedex_screen.style.width = 350
pokedex_screen.style.height = 500
pokedex_screen.style.backgroundColor = 'rgb(15, 15, 18)'
pokedex_screen.style.border = '3px solid rgb(100, 100, 100)'
pokedex_screen.style.padding = 15 # Internal padding so cards don't touch the edges
main_row.append(pokedex_screen)

# ===
# INSTANTIATE DATA & LOGIC
# ===
roster = [
    Pokemon("Pikachu", "Electric", "#D4A017"),
    Pokemon("Charmander", "Fire", "#C0392B"),
    Pokemon("Bulbasaur", "Grass", "#27AE60"),
    Pokemon("Squirtle", "Water", "#2980B9")
]

# Generate a button for every Pokemon in our array
for poke in roster:
    btn = ce('button')
    btn.className = 'summon_btn'
    btn.textContent = f"Summon {poke.name}"
    
    # Freeze the current 'poke' variable into the lambda!
    btn.onclick = lambda p=poke: p.renderCard(pokedex_screen)
    
    controls.append(btn)

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
```


</details>

---

<details>
<summary><b>Section: console</b></summary>


### `get_year_month_day.py`

```python
# get_year_month_day.py

import datetime as dt

def get_year_month_day():
    today = dt.date.today()
    return today

if __name__ == '__main__':
    print(get_year_month_day())
    input('Press Enter to Exit')

'''
2026-08-20
Press Enter to Exit
'''

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
```


</details>

---

<details>
<summary><b>Section: pyside6dom_custom</b></summary>


### `get_year_month_day.py`

```python
# get_year_month_day.py

import datetime as dt
from pyside6dom import *

def get_year_month_day():
    today = dt.date.today()
    return today

init_window('Date', 800, 500)

date_div = ce('div')
date_div.textContent = get_year_month_day()
date_div.style.fontFamily = 'Arial'
date_div.style.fontSize = '50px'
date_div.style.fontWeight = 'bold'
date_div.style.padding = '5px 10px'
ba(date_div)

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
```


</details>

---

<details>
<summary><b>Section: pyside6dom_native</b></summary>


### `get_year_month_day.py`

```python
# get_year_month_day.py

from pyside6dom import *

init_window('Date', 800, 500)

date_div = ce('div')
date_div.textContent = dom.get_year_month_day()
date_div.style.fontFamily = 'Arial'
date_div.style.fontSize = '50px'
date_div.style.fontWeight = 'bold'
date_div.style.padding = '5px 10px'
ba(date_div)

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
```


</details>

---

<details>
<summary><b>Section: elements</b></summary>


### `text.py`

```python
# text.py

from pyside6dom import *

init_window('Element: text', 700, 500)

our_text = ce('text')
our_text.textContent = 'Hi Everyone'
ba(our_text)

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
```


</details>

---

<details>
<summary><b>Section: experiments</b></summary>


### `movement_with_controls.py`

```python
from pyside6dom import *

# Import Qt's keyboard listener tools
from PySide6.QtGui import QShortcut, QKeySequence

init_window('Continuous Movement + WASD', 700, 600)

# OUR STATE 
state = {
    "x": 0,
    "timer": None
}

# THE PLAYER (The Cube)
player = ce('div')
player.id = 'player'
player.style.border = '2px solid rgb(0, 255, 200)'
player.style.background = 'rgb(20, 100, 150)'
player.style.width = 100
player.style.height = 100
player.style.position = 'absolute'
player.style.left = state["x"]
player.style.top = 100
ba(player)

# THE BUTTON CONTAINER FIX
move_btn_container = ce('div')
move_btn_container.style.display = 'flex'
move_btn_container.style.flexDirection = 'row'
move_btn_container.style.position = 'absolute'
move_btn_container.style.top = 230
# Hard dimensions prevent Qt from collapsing it
move_btn_container.style.width = 400 
move_btn_container.style.height = 50 
ba(move_btn_container)

# MOVEMENT LOGIC
def stop_moving():
    if state["timer"]:
        clearInterval(state["timer"])
        state["timer"] = None

def move_left():
    stop_moving() 
    def loop():
        state["x"] -= 5
        player.style.left = state["x"]
    state["timer"] = setInterval(loop, 20)

def move_right():
    stop_moving()
    def loop():
        state["x"] += 5
        player.style.left = state["x"]
    state["timer"] = setInterval(loop, 20)

# ATTACH BUTTONS
btn_left = ce('button')
btn_left.textContent = '<< Left (A)'
btn_left.onclick = move_left
move_btn_container.append(btn_left)

btn_stop = ce('button')
btn_stop.textContent = 'STOP (S)'
btn_stop.onclick = stop_moving
btn_stop.style.color = 'salmon'
move_btn_container.append(btn_stop)

btn_right = ce('button')
btn_right.textContent = 'Right (D) >>'
btn_right.onclick = move_right
move_btn_container.append(btn_right)

# ===
# WASD KEYBOARD CONTROLS
# QShortcut is Qt's version of addEventListener('keydown')!
# ===

QShortcut(QKeySequence("A"), player.raw).activated.connect(move_left)
QShortcut(QKeySequence("D"), player.raw).activated.connect(move_right)
QShortcut(QKeySequence("S"), player.raw).activated.connect(stop_moving)

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
```


</details>

---

<details>
<summary><b>Section: math</b></summary>


### `abs.py`

```python
# abs.py

from pyside6dom import *

init_window('Absolute Value', 700, 500)

our_number = -17

result_txt = ce('div')
result_txt.textContent = abs(our_number)
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```

### `ceil.py`

```python
# ceil.py

from pyside6dom import *

init_window('math.ceil', 700, 500)

our_number = 23.3

result_txt = ce('div')
result_txt.textContent = math.ceil(our_number)
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```

### `exponent.py`

```python
# exponent.py

from pyside6dom import *

init_window('exponent', 700, 500)

our_number = 8

result_txt = ce('div')
result_txt.textContent = our_number ** 2
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```

### `floor.py`

```python
# floor.py

from pyside6dom import *

init_window('math.floor', 700, 500)

our_number = 23.3

result_txt = ce('div')
result_txt.textContent = math.floor(our_number)
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```

### `is_prime.py`

```python
# is_prime.py

from pyside6dom import *

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

init_window('Is Number Prime', 700, 500)

our_number = 23

result_txt = ce('div')
result_txt.textContent = is_prime(our_number)
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```

### `pi.py`

```python
# pi.py

from pyside6dom import *

init_window('math.pi', 1000, 500)

result_txt = ce('div')
result_txt.textContent = math.pi
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```

### `pow.py`

```python
# pow.py

from pyside6dom import *

init_window('pow', 700, 500)

our_number = 4

result_txt = ce('div')
result_txt.textContent = pow(our_number, 2)
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```

### `round.py`

```python
# round.py

from pyside6dom import *

init_window('round', 700, 500)

our_number = 23.3

result_txt = ce('div')
result_txt.textContent = round(our_number)
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```

### `sqrt.py`

```python
# sqrt.py

from pyside6dom import *

init_window('math.sqrt', 700, 500)

our_number = 4

result_txt = ce('div')
result_txt.textContent = math.sqrt(our_number)
result_txt.style.fontSize = '100px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.10_dividing_fractions</b></summary>


### `dividing_fractions.py`

```python
# dividing_fractions.py

from sympy import Rational
from pyside6dom import *

init_window('Dividing Fractions', 700, 600)

# We define our same baseline fractions
fraction_a = Rational(1, 2)
fraction_b = Rational(1, 3)

# We divide the first fraction by the second
total = fraction_a / fraction_b

# We create our div to hold the text
result = ce('div')
result.textContent = "Our Equation:\n" + str(fraction_a) + " / " + str(fraction_b) + " = " + str(total)
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.padding = '2px 10px'
ba(result)

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
```


</details>

---

<details>
<summary><b>Section: 1.1_foundation</b></summary>


### `foundation.py`

```python
# foundation.py

from sympy import symbols, Eq, solve, Rational

from pyside6dom import *

init_window('SymPY Foundation', 700, 600)

x = symbols('x')

# 1/2x + 3/2(x + 1) - 1/4 = 5
eq = Eq(Rational(1,2)*x + Rational(3,2)*(x + 1) - Rational(1,4), 5)

sol = solve(eq, x)

print(sol)

show_work = ce('textarea')
show_work.value = eq
show_work.style.fontSize = '35px'
show_work.style.fontWeight = 'bold'
ba(show_work)

result_div = ce('textarea')
result_div.value = sol
result_div.style.fontSize = '35px'
result_div.style.fontWeight = 'bold'
ba(result_div)

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
```


</details>

---

<details>
<summary><b>Section: 1.2_algebra_distributive_property</b></summary>


### `algebra_distributive_property.py`

```python
# foundation.py

from sympy import symbols

from pyside6dom import *

init_window('Foundation', 700, 500)

r, s = symbols('r s')

# "the sum of r and s"
sum_rs = r + s

# "5 times as much as the sum of r and s"
expr = 5 * sum_rs

print(expr)

show_work = ce('textarea')
show_work.value = expr
show_work.style.fontSize = '35px'
show_work.style.fontWeight = 'bold'
ba(show_work)

result_txt = ce('textarea')
result_txt.value = '5*(r + s)'
result_txt.style.fontSize = '35px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

run_app()

# 5*(r + s)

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
```

### `algebra_distributive_property_b.py`

```python
# foundation_b.py

from sympy import symbols, Mul
from pyside6dom import *

init_window('Foundation', 700, 500)

r, s = symbols('r s')

# "the sum of r and s"
sum_rs = r + s

# "5 times as much as the sum of r and s"
# Use Mul with evaluate=False to stop SymPy from auto-expanding
expr = Mul(5, sum_rs, evaluate=False)

print(expr)

show_work = ce('textarea')
# Convert the SymPy expression to a string explicitly for the textarea
show_work.value = str(expr) 
show_work.style.fontSize = '35px'
show_work.style.fontWeight = 'bold'
ba(show_work)

# We no longer need the hardcoded second textarea because 
# expr now correctly holds the exact '(r + s)*5' structure

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
```


</details>

---

<details>
<summary><b>Section: 1.3_proportions_and_ratios</b></summary>


### `proportions_and_ratios.py`

```python
# proportions_and_ratios.py

from sympy import symbols, Eq, solve, Rational
from pyside6dom import *

init_window('Algebra Proportions', 700, 500)

x = symbols('x')

# 20 grams per 10 ounces = x grams per 8 ounces
eq = Eq(Rational(20, 10), x / 8)

# Solve the equation
sol = solve(eq, x)

# Display the raw equation to the student
show_work = ce('textarea')
show_work.value = "20 / 10 = x / 8"
show_work.style.fontSize = '35px'
show_work.style.fontWeight = 'bold'
ba(show_work)

# Display the calculated result
result_txt = ce('textarea')
result_txt.value = f"x = {sol[0]}"
result_txt.style.fontSize = '35px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.4_algebra_functions</b></summary>


### `algebra_functions.py`

```python
# algebra_functions.py

from sympy import symbols
from pyside6dom import *

init_window('Algebra Functions', 700, 500)

x = symbols('x')

# Define the math function
f_x = -3*x + 5

# Substitute -2 for x
result = f_x.subs(x, -2)

# Display the original function notation
show_func = ce('textarea')
show_func.value = "f(x) = -3x + 5\nFind f(-2)"
show_func.style.fontSize = '35px'
show_func.style.fontWeight = 'bold'
ba(show_func)

# Display the substitution step and final answer
result_txt = ce('textarea')
result_txt.value = f"f(-2) = -3(-2) + 5\nf(-2) = {result}"
result_txt.style.fontSize = '35px'
result_txt.style.fontWeight = 'bold'
ba(result_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.5_algebra_linear_modeling</b></summary>


### `algebra_linear_modeling.py`

```python
# algebra_linear_modeling.py

from sympy import symbols, Eq
from pyside6dom import *

init_window('Algebra Linear Modeling', 800, 600)

# Math Logic
v, t = symbols('v t')
initial_amount = 42
leak_rate = 0.5

# Volume equals initial amount minus (rate * time)
eq = Eq(v, initial_amount - leak_rate * t)

# UI Construction
# Display the word problem
problem_txt = ce('textarea')
problem_txt.value = (
    "A water cooler has 42 gallons of water.\n"
    "It leaks at a rate of 0.5 gallons per hour.\n\n"
    "Write an equation for the volume (v) remaining\n"
    "after (t) hours."
)
problem_txt.style.fontSize = '24px'
problem_txt.style.fontWeight = 'bold'
problem_txt.style.height = '200px'
ba(problem_txt)

# Display the translated equation
result_txt = ce('textarea')
# We replace the Python 'Eq(v, ...)' formatting with a standard equals sign for reading
result_txt.value = f"Equation:\nv = {eq.rhs}"
result_txt.style.fontSize = '35px'
result_txt.style.fontWeight = 'bold'
result_txt.style.color = 'rgb(100, 200, 100)'
ba(result_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.6_algebra_systems</b></summary>


### `algebra_systems_gui.py`

```python
# algebra_systems_gui.py

from sympy import symbols, Eq, solve
from pyside6dom import *

init_window('Systems of Equations', 700, 550)

x, y = symbols('x y')

# Define the system
eq1 = Eq(2*x - 3*y, 12)
eq2 = Eq(x + y, 1)

# Solve the system
sol = solve((eq1, eq2), (x, y))

# Display the equations
show_work = ce('textarea')
show_work.value = "Equation 1: 2x - 3y = 12\nEquation 2: x + y = 1\n\nFind (x, y)"
show_work.style.fontSize = '30px'
show_work.style.fontWeight = 'bold'
show_work.style.height = '180px'
ba(show_work)

# Extract the values from the dictionary and format them as a coordinate pair
# sol[x] gets the value 3, sol[y] gets the value -2
result_txt = ce('textarea')
result_txt.value = f"Solution:\n(x, y) = ({sol[x]}, {sol[y]})"
result_txt.style.fontSize = '35px'
result_txt.style.fontWeight = 'bold'
result_txt.style.color = 'rgb(100, 200, 255)'
ba(result_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.7_adding_fractions</b></summary>


### `adding_fractions.py`

```python
# adding_fractions.py

from sympy import Rational
from pyside6dom import *

init_window('Adding Fractions', 700, 600)

# We define our fractions
fraction_a = Rational(1, 2)
fraction_b = Rational(1, 3)

# We add the fractions together
total = fraction_a + fraction_b

# We create our div to hold the text
result = ce('div')
# Using str() gives us a clean "1/2 + 1/3 = 5/6" format
result.textContent = "Our Equation:\n" + str(fraction_a) + " + " + str(fraction_b) + " = " + str(total)
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.padding = '2px 10px'
ba(result)

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
```


</details>

---

<details>
<summary><b>Section: 1.8_subtracting_fractions</b></summary>


### `subtracting_fractions.py`

```python
# subtracting_fractions.py

from sympy import Rational
from pyside6dom import *

init_window('Subtracting Fractions', 700, 600)

# We define our same baseline fractions
fraction_a = Rational(1, 2)
fraction_b = Rational(1, 3)

# We subtract the second fraction from the first
total = fraction_a - fraction_b

# We create our div to hold the text
result = ce('div')
result.textContent = "Our Equation:\n" + str(fraction_a) + " - " + str(fraction_b) + " = " + str(total)
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.padding = '2px 10px'
ba(result)

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
```


</details>

---

<details>
<summary><b>Section: 1.9_multiplying_fractions</b></summary>


### `multiplying_fractions.py`

```python
# multiplying_fractions.py

from sympy import Rational
from pyside6dom import *

init_window('Multiplying Fractions', 700, 600)

# We define our same baseline fractions
fraction_a = Rational(1, 2)
fraction_b = Rational(1, 3)

# We multiply the fractions together
total = fraction_a * fraction_b

# We create our div to hold the text
result = ce('div')
result.textContent = "Our Equation:\n" + str(fraction_a) + " * " + str(fraction_b) + " = " + str(total)
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.padding = '2px 10px'
ba(result)

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
```


</details>

---

<details>
<summary><b>Section: fractions_event_property_method</b></summary>


### `fractions_event_property_method.py`

```python
# fractions_event_property_method.py

from sympy import Rational
from pyside6dom import *

init_window('Adding Fractions', 800, 600)

set_theme('''
    button {
        background-color: rgb(0, 0, 0);
        color: rgb(255, 255, 255);
        font-family: Arial;
        font-size: 20px;
        border: 1px solid rgb(255, 255, 255);
    }
    button:hover {
        border-color: rgb(0, 255, 255);
    }
    button:active {
        color: rgb(255, 0, 255);
    }

    input {
        padding: 2px 8px;
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
    }
''')

# We create our calculation logic first so our inputs can reference it
def calculate_addition():
    try:
        num1 = int(input_num1.value)
        den1 = int(input_den1.value)
        num2 = int(input_num2.value)
        den2 = int(input_den2.value)

        fraction_a = Rational(num1, den1)
        fraction_b = Rational(num2, den2)
        total = fraction_a + fraction_b

        result.textContent = f"Our Equation:\n{fraction_a} + {fraction_b} = {total}"
    except ValueError:
        result.textContent = "Please enter valid whole numbers."

# We create our Enter key listener
def check_enter(event):
    if event.key.lower() == 'Enter':
        calculate_addition()

# MAIN ROW CONTAINER
equation_row = ce('div')
equation_row.style.display = 'flex'
equation_row.style.flexDirection = 'row'
equation_row.style.alignItems = 'center'
equation_row.style.gap = '20px'
equation_row.style.margin = '20px'
ba(equation_row)

# FIRST FRACTION (COLUMN)
frac1_col = ce('div')
frac1_col.style.display = 'flex'
frac1_col.style.flexDirection = 'column'
frac1_col.style.gap = '10px'
equation_row.append(frac1_col)

input_num1 = ce('input')
input_num1.placeholder = "Num 1"
input_num1.style.fontSize = '24px'
input_num1.style.textAlign = 'center'
input_num1.onkeyup = check_enter
frac1_col.append(input_num1)

input_den1 = ce('input')
input_den1.placeholder = "Den 1"
input_den1.style.fontSize = '24px'
input_den1.style.textAlign = 'center'
input_den1.onkeyup = check_enter
frac1_col.append(input_den1)

# OPERATOR SIGN
plus_sign = ce('div')
plus_sign.textContent = "+"
plus_sign.style.fontSize = '40px'
plus_sign.style.fontWeight = 'bold'
equation_row.append(plus_sign)

# SECOND FRACTION (COLUMN)
frac2_col = ce('div')
frac2_col.style.display = 'flex'
frac2_col.style.flexDirection = 'column'
frac2_col.style.gap = '10px'
equation_row.append(frac2_col)

input_num2 = ce('input')
input_num2.placeholder = "Num 2"
input_num2.style.fontSize = '24px'
input_num2.style.textAlign = 'center'
input_num2.onkeyup = check_enter
frac2_col.append(input_num2)

input_den2 = ce('input')
input_den2.placeholder = "Den 2"
input_den2.style.fontSize = '24px'
input_den2.style.textAlign = 'center'
input_den2.onkeyup = check_enter
frac2_col.append(input_den2)

# CALCULATE BUTTON
calc_button = ce('button')
calc_button.textContent = "Calculate"
calc_button.onclick = calculate_addition
calc_button.style.fontSize = '24px'
calc_button.style.margin = '20px'
ba(calc_button)

# RESULT DISPLAY
result = ce('div')
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.paddingLeft = '20px'
result.textContent = "Awaiting cadet input..."
ba(result)

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
```


</details>

---

<details>
<summary><b>Section: fractions_standard_dom</b></summary>


### `fractions_standard_dom.py`

```python
# fractions_standard_dom.py

from sympy import Rational
from pyside6dom import *

init_window('Standard DOM Events', 800, 600)

set_theme('''
    button {
        background-color: rgb(0, 0, 0);
        color: rgb(255, 255, 255);
        font-family: Arial;
        font-size: 20px;
        border: 1px solid rgb(255, 255, 255);
    }
    button:hover {
        border-color: rgb(0, 255, 255);
    }
    button:active {
        color: rgb(255, 0, 255);
    }

    input {
        padding: 2px 8px;
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
    }
''')

def calculate_addition():
    try:
        num1 = int(input_num1.value)
        den1 = int(input_den1.value)
        num2 = int(input_num2.value)
        den2 = int(input_den2.value)

        fraction_a = Rational(num1, den1)
        fraction_b = Rational(num2, den2)
        total = fraction_a + fraction_b

        result.textContent = f"Our Equation:\n{fraction_a} + {fraction_b} = {total}"
        
        # Clear inputs and focus back on the first box for the next calculation
        input_num1.value = ""
        input_den1.value = ""
        input_num2.value = ""
        input_den2.value = ""
        input_num1.focus()
    except ValueError:
        result.textContent = "Please enter valid whole numbers."

# Standard DOM event handler
def handle_keydown(event):
    if event.key == 'Enter':
        event.preventDefault()
        ge('calc_button').click()

# MAIN ROW CONTAINER
equation_row = ce('div')
equation_row.style.display = 'flex'
equation_row.style.flexDirection = 'row'
equation_row.style.alignItems = 'center'
equation_row.style.gap = '20px'
equation_row.style.margin = '20px'
ba(equation_row)

# FIRST FRACTION
frac1_col = ce('div')
frac1_col.style.display = 'flex'
frac1_col.style.flexDirection = 'column'
frac1_col.style.gap = '10px'
equation_row.append(frac1_col)

input_num1 = ce('input')
input_num1.placeholder = "Num 1"
input_num1.addEventListener('keydown', handle_keydown)
frac1_col.append(input_num1)

# Horizontal fraction line
line1 = ce('div')
line1.style.borderBottom = '2px solid white'
frac1_col.append(line1)

input_den1 = ce('input')
input_den1.placeholder = "Den 1"
input_den1.addEventListener('keydown', handle_keydown)
frac1_col.append(input_den1)

# OPERATOR
plus_sign = ce('div')
plus_sign.textContent = "+"
equation_row.append(plus_sign)

# SECOND FRACTION
frac2_col = ce('div')
frac2_col.style.display = 'flex'
frac2_col.style.flexDirection = 'column'
frac2_col.style.gap = '10px'
equation_row.append(frac2_col)

input_num2 = ce('input')
input_num2.placeholder = "Num 2"
input_num2.addEventListener('keydown', handle_keydown)
frac2_col.append(input_num2)

# Horizontal fraction line
line2 = ce('div')
line2.style.borderBottom = '2px solid white'
frac2_col.append(line2)

input_den2 = ce('input')
input_den2.placeholder = "Den 2"
input_den2.addEventListener('keydown', handle_keydown)
frac2_col.append(input_den2)

# BUTTON & RESULT
calc_button = ce('button')
calc_button.id = 'calc_button'
calc_button.textContent = "Calculate"
calc_button.onclick = calculate_addition
ba(calc_button)

result = ce('div')
result.textContent = "Awaiting cadet input..."
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.paddingLeft = '20px'
ba(result)

input_num1.focus()
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
```


</details>

---

<details>
<summary><b>Section: fractions_using_onenter</b></summary>


### `fractions_using_onenter.py`

```python
# fractions_using_onenter.py

from sympy import Rational
from pyside6dom import *

init_window('PySide6 DOM Custom Events', 800, 600)

set_theme('''
    body {
        font-family: Arial;
        font-size: 30px;
    }
    button {
        background-color: rgb(0, 0, 0);
        color: rgb(255, 255, 255);
        font-family: Arial;
        font-size: 30px;
        border: 1px solid rgb(255, 255, 255);
    }
    button:hover {
        border-color: rgb(0, 255, 255);
    }
    button:active {
        color: rgb(255, 0, 255);
    }

    input {
        padding: 2px 8px;
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
    }
''')

def calculate_addition():
    try:
        num1 = int(input_num1.value)
        den1 = int(input_den1.value)
        num2 = int(input_num2.value)
        den2 = int(input_den2.value)

        fraction_a = Rational(num1, den1)
        fraction_b = Rational(num2, den2)
        total = fraction_a + fraction_b

        result.textContent = f"Our Equation:\n{fraction_a} + {fraction_b} = {total}"
        
        # We clear inputs and focus back on the first box for the next calculation
        input_num1.value = ""
        input_den1.value = ""
        input_num2.value = ""
        input_den2.value = ""
        input_num1.focus()
    except ValueError:
        result.textContent = "Please enter valid whole numbers."

# MAIN ROW CONTAINER
equation_row = ce('div')
equation_row.style.display = 'flex'
equation_row.style.flexDirection = 'row'
equation_row.style.alignItems = 'center'
equation_row.style.gap = '20px'
equation_row.style.margin = '20px'
ba(equation_row)

# FIRST FRACTION
frac1_col = ce('div')
frac1_col.style.display = 'flex'
frac1_col.style.flexDirection = 'column'
frac1_col.style.gap = '10px'
equation_row.append(frac1_col)

input_num1 = ce('input')
input_num1.placeholder = "Num 1"
input_num1.onenter = calculate_addition
frac1_col.append(input_num1)

# Horizontal fraction line
line1 = ce('div')
line1.style.borderBottom = '2px solid white'
frac1_col.append(line1)

input_den1 = ce('input')
input_den1.placeholder = "Den 1"
input_den1.onenter = calculate_addition
frac1_col.append(input_den1)

# OPERATOR
plus_sign = ce('div')
plus_sign.textContent = "+"
equation_row.append(plus_sign)

# SECOND FRACTION
frac2_col = ce('div')
frac2_col.style.display = 'flex'
frac2_col.style.flexDirection = 'column'
frac2_col.style.gap = '10px'
equation_row.append(frac2_col)

input_num2 = ce('input')
input_num2.placeholder = "Num 2"
input_num2.onenter = calculate_addition
frac2_col.append(input_num2)

# Horizontal fraction line
line2 = ce('div')
line2.style.borderBottom = '2px solid white'
frac2_col.append(line2)

input_den2 = ce('input')
input_den2.placeholder = "Den 2"
input_den2.onenter = calculate_addition
frac2_col.append(input_den2)

# BUTTON & RESULT
calc_button = ce('button')
calc_button.id = 'calc_button'
calc_button.textContent = "Calculate"
calc_button.onclick = calculate_addition
ba(calc_button)

result = ce('div')
result.textContent = "Awaiting cadet input..."
result.style.fontFamily = 'Arial'
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.paddingLeft = '20px'
ba(result)

# Auto-focus the input when the app launches
input_num1.focus()

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
```


</details>

---

<details>
<summary><b>Section: 1.0_foundation</b></summary>


### `matplotlib_telemetry.py`

```python
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
```

### `simple_graph.py`

```python
# simple_graph.py

import matplotlib.pyplot as plt

# Apply the global dark theme style
plt.style.use('dark_background')

# Define sample data
x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 22, 18]

# Initialize the plot and layout
plt.plot(x, y, marker='o', linestyle='-', color='blue')

# Add descriptive labels
plt.title("Sample Line Chart")
plt.xlabel("X-Axis Label")
plt.ylabel("Y-Axis Label")

# Render the chart window
plt.show()

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
```


</details>

---

<details>
<summary><b>Section: 001_scalars_vectors_matrices</b></summary>


### `scalars_vectors_matrices.py`

```python
# scalars_vectors_matrices_textContent.py

import numpy as np
from pyside6dom import *

init_window("Scalars, Vectors, Matrices", 700, 600)

# 0D: The Scalar
scalar_txt = ce('text')
scalar = np.array(5)
# Using \n for line breaks instead of HTML tags
scalar_txt.textContent = f"0D: The Scalar\nScalar: {scalar}"
ba(scalar_txt)

# 1D: The Vector
vector_txt = ce('text')
# A single row of data
vector = np.array([10, 20, 30])
vector_txt.textContent = f"\n1D: The Vector\nVector: {vector}"
ba(vector_txt)

# 2D: The Matrix
matrix_txt = ce('text')
# A grid of data (lists inside a list)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# Plain text naturally preserves NumPy's built-in matrix spacing!
matrix_txt.textContent = f"\n2D: The Matrix\n{matrix}"
ba(matrix_txt)

# Vectorization (The Magic)
vectorization_txt = ce('text')
# Multiply every number in the grid by 10 instantly
multiplied = matrix * 10
vectorization_txt.textContent = f"\nVectorization (The Magic)\nMultiplied by 10:\n{multiplied}"
ba(vectorization_txt)

run_app()

####

'''
0D: The Scalar
Scalar:
 5

1D: The Vector
Vector:
 [10 20 30]

2D: The Matrix
Matrix:
 [[1 2 3]
 [4 5 6]]

Vectorization (The Magic)
Multiplied by 10:
 [[10 20 30]
 [40 50 60]]
'''

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
```

### `scalars_vectors_matrices_innerHTML.py`

```python
# scalars_vectors_matrices_innerHTML.py

import numpy as np
from pyside6dom import *

init_window("Scalars, Vectors, Matrices", 700, 600)

# 0D: The Scalar
scalar_txt = ce('text')
scalar = np.array(5)
# Using <b> for bold headers and <br> for line breaks
scalar_txt.innerHTML = f"<b>0D: The Scalar</b><br>Scalar: {scalar}"
ba(scalar_txt)

# 1D: The Vector
vector_txt = ce('text')
# A single row of data
vector = np.array([10, 20, 30])
vector_txt.innerHTML = f"<br><b>1D: The Vector</b><br>Vector: {vector}"
ba(vector_txt)

# 2D: The Matrix
matrix_txt = ce('text')
# A grid of data (lists inside a list)
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
# Using <pre> preserves NumPy's built-in spacing and line breaks for the grid
matrix_txt.innerHTML = f"<br><b>2D: The Matrix</b><br><pre>{matrix}</pre>"
ba(matrix_txt)

# Vectorization (The Magic)
vectorization_txt = ce('text')
# Multiply every number in the grid by 10 instantly
multiplied = matrix * 10
vectorization_txt.innerHTML = f"<br><b>Vectorization (The Magic)</b><br>Multiplied by 10:<br><pre>{multiplied}</pre>"
ba(vectorization_txt)

run_app()

####

'''
0D: The Scalar
Scalar:
 5

1D: The Vector
Vector:
 [10 20 30]

2D: The Matrix
Matrix:
 [[1 2 3]
 [4 5 6]]

Vectorization (The Magic)
Multiplied by 10:
 [[10 20 30]
 [40 50 60]]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 002_generating_grids_and_zeros</b></summary>


### `generating_grids_and_zeros.py`

```python
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
```


</details>

---

<details>
<summary><b>Section: 003_one_dimensional_array</b></summary>


### `one_dimensional_array.py`

```python
# one_dimensional_array.py

import numpy as np
from pyside6dom import *

init_window("One Dimensional Array", 400, 300)

# We make a one-dimensional array
our_array = np.array([10, 17, 41, 19, 16, 8])

# Display it
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
```


</details>

---

<details>
<summary><b>Section: 001_vector_addition</b></summary>


### `vector_addition.py`

```python
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
```


</details>

---

<details>
<summary><b>Section: 002_broadcasting_and_scaling</b></summary>


### `broadcasting_and_scaling.py`

```python
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
```


</details>

---

<details>
<summary><b>Section: 001_boolean_masking</b></summary>


### `boolean_masking.py`

```python
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
```


</details>

---

<details>
<summary><b>Section: 1.1_opencv_studio</b></summary>


### `opencv_studio.py`

```python
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
```


</details>

---

<details>
<summary><b>Section: show_with_innerHTML</b></summary>


### `read_csv_show_with_innerHTML.py`

```python
# read_csv_show_with_innerHTML.py

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV File', 700, 400)

output = ce('text')
# Inject the Pandas HTML directly into the text element
output.innerHTML = theData.to_html(index=False, border=1)
ba(output)

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
```


</details>

---

<details>
<summary><b>Section: show_with_textContent</b></summary>


### `read_csv_show_with_textContent.py`

```python
# read_csv_show_with_textContent.py

import pandas as pd

from pyside6dom import *

theData = pd.read_csv('data.csv')

print(theData.to_string())

init_window('Read CSV File', 700, 400)

output = ce('text')
output.textContent = theData.to_string()
ba(output)

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
```


</details>

---

<details>
<summary><b>Section: 1.2_read_csv_len</b></summary>


### `read_csv_len.py`

```python
# read_csv_len.py

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

output_text = ce('text')
output_text.innerHTML = theData.to_html(index=False, border=1)
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
4 people
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
'''

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
```

### `read_csv_len_with_padding_replace.py`

```python
# read_csv_len_with_padding_replace.py

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

# Generate the raw HTML string from Pandas
raw_html = theData.to_html(index=False, border=1)

# Inject standard HTML cellpadding directly into the table tag
padded_html = raw_html.replace('<table', '<table cellpadding="8"')

output_text = ce('text')
output_text.innerHTML = padded_html
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
4 people
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

### `read_csv_len_with_padding_style.py`

```python
# read_csv_len_with_padding_style.py

import pandas as pd
from pyside6dom import *

theData = pd.read_csv('data.csv')

init_window('Read CSV len', 700, 400)

how_many_txt = ce('text')
how_many_txt.textContent = f"{len(theData)} people"
ba(how_many_txt)

# Generate the raw HTML string from Pandas (no need to force the border here anymore)
raw_html = theData.to_html(index=False)

# Write pure CSS exactly how a web developer would expect to
table_css = """
<style>
    table {
        border-collapse: collapse;
        margin-top: 10px;
    }
    th, td {
        padding: 8px 15px; 
        border: 1px solid white;
    }
    th {
        background-color: #333333;
        font-weight: bold;
    }
</style>
"""

output_text = ce('text')
# We just glue the CSS and the HTML together, like a real webpage
output_text.innerHTML = table_css + raw_html
ba(output_text)

print(f"{len(theData)} people")
print(theData.to_string())

run_app()

####

'''
4 people
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.3_read_csv_info</b></summary>


### `read_csv_info.py`

```python
# read_csv_info.py

import pandas as pd
import io
from pyside6dom import *

init_window('Read CSV Info', 700, 600)

theData = pd.read_csv('data.csv')

# Display the Data as a beautiful HTML table
# Because of our engine upgrade, to_html() automatically gets padded and styled
table_txt = ce('text')
table_txt.innerHTML = theData.to_html(index=False)
ba(table_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>DataFrame Info:</b>"
ba(sep_txt)

# Catch the .info() output
buffer = io.StringIO()
theData.info(buf=buffer)
info_string = buffer.getvalue()

# Display the .info() using textContent
# We use textContent here so the terminal spacing and alignment stays perfect
info_txt = ce('text')
info_txt.textContent = info_string
ba(info_txt)

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
```

### `read_csv_info_textContent.py`

```python
# read_csv_info.py

# read_csv_info.py

import pandas as pd
import io
from pyside6dom import *

init_window('Read CSV Info', 700, 600)

theData = pd.read_csv('data.csv')

# Display the raw Data
data_txt = ce('text')
data_txt.textContent = theData.to_string()
ba(data_txt)

# Display the Separator
sep_txt = ce('text')
sep_txt.textContent = "\n-------------------------------\n"
ba(sep_txt)

# Catch and Display the .info()
# We create an empty "catcher's mitt"
buffer = io.StringIO()

# We tell Pandas to print the info into the buffer instead of the console
theData.info(buf=buffer)

# We grab the caught text out of the buffer
info_string = buffer.getvalue()

# Now we can display it in the DOM!
info_txt = ce('text')
info_txt.textContent = info_string
ba(info_txt)

run_app()

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
-------------------------------
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4 entries, 0 to 3
Data columns (total 2 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    4 non-null      object
 1   Score   4 non-null      int64
dtypes: int64(1), object(1)
memory usage: 196.0+ bytes
None
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.4_read_csv_describe</b></summary>


### `read_csv_describe.py`

```python
# read_csv_describe.py

import pandas as pd
from pyside6dom import *

init_window('Read CSV Describe', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data as a beautiful HTML table
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Statistical Summary (.describe):</b>"
ba(sep_txt)

# Display the describe() data as a second HTML table
# Because .describe() returns a DataFrame, it has .to_html() built right in.
# (We leave the index on here because the index contains the labels like 'mean', 'min', 'max')
desc_txt = ce('text')
desc_txt.innerHTML = theData.describe().to_html()
ba(desc_txt)

run_app()

####

'''
             Name  Score
0         Tabitha  98
1            Jane  95
2        Jennifer  90
3  Alison, Martin  89
-------------------------------
           Score
count   4.000000
mean   93.000000
std     4.242641
min    89.000000
25%    89.750000
50%    92.500000
75%    95.750000
max    98.000000
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.5_read_csv_filter_by_year</b></summary>


### `read_csv_filter_by_year.py`

```python
# read_csv_filter_by_year.py

import pandas as pd
from pyside6dom import *

init_window('Filter by Year', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data as a beautiful HTML table
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Filtered Data (Year == 2026):</b>"
ba(sep_txt)

# Filter the data
# Show only the rows where the 'Year' column equals 2026
recent_data = theData[theData['Year'] == 2026]

# Display the filtered subset as its own HTML table
filtered_txt = ce('text')
filtered_txt.innerHTML = recent_data.to_html(index=False)
ba(filtered_txt)

run_app()

####

'''
             Name  Score  Year
0         Tabitha  98  2026
1            Jane  95  2025
2        Jennifer  90  2025
3  Alison, Martin  89  2024
-------------------------------
      Name  Score  Year
0  Tabitha  98  2026
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 1.6_read_csv_filter_by_name</b></summary>


### `read_csv_filter_by_name.py`

```python
# read_csv_filter_by_name.py

import pandas as pd
from pyside6dom import *

init_window('Filter by Name', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Filtered Data (Name == 'Jane'):</b>"
ba(sep_txt)

# Filter the data for a specific string
# Show only rows where the 'Name' column is 'Jane'
jane_data = theData[theData['Name'] == 'Jane']

# Display the filtered subset
filtered_txt = ce('text')
filtered_txt.innerHTML = jane_data.to_html(index=False)
ba(filtered_txt)

run_app()

####

'''
             Name  Score  Year
0         Tabitha  98  2026
1            Jane  95  2025
2        Jennifer  90  2025
3  Alison, Martin  89  2024
-------------------------------
   Name  Score  Year
1  Jane  95  2025
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.7_read_csv_filter_by_columns</b></summary>


### `read_csv_filter_by_columns.py`

```python
# read_csv_filter_by_columns.py

import pandas as pd
from pyside6dom import *

init_window('Filter by Columns', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Isolated Columns ('Name' and 'Job'):</b>"
ba(sep_txt)

# Isolate the specific columns
# Notice the double brackets [[ ]] - this passes a list of columns to Pandas
isolated_columns = theData[['Name', 'Job']]

# Display the new subset
isolated_txt = ce('text')
isolated_txt.innerHTML = isolated_columns.to_html(index=False)
ba(isolated_txt)

run_app()

####

'''
Name  Score  Year  Team  Job
0 Tabitha  98  2026   Red Engineer
1 Jane  95  2025  Blue  Computer Scientist
2 Jennifer  90  2025  Red  AI Specialist
3  Alison, Martin  89  2024  Blue  Robotics Technician
-------------------------------
             Name               Job
0         Tabitha  Engineer
1            Jane  Computer Scientist
2        Jennifer  AI Specialist
3  Alison, Martin  Robotics Technician
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.8_read_csv_show_scores</b></summary>


### `read_csv_show_scores.py`

```python
# read_csv_show_scores.py

import pandas as pd

theData = pd.read_csv('data.csv')

print(theData["Score"])

####

'''
0  98
1  95
2  90
3  89
Name: Score, dtype: int64
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 1.9_read_csv_show_names</b></summary>


### `read_csv_show_names.py`

```python
# read_csv_show_names.py

import pandas as pd
from pyside6dom import *

init_window('Show Names', 700, 600)

theData = pd.read_csv('data.csv')

# Display the original Data
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Isolated Column ('Name') as a Series:</b>"
ba(sep_txt)

# Extract the single column
# Using single brackets returns a Pandas 'Series' instead of a 'DataFrame'
names_series = theData["Name"]

# Display the Series
# We use .to_frame() to convert the 1D Series back into a 2D table so 
# our engine can automatically style it with the beautiful CSS!
names_txt = ce('text')
names_txt.innerHTML = names_series.to_frame().to_html(index=False)
ba(names_txt)

run_app()

####

'''
0  Tabitha
1  Jane
2  Jennifer
3  Alison, Martin
Name: Name, dtype: object
'''

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
```


</details>

---

<details>
<summary><b>Section: 2.1_write_and_read_csv</b></summary>


### `write_and_read_csv_data.py`

```python
# write_and_read_csv_data.py

import pandas as pd
import os
from pyside6dom import *

def create_mission_data():
    # We create a CSV string where some data points contain commas.
    # Notice how the names and locations are wrapped in quotes.
    csv_content = """ID,Name,Last_Known_Location,Status
101,"Smith, John","Sector 4, Alpha",Rescued
102,"Doe, Jane","Sector 7, Beta",Awaiting Rescue
103,"O'Connor, Sarah","Sector 4, Alpha",Rescued
104,"Patel, Ravi","Sector 9, Delta",Awaiting Rescue"""

    # Write it to a file
    with open('rescue_manifest.csv', 'w') as file:
        file.write(csv_content)
        
    return "System: 'rescue_manifest.csv' generated on local drive."

# Start the Engine
init_window('Write and Read CSV', 700, 650)

# Generate the file and show the status message
status_msg = create_mission_data()

status_txt = ce('text')
status_txt.textContent = f"{status_msg}\n\n1. Loading the Rescue Manifest..."
ba(status_txt)

# Read the entire file into a DataFrame
df = pd.read_csv('rescue_manifest.csv')

# Displaying the full DataFrame
header_1 = ce('text')
header_1.innerHTML = "<br><b>2. Displaying the DataFrame:</b>"
ba(header_1)

df_txt = ce('text')
df_txt.innerHTML = df.to_html(index=False)
ba(df_txt)

# Isolating a Specific Column (Just the Names)
header_2 = ce('text')
header_2.innerHTML = "<br><hr><br><b>3. Isolating a Specific Column (Just the Names):</b>"
ba(header_2)

# Convert the Series to a Frame so our engine styles it perfectly
names_txt = ce('text')
names_txt.innerHTML = df['Name'].to_frame().to_html(index=False)
ba(names_txt)

run_app()

####

'''
System: 'rescue_manifest.csv' generated on local drive.

1. Loading the Rescue Manifest...

2. Displaying the DataFrame:
    ID             Name Last_Known_Location           Status
0  101  Smith, John  Sector 4, Alpha  Rescued
1  102  Doe, Jane  Sector 7,  Beta  Awaiting Rescue
2  103  O'Connor, Sarah  Sector 4, Alpha  Rescued
3  104  Patel, Ravi  Sector 9, Delta  Awaiting Rescue

3. Isolating a Specific Column (Just the Names):
0  Smith, John
1  Doe, Jane
2  O'Connor, Sarah
3  Patel, Ravi
Name: Name, dtype: object
'''

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
```


</details>

---

<details>
<summary><b>Section: 3.1_read_csv_make_chart</b></summary>


### `read_csv_make_chart.py`

```python
# read_csv_make_chart.py

import pandas as pd
import matplotlib.pyplot as plt
import os
from pyside6dom import *

init_window('Read CSV Chart', 800, 800)

theData = pd.read_csv('data.csv')

# Display the raw Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Sales Bar Chart:</b><br>"
ba(sep_txt)

# Create the bar chart using Pandas/Matplotlib
theData.plot(kind='bar', x='Month', y='Sales')

# Instead of plt.show(), we save it as an image
chart_filename = 'sales_chart.png'
plt.savefig(chart_filename, bbox_inches='tight') # bbox_inches keeps the edges clean
plt.close() # Closes it in matplotlib's invisible background to free up memory

# Load the image into the PySide6 DOM using your engine's img tag
chart_img = ce('img')
chart_img.src = chart_filename
chart_img.width = 600  # our engine's proportional sizing will auto-calculate the height
ba(chart_img)

run_app()

####

'''
Name  Score  Year  Team  Job    Month  Sales
0  Tabitha  98  2026  Red  Engineer  January  4000
1  Jane  95  2025  Blue  Computer Scientist  August  5000
2  Jennifer  90  2025  Red  AI Specialist  June  1000
3  Alison, Martin  89  2024  Blue  Robotics Technician  March  500
'''

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
```


</details>

---

<details>
<summary><b>Section: 3.2_read_csv_make_chart_dark</b></summary>


### `read_csv_make_chart_dark.py`

```python
# read_csv_make_chart_dark.py

import pandas as pd
import matplotlib.pyplot as plt
import os
from pyside6dom import *

init_window('Read CSV Chart Dark', 800, 800)

# Turn on the worldwide dark theme for all matplotlib charts
plt.style.use('dark_background')

# Load our data
theData = pd.read_csv('data.csv')

# Display the raw Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = theData.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Dark Theme Sales Bar Chart:</b><br>"
ba(sep_txt)

# Create the bar chart and force the bars to be neon cyan
theData.plot(kind='bar', x='Month', y='Sales', color='#00FFFF')

# Save the dark chart as an image
chart_filename = 'sales_chart_dark.png'
plt.savefig(chart_filename, bbox_inches='tight') 
plt.close() # Close it in the background to free up memory

# Load the image into the DOM
chart_img = ce('img')
chart_img.src = chart_filename
chart_img.width = 600  
ba(chart_img)

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
```


</details>

---

<details>
<summary><b>Section: 4.1_read_csv_convert_to_list_of_dictionaries</b></summary>


### `read_csv_convert_to_list_of_dictionaries.py`

```python
# read_csv_convert_to_list_of_dictionaries.py

import pandas as pd
import json
from pyside6dom import *

init_window('Convert to List of Dictionaries', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Converted to List of Dictionaries (JSON Array of Objects):</b><br>"
ba(sep_txt)

# Convert the DataFrame to a List of Dictionaries
# orient='records' creates the classic Array of Objects format
data_array = df.to_dict(orient='records')

# Format the Python dictionary into a beautiful JSON string
# indent=4 gives it that perfect code-editor spacing
formatted_json = json.dumps(data_array, indent=4)

#  Display the formatted string
# We use textContent here so the GUI preserves all the spaces and line breaks
json_txt = ce('text')
json_txt.textContent = formatted_json
ba(json_txt)

run_app()

####

'''
[
    {
        'Name': 'Tabitha',
        'Score': 98
    },

    {
        'Name': 'Jane',
        'Score': 95
    },
    
    {
        'Name': 'Jennifer',
        'Score': 90
    },
    
    {
        'Name': 'Alison,
        Martin', 'Score': 89
    }
]
'''

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
```


</details>

---

<details>
<summary><b>Section: 4.2_read_csv_convert_to_list_of_dictionaries_show_names</b></summary>


### `read_csv_convert_to_list_of_dictionaries_show_names.py`

```python
# read_csv_convert_to_list_of_dictionaries_show_names.py

import pandas as pd
from pyside6dom import *

init_window('Show Names from Dictionaries', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Looping Through Array of Objects:</b><br>"
ba(sep_txt)

# Convert the DataFrame to a List of Dictionaries (Array of Objects)
data_array = df.to_dict(orient='records')

# Loop through the array and build UI elements dynamically
for person in data_array:
    # Instead of printing to the console, we create a new text element for each person
    person_txt = ce('text')
    
    # We grab the 'Name' and 'Score' exactly like a JavaScript object
    person_txt.textContent = f"{person['Name']}: {person['Score']}"
    
    # Add it to the screen
    ba(person_txt)

run_app()

####

'''
Tabitha: 98
Jane: 95
Jennifer: 90
Alison, Martin: 89
'''

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
```


</details>

---

<details>
<summary><b>Section: 4.3_read_csv_convert_to_list_of_dictionaries_export_json</b></summary>


### `read_csv_convert_to_list_of_dictionaries_export_json.py`

```python
# read_csv_convert_to_list_of_dictionaries_export_json.py

import pandas as pd
import json
from pyside6dom import *

init_window('Export CSV to JSON', 700, 750)

# Load the CSV and create the array of objects
df = pd.read_csv('data.csv')
data_array = df.to_dict(orient='records')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Write the array to a JSON file on the local drive
with open('exported_data.json', 'w') as json_file:
    # json.dump() physically writes the file to the drive
    json.dump(data_array, json_file, indent=4)

# Display a clean separator and a success message
status_txt = ce('text')
status_txt.innerHTML = "<br><hr><br><b style='color: #00ffcc;'>Status: Successfully exported 'exported_data.json' to local drive!</b><br><br><b>File Preview:</b>"
ba(status_txt)

# Show a preview of the JSON data we just saved
preview_txt = ce('text')
# We use json.dumps() here to create a formatted string just for the visual preview
preview_txt.textContent = json.dumps(data_array, indent=4)
ba(preview_txt)

run_app()

####

'''
[
    {
        "Name": "Tabitha",
        "Score": 98
    },
    {
        "Name": "Jane",
        "Score": 95
    },
    {
        "Name": "Jennifer",
        "Score": 90
    },
    {
        "Name": "Alison, Martin",
        "Score": 89
    }
]
'''

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
```


</details>

---

<details>
<summary><b>Section: 5.1_read_csv_convert_to_dictionary_of_dictionaries</b></summary>


### `read_csv_convert_to_dictionary_of_dictionaries.py`

```python
# read_csv_convert_to_dictionary_of_dictionaries.py

import pandas as pd
import json
from pyside6dom import *

init_window('Convert to Dictionary of Dictionaries', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Converted to Dictionary of Dictionaries (Lookup Table):</b><br>"
ba(sep_txt)

# Convert the DataFrame to a Dict of Dicts
# By setting 'Name' as the index first, the names become the master keys
data_obj = df.set_index('Name').to_dict(orient='index')

# Format the Python dictionary into a beautiful JSON string
formatted_json = json.dumps(data_obj, indent=4)

# Display the formatted string
# textContent perfectly preserves our indent=4 spacing
json_txt = ce('text')
json_txt.textContent = formatted_json
ba(json_txt)

run_app()

####

'''
{'Tabitha': {'Score': 98}, 'Jane': {'Score': 95}, 'Jennifer': {'Score': 90}, 'Alison, Martin': {'Score': 89}}
'''

'''
{
    'Tabitha':
    {
        'Score': 98
    },

    'Jane':
    {
        'Score': 95
    },

    'Jennifer':
    {
        'Score': 90
    },

    'Alison, Martin':
    {
        'Score': 89
    }
}
'''

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
```


</details>

---

<details>
<summary><b>Section: 5.2_read_csv_convert_to_dictionary_of_dictionaries_show_names</b></summary>


### `read_csv_convert_to_dictionary_of_dictionaries_show_names.py`

```python
# read_csv_convert_to_dictionary_of_dictionaries_show_names.py

import pandas as pd
from pyside6dom import *

init_window('Show Names from Dictionary of Dictionaries', 700, 600)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Display a clean web-style separator
sep_txt = ce('text')
sep_txt.innerHTML = "<br><hr><br><b>Looping Through Dictionary Keys (Names):</b><br>"
ba(sep_txt)

# Convert the DataFrame to a Dict of Dicts
# 'Name' becomes the master key for each record
data_dict = df.set_index('Name').to_dict(orient='index')

# Loop through the keys!
# This behaves exactly like a 'for...in' loop in vanilla JavaScript.
for name in data_dict:
    # Create a brand new text element for each name
    name_txt = ce('text')

    # We display the name (the dictionary key)
    name_txt.textContent = f"Master Key: {name}"
    
    # Append it to the screen
    ba(name_txt)

run_app()

####

'''
Tabitha
Jane
Jennifer
Alison, Martin
'''

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
```


</details>

---

<details>
<summary><b>Section: 5.3_read_csv_convert_to_dictionary_of_dictionaries_export_json</b></summary>


### `read_csv_convert_to_dictionary_of_dictionaries_export_json.py`

```python
# read_csv_convert_to_dictionary_of_dictionaries_export_json.py

import pandas as pd
import json
from pyside6dom import *

init_window('Export Dictionary of Dictionaries to JSON', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Convert the DataFrame to a Dictionary of Dictionaries
# Setting 'Name' as the index makes the names the master keys
data_dict = df.set_index('Name').to_dict(orient='index')

# Write the dictionary to a JSON file on the local drive
# We include encoding='utf-8' just in case there are any special characters in the data!
with open('exported_dict_data.json', 'w', encoding='utf-8') as json_file:
    json.dump(data_dict, json_file, indent=4)

# Display a clean separator and a styled success message
status_txt = ce('text')
status_txt.innerHTML = "<br><hr><br><b style='color: #00ffcc;'>Status: Successfully exported 'exported_dict_data.json' to local drive!</b><br><br><b>File Preview:</b>"
ba(status_txt)

# Show a preview of the JSON data we just saved
preview_txt = ce('text')
# We use json.dumps() to create a formatted string for the visual preview
preview_txt.textContent = json.dumps(data_dict, indent=4)
ba(preview_txt)

run_app()

####

'''
{
    "Tabitha": {
        "Score": 98
    },
    "Jane": {
        "Score": 95
    },
    "Jennifer": {
        "Score": 90
    },
    "Alison, Martin": {
        "Score": 89
    }
}
'''

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
```


</details>

---

<details>
<summary><b>Section: 5.4_read_csv_convert_to_dictionary_of_dictionaries_filter_by_name</b></summary>


### `read_csv_convert_to_dictionary_of_dictionaries_filter_by_name.py`

```python
# read_csv_convert_to_dictionary_of_dictionaries_filter_by_name.py

import pandas as pd
import json
from pyside6dom import *

init_window('Instant Lookup by Name', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Create the Lookup Table (Dictionary of Dictionaries)
# 'Name' is set as the index, becoming the master key
data_dict = df.set_index('Name').to_dict(orient='index')

# Display the List of Names (The Keys)
sep_1 = ce('text')
sep_1.innerHTML = "<br><hr><br><b>List of Names (Master Keys):</b>"
ba(sep_1)

for name in data_dict.keys():
    name_txt = ce('text')
    # Adding a clean HTML bullet point (&bull;) for visual styling
    name_txt.innerHTML = f"&bull; {name}"
    ba(name_txt)

# Perform the Instant Lookup
sep_2 = ce('text')
sep_2.innerHTML = "<br><hr><br><b style='color: #00ffcc;'>Instant Data Lookup (Tabitha):</b><br>"
ba(sep_2)

# Grab Tabitha's data directly and format it as a beautiful JSON string
tabitha_data = data_dict['Tabitha']
formatted_tabitha = json.dumps(tabitha_data, indent=4)

lookup_txt = ce('text')
# We use textContent here to preserve all the line breaks and spaces
lookup_txt.textContent = f"{formatted_tabitha}"
ba(lookup_txt)

run_app()

####

'''
List of Names (Keys)
Tabitha
Jane
Jennifer
Alison, Martin

Instant Data Lookup
Tabitha's data: {'Score': 98}
'''

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
```


</details>

---

<details>
<summary><b>Section: 5.5_read_csv_convert_to_dictionary_of_dictionaries_export_json_direct</b></summary>


### `read_csv_convert_to_dictionary_of_dictionaries_export_json_direct.py`

```python
# read_csv_convert_to_dictionary_of_dictionaries_export_json_direct.py

import pandas as pd
from pyside6dom import *

init_window('Direct Export to JSON', 700, 750)

# Load the CSV
df = pd.read_csv('data.csv')

# Display the original Data as an HTML table
data_txt = ce('text')
data_txt.innerHTML = df.to_html(index=False)
ba(data_txt)

# Set the index to 'Name' and export directly to a formatted JSON file
export_filename = 'exported_dictionary_data.json'
df.set_index('Name').to_json(export_filename, orient='index', indent=4)

# Display a clean separator and a styled success message
status_txt = ce('text')
status_txt.innerHTML = f"<br><hr><br><b style='color: #00ffcc;'>Status: Successfully exported '{export_filename}' in a single line!</b><br><br><b>File Verification (Reading from drive):</b>"
ba(status_txt)

# Read the newly created file back from the hard drive to prove it exists
with open(export_filename, 'r', encoding='utf-8') as f:
    saved_json_content = f.read()

# Show the exact contents of the file on the screen
preview_txt = ce('text')
preview_txt.textContent = saved_json_content
ba(preview_txt)

run_app()

####

'''
{
    "Tabitha":{
        "Score":98
    },
    "Jane":{
        "Score":95
    },
    "Jennifer":{
        "Score":90
    },
    "Alison, Martin":{
        "Score":89
    }
}
'''

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
```


</details>

---

<details>
<summary><b>Section: 6.1_earthquake_realtime_data</b></summary>


### `earthquake_realtime_data.py`

```python
# earthquake_realtime_data.py

import pandas as pd
from pyside6dom import *

init_window('Real-Time Earthquake Data', 1100, 700)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>USGS Real-Time Earthquake Monitor (Past 24 Hours)</b><br><hr><br>"
ba(title_txt)

# Fetch the live data directly from the USGS servers
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
theData = pd.read_csv(url)

# Display the live data using the new smooth-scrolling engine component!
data_view = ce('table_view')
data_view.innerHTML = theData.to_html(index=False)
ba(data_view)

run_app()

####

'''
This app will take longer to load on older computers and will scroll slower.
This is because the Earthquake data is thousands and thousands of lines!

On the next tutorial we show the optimized version, where we only load some at a time!
'''

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
```

### `earthquake_realtime_data_local_testing.py`

```python
# earthquake_realtime_data_local_testing.py

import sys
import os

# Local Testing
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) 
sys.path.insert(0, project_root)
# --------------------------

import pandas as pd
from pyside6dom import *

init_window('Real-Time Earthquake Data', 1100, 700)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>USGS Real-Time Earthquake Monitor (Past 24 Hours)</b><br><hr><br>"
ba(title_txt)

# Fetch the live data directly from the USGS servers
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
theData = pd.read_csv(url)

# Display the live data using the new smooth-scrolling engine component!
data_view = ce('table_view')
data_view.innerHTML = theData.to_html(index=False)
ba(data_view)

run_app()

####

'''
This app will take longer to load on older computers and will scroll slower.
This is because the Earthquake data is thousands and thousands of lines!

On the next tutorial we show the optimized version, where we only load some at a time!
'''

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
```


</details>

---

<details>
<summary><b>Section: 6.2_earthquake_realtime_data_optimized</b></summary>


### `earthquake_realtime_data_optimized.py`

```python
# earthquake_realtime_data_optimized.py

import pandas as pd
from pyside6dom import *

init_window('Real-Time Earthquakes (Optimized)', 1200, 700)

# Fetch the live data
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
theData = pd.read_csv(url)

# Find out exactly how many rows (earthquakes) are in the data today!
total_quakes = len(theData)

# Add a stylish dashboard title with the live count
title_txt = ce('text')
title_txt.innerHTML = f"<b style='color: #00ffcc; font-size: 18px;'>USGS Real-Time Earthquake Monitor</b><br>Worldwide Earthquakes in the past 24 hours: <b>{total_quakes}</b><br><hr><br>"
ba(title_txt)

# THE SPEED FIX: Grab only the first 50 rows
# This prevents the HTML renderer from overloading your computer's memory
recent_50 = theData.head(50)

# Create the scrollable container for the table
table_container = ce('scroll_div')
table_container.style.border = '1px solid #444'
ba(table_container)

# Convert the optimized 50 rows to HTML
data_txt = ce('text')
data_txt.innerHTML = recent_50.to_html(index=False)

# Append the data text INTO the scroll container (not the main window)
ba(data_txt, table_container)

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
```

### `earthquake_realtime_data_optimized_local_testing.py`

```python
# earthquake_realtime_data_optimized_local_testing.py

# earthquake_realtime_data_optimized.py

import sys
import os

# Local Testing: Go exactly THREE levels up to the root
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) 
sys.path.insert(0, project_root)
# --------------------------

import pandas as pd
from pyside6dom import *

init_window('Real-Time Earthquakes (Optimized)', 1200, 700)

# Fetch the live data
url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.csv'
theData = pd.read_csv(url)

# Find out exactly how many rows (earthquakes) are in the data today!
total_quakes = len(theData)

# Add a stylish dashboard title with the live count
title_txt = ce('text')
title_txt.innerHTML = f"<b style='color: #00ffcc; font-size: 18px;'>USGS Real-Time Earthquake Monitor</b><br>Worldwide Earthquakes in the past 24 hours: <b>{total_quakes}</b><br><hr><br>"
ba(title_txt)

# THE SPEED FIX: Grab only the first 50 rows
# This prevents the HTML renderer from overloading your computer's memory
recent_50 = theData.head(50)

# Create the scrollable container for the table
table_container = ce('scroll_div')
table_container.style.border = '1px solid #444'
ba(table_container)

# Convert the optimized 50 rows to HTML
data_txt = ce('text')
data_txt.innerHTML = recent_50.to_html(index=False)

# Append the data text INTO the scroll container (not the main window)
ba(data_txt, table_container)

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
```


</details>

---

<details>
<summary><b>Section: 1.1_liter</b></summary>


### `dir_constants.py`

```python
# dir_constants.py

from pyside6dom import *
from scipy import constants

init_window('Show All Constants', 700, 600)

the_constants = dir(constants)

result = ce('textarea')
result.value = f" constants: {the_constants}"
result.style.fontSize = '22px'
result.style.fontWeight = 'bold'
result.style.color = 'rgb(0, 255, 255)'
result.style.padding = '20px 20px'
ba(result)

run_app()

####

'''
constants: ['Avogadro', 'Boltzmann', 'Btu', 'Btu_IT', 'Btu_th', 'ConstantWarning', 'G', 'Julian_year', 'N_A', 'Planck', 'R', 'Rydberg', 'Stefan_Boltzmann', 'Wien', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '_codata', '_constants', '_obsolete_constants', 'acre', 'alpha', 'angstrom', 'arcmin', 'arcminute', 'arcsec', 'arcsecond', 'astronomical_unit', 'atm', 'atmosphere', 'atomic_mass', 'atto', 'au', 'bar', 'barrel', 'bbl', 'blob', 'c', 'calorie', 'calorie_IT', 'calorie_th', 'carat', 'centi', 'codata', 'constants', 'convert_temperature', 'day', 'deci', 'degree', 'degree_Fahrenheit', 'deka', 'dyn', 'dyne', 'e', 'eV', 'electron_mass', 'electron_volt', 'elementary_charge', 'epsilon_0', 'erg', 'exa', 'exbi', 'femto', 'fermi', 'find', 'fine_structure', 'fluid_ounce', 'fluid_ounce_US', 'fluid_ounce_imp', 'foot', 'g', 'gallon', 'gallon_US', 'gallon_imp', 'gas_constant', 'gibi', 'giga', 'golden', 'golden_ratio', 'grain', 'gram', 'gravitational_constant', 'h', 'hbar', 'hectare', 'hecto', 'horsepower', 'hour', 'hp', 'inch', 'k', 'kgf', 'kibi', 'kilo', 'kilogram_force', 'kmh', 'knot', 'lambda2nu', 'lb', 'lbf', 'light_year', 'liter', 'litre', 'long_ton', 'm_e', 'm_n', 'm_p', 'm_u', 'mach', 'mebi', 'mega', 'metric_ton', 'micro', 'micron', 'mil', 'mile', 'milli', 'minute', 'mmHg', 'mph', 'mu_0', 'nano', 'nautical_mile', 'neutron_mass', 'nu2lambda', 'ounce', 'oz', 'parsec', 'pebi', 'peta', 'physical_constants', 'pi', 'pico', 'point', 'pound', 'pound_force', 'precision', 'proton_mass', 'psi', 'pt', 'quecto', 'quetta', 'ronna', 'ronto', 'short_ton', 'sigma', 'slinch', 'slug', 'speed_of_light', 'speed_of_sound', 'stone', 'survey_foot', 'survey_mile', 'tebi', 'tera', 'test', 'ton_TNT', 'torr', 'troy_ounce', 'troy_pound', 'u', 'unit', 'value', 'week', 'yard', 'year', 'yobi', 'yocto', 'yotta', 'zebi', 'zepto', 'zero_Celsius', 'zetta']
'''

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
```

### `liter.py`

```python
# liter.py

from pyside6dom import *
from scipy import constants

init_window('Our App', 700, 600)

result = ce('div')
result.textContent = f" liter: {constants.liter}"
result.style.fontSize = '100px'
result.style.fontWeight = 'bold'
result.style.color = 'rgb(0, 255, 255)'
result.style.padding = '20px 20px'
ba(result)

run_app()

####

'''
scipy.constants.liter returns the value of 1 liter in cubic meters (m³), which is exactly 0.001. We can also use the spelling variant scipy.constants.litre
'''

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
```

### `liters_to_cubic_meters.py`

```python
# liters_to_cubic_meters.py

from pyside6dom import *
from scipy import constants

init_window('Our App', 700, 600)

set_theme('''
    .headline
    {
        font-size: 30px;
        font-weight: bold;
        color: rgb(0, 255, 255);
        padding: 20px 20px;
    }
''')

result_container = ce('div')
result_container.style.display = 'flex'
result_container.style.flexDirection = 'column'
ba(result_container)

# Get the conversion factor (1 liter in m^3)
print(constants.liter)  
conversion_factor = ce('textarea')
conversion_factor.value = f" conversion factor: {constants.liter}"
conversion_factor.className = 'headline'
result_container.append(conversion_factor)
# Output: 0.001

# Convert 500 liters to cubic meters
example = 500 * constants.liter

converted_liters = ce('textarea')
converted_liters.value = f" converted liters to cubic meters: 500 * {constants.liter} equals {example}"
converted_liters.className = 'headline'
result_container.append(converted_liters)
# Output: 0.5

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
```

### `metric_prefixes.py`

```python
# metric_prefixes.py

from pyside6dom import *
from scipy import constants

init_window('Metric Prefixes', 700, 600)

yotta = constants.yotta  #1e+24
zetta = constants.zetta  #1e+21
exa = constants.exa  #1e+18
peta = constants.peta  #1000000000000000.0
tera = constants.tera  #1000000000000.0
giga = constants.giga  #1000000000.0
mega = constants.mega  #1000000.0
kilo = constants.kilo  #1000.0
hecto = constants.hecto  #100.0
deka = constants.deka  #10.0
deci = constants.deci  #0.1
centi = constants.centi  #0.01
milli = constants.milli  #0.001
micro = constants.micro  #1e-06
nano = constants.nano  #1e-09
pico = constants.pico  #1e-12
femto = constants.femto  #1e-15
atto = constants.atto  #1e-18
zepto = constants.zepto  #1e-21

result = ce('textarea')
result.value = f" kilo: {kilo}"
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.color = 'rgb(0, 255, 255)'
result.style.padding = '20px 20px'
ba(result)

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
```

### `pi.py`

```python
# pi.py

from pyside6dom import *
from scipy import constants

init_window('Our App', 700, 600)

result = ce('textarea')
result.value = f" pi: {constants.pi}"
result.style.fontSize = '50px'
result.style.fontWeight = 'bold'
result.style.color = 'rgb(0, 255, 255)'
result.style.padding = '20px 20px'
ba(result)

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
```


</details>

---

<details>
<summary><b>Section: showcase_001</b></summary>


### `inline_css_example.py`

```python
# inline_css_example.py

from pyside6dom import *

# Initialize the Application
init_window("PySide6DOM Feature Showcase", 450, 650)

# Worldwide Header
header = ce("h1")
header.textContent = "🚀 Mission Control"
header.style("font-size: 24px; color: #00ffcc; font-weight: bold; margin-bottom: 20px;")
ba(header)

# Text Input with Real-Time 'oninput' Event
pilot_input = ce("input")
pilot_input.id = "pilot_name"
pilot_input.placeholder = "Enter Pilot Name..."
pilot_input.style("padding: 10px; font-size: 14px; border: 2px solid #555; border-radius: 5px;")
ba(pilot_input)

# Live feedback label for the input
typing_echo = ce("text")
typing_echo.id = "echo_label"
typing_echo.textContent = "Awaiting pilot identification..."
typing_echo.style("color: #aaaaaa; font-style: italic; margin-bottom: 20px;")
ba(typing_echo)

# JS-Style zero-argument function
def on_type():
    ge("echo_label").textContent = f"Live typing: {pilot_input.value}"
pilot_input.oninput = on_type

# Slider with Real-Time 'oninput' Event
throttle_label = ce("text")
throttle_label.id = "throttle_display"
throttle_label.textContent = "Engine Throttle: 0%"
throttle_label.style("font-size: 16px; font-weight: bold; margin-top: 10px;")
ba(throttle_label)

throttle_slider = ce("slider")
throttle_slider.id = "throttle"

# JS-Style zero-argument function
def on_slide():
    # val comes in as a float natively, we multiply back for display
    ge("throttle_display").textContent = f"Engine Throttle: {int(throttle_slider.value * 10)}%"
throttle_slider.oninput = on_slide
ba(throttle_slider)

# Nested Containers (Div) for layout grouping
action_panel = ce("div")
action_panel.style("background-color: #222; border-radius: 8px; padding: 15px; margin-top: 20px;")
ba(action_panel)

# Interactive Button with rich CSS pseudo-states inside the Div
submit_btn = ce("button")
submit_btn.textContent = "ENGAGE THRUSTERS"
submit_btn.style("""
    button { 
        background-color: rgb(0, 0, 0); 
        color: white; 
        border-radius: 6px; 
        padding: 12px; 
        font-size: 16px; 
        font-weight: bold;
    }
    button:hover { background-color: rgb(0, 180, 180); }
    button:active { background-color: rgb(255, 255, 255); }
""")
ba(submit_btn, action_panel) # Appended to action_panel, NOT the main window

# Scrolling Log Window (scroll_div) for dynamic output
log_title = ce("h1")
log_title.textContent = "System Logs:"
log_title.style("margin-top: 20px; font-size: 14px; color: #888;")
ba(log_title)

log_window = ce("scroll_div")
log_window.style("background-color: #0a0a0a; border: 1px solid #333; min-height: 150px;")
ba(log_window)

# Button Click Event (Gathering data via 'ge' and appending to scroll_div)
def handle_engage():
    # Grab values from the registry
    pilot = ge("pilot_name").value or "Unknown Pilot"
    throttle = ge("throttle").value * 10

    # Create a new dynamic log entry
    log_entry = ce("p")
    log_entry.textContent = f"> {pilot} engaged engines at {int(throttle)}%"
    log_entry.style("color: #00ff00; font-family: monospace; font-size: 13px; margin: 2px;")

    # Append the new text directly into the scrolling window
    ba(log_entry, log_window)

submit_btn.onclick = handle_engage

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
```

### `pyside6dom_example.py`

```python
# pyside6dom_example.py

from pyside6dom import *

# Initialize the Application
init_window("PySide6DOM Feature Showcase", 450, 650)

# Worldwide Header
header = ce("h1")
header.textContent = "🚀 Mission Control"
header.style("font-size: 24px; color: #00ffcc; font-weight: bold; margin-bottom: 20px;")
ba(header)

# Text Input with Real-Time 'oninput' Event
pilot_input = ce("input")
pilot_input.id = "pilot_name"
pilot_input.placeholder = "Enter Pilot Name..."
pilot_input.style("padding: 10px; font-size: 14px; border: 2px solid #555; border-radius: 5px;")
ba(pilot_input)

# Live feedback label for the input
typing_echo = ce("text")
typing_echo.id = "echo_label"
typing_echo.textContent = "Awaiting pilot identification..."
typing_echo.style("color: #aaaaaa; font-style: italic; margin-bottom: 20px;")
ba(typing_echo)

# JS-Style zero-argument function
def on_type():
    ge("echo_label").textContent = f"Live typing: {pilot_input.value}"
pilot_input.oninput = on_type

# Slider with Real-Time 'oninput' Event
throttle_label = ce("text")
throttle_label.id = "throttle_display"
throttle_label.textContent = "Engine Throttle: 0%"
throttle_label.style("font-size: 16px; font-weight: bold; margin-top: 10px;")
ba(throttle_label)

throttle_slider = ce("slider")
throttle_slider.id = "throttle"

# JS-Style zero-argument function
def on_slide():
    ge("throttle_display").textContent = f"Engine Throttle: {int(throttle_slider.value * 10)}%"
throttle_slider.oninput = on_slide
ba(throttle_slider)

# Nested Containers (Div) for layout grouping
action_panel = ce("div")
action_panel.style("background-color: #222; border-radius: 8px; padding: 15px; margin-top: 20px;")
ba(action_panel)

# Interactive Button with rich CSS pseudo-states inside the Div
submit_btn = ce("button")
submit_btn.textContent = "ENGAGE THRUSTERS"
submit_btn.style("""
    button { 
        background-color: rgb(0, 0, 0); 
        color: white; 
        border-radius: 6px; 
        padding: 12px; 
        font-size: 16px; 
        font-weight: bold;
    }
    button:hover { background-color: rgb(0, 180, 180); }
    button:pressed { background-color: rgb(255, 255, 255); }
""")
ba(submit_btn, action_panel) 

# Scrolling Log Window (scroll_div) for dynamic output
log_title = ce("h1")
log_title.textContent = "System Logs:"
log_title.style("margin-top: 20px; font-size: 14px; color: #888;")
ba(log_title)

log_window = ce("scroll_div")
log_window.style("background-color: #0a0a0a; border: 1px solid #333; min-height: 150px;")
ba(log_window)

# Button Click Event (Gathering data via 'ge' and appending to scroll_div)
def handle_engage():
    # Grab values from the registry exactly like DOM manipulation
    pilot = ge("pilot_name").value or "Unknown Pilot"
    throttle = ge("throttle").value * 10

    # Create a new dynamic log entry
    log_entry = ce("p")
    log_entry.textContent = f"> {pilot} engaged engines at {int(throttle)}%"
    log_entry.style("color: #00ff00; font-family: monospace; font-size: 13px; margin: 2px;")

    # Append the new text directly into the scrolling window
    ba(log_entry, log_window)

submit_btn.onclick = handle_engage

# Launch the App
run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting
```

### `set_theme_example.py`

```python
# easy.py

from pyside6dom import *

# Initialize the Application
init_window("PySide6DOM Feature Showcase", 450, 650)

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
    button:active {
        color: rgb(255, 0, 255);
    }
    input {
        border: 1px solid white;
    }
""")

# Worldwide Header
header = ce("h1")
header.textContent = "🚀 Mission Control"
header.style("font-size: 24px; color: #00ffcc; font-weight: bold; margin-bottom: 20px;")
ba(header)

# Text Input with Real-Time 'oninput' Event
pilot_input = ce("input")
pilot_input.id = "pilot_name"
pilot_input.placeholder = "Enter Pilot Name..."
pilot_input.style("padding: 10px; font-size: 14px; border: 2px solid #555; border-radius: 5px;")
ba(pilot_input)

# Live feedback label for the input
typing_echo = ce("text")
typing_echo.id = "echo_label"
typing_echo.textContent = "Awaiting pilot identification..."
typing_echo.style("color: #aaaaaa; font-style: italic; margin-bottom: 20px;")
ba(typing_echo)

# JS-Style zero-argument function
def on_type():
    ge("echo_label").textContent = f"Live typing: {pilot_input.value}"
pilot_input.oninput = on_type

# Slider with Real-Time 'oninput' Event
throttle_label = ce("text")
throttle_label.id = "throttle_display"
throttle_label.textContent = "Engine Throttle: 0%"
throttle_label.style("font-size: 16px; font-weight: bold; margin-top: 10px;")
ba(throttle_label)

throttle_slider = ce("slider")
throttle_slider.id = "throttle"

# JS-Style zero-argument function
def on_slide():
    # val comes in as a float natively, we multiply back for display
    ge("throttle_display").textContent = f"Engine Throttle: {int(throttle_slider.value * 10)}%"
throttle_slider.oninput = on_slide
ba(throttle_slider)

# Nested Containers (Div) for layout grouping
action_panel = ce("div")
action_panel.style("background-color: #222; border-radius: 8px; padding: 15px; margin-top: 20px;")
ba(action_panel)

# Interactive Button with rich CSS pseudo-states inside the Div
submit_btn = ce("button")
submit_btn.textContent = "ENGAGE THRUSTERS"
ba(submit_btn, action_panel) # Appended to action_panel, NOT the main window

# Scrolling Log Window (scroll_div) for dynamic output
log_title = ce("h1")
log_title.textContent = "System Logs:"
log_title.style("margin-top: 20px; font-size: 14px; color: #888;")
ba(log_title)

log_window = ce("scroll_div")
log_window.style("background-color: #0a0a0a; border: 1px solid #333; min-height: 150px;")
ba(log_window)

# Button Click Event (Gathering data via 'ge' and appending to scroll_div)
def handle_engage():
    # Grab values from the registry
    pilot = ge("pilot_name").value or "Unknown Pilot"
    throttle = ge("throttle").value * 10

    # Create a new dynamic log entry
    log_entry = ce("p")
    log_entry.textContent = f"> {pilot} engaged engines at {int(throttle)}%"
    log_entry.style("color: #00ff00; font-family: monospace; font-size: 13px; margin: 2px;")

    # Append the new text directly into the scrolling window
    ba(log_entry, log_window)

submit_btn.onclick = handle_engage

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
```


</details>

---

<details>
<summary><b>Section: showcase_002</b></summary>


### `example_easier.py`

```python
# pyside6dom_example.py

from pyside6dom import *

init_window("Settings Panel", 400, 500)

# ===
#   WORLDWIDE STYLESHEET (CSS)
# ===
set_theme("""
    div {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    text {
        padding-top: 5px;
    }
    text#title_heading {
        font-size: 22px;
        font-weight: bold;
        color: #00ffcc;
        margin-bottom: 10px;
    }
    button {
        background-color: #007acc;
        color: white;
        border-radius: 4px;
        padding: 10px;
        font-weight: bold;
        margin-top: 15px;
    }
    button:hover { background-color: #0099ff; }
    button:pressed { background-color: #005c99; }
    
    select {
        padding: 6px;
        background-color: #2b2b2b;
        border: 1px solid #555;
        border-radius: 3px;
    }
    /* This fixes the missing hover highlight in dropdowns! */
    select option {
        background-color: #2b2b2b;
        selection-background-color: #007acc;
        selection-color: white;
    }
    
    scroll_div {
        border: 1px solid #444;
        background-color: #111;
        margin-top: 10px;
    }
""")

# ===
#  UI BUILDER
# ===

header = ce("h1")
header.id = "title_heading"
header.textContent = "⚙️ Settings Panel"
ba(header)

mode_label = ce("text")
mode_label.textContent = "Select Operating Mode:"
ba(mode_label)

mode_select = ce("select")
mode_select.id = "app_mode"
mode_select.options = ["Standard", "Advanced", "Developer"]
ba(mode_select)

debug_checkbox = ce("checkbox")
debug_checkbox.id = "debug_flag"
debug_checkbox.textContent = "Enable Debug Logging"
debug_checkbox.checked = True
ba(debug_checkbox)

apply_btn = ce("button")
apply_btn.textContent = "Apply Settings"
ba(apply_btn)

log_window = ce("scroll_div")
ba(log_window)

def handle_apply():
    selected = ge("app_mode").value
    debug = ge("debug_flag").checked
    
    log = ce("p")
    log.textContent = f"> Mode: {selected} | Debug: {debug}"
    log.style("color: #00ff00; font-family: monospace;") # Inline overrides still work
    ba(log, log_window)

apply_btn.onclick = handle_apply

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
```

### `pyside6dom_example.py`

```python
# pyside6dom_example.py

from pyside6dom import *

init_window("Settings Panel", 400, 500)

# ===
#   WORLDWIDE STYLESHEET (CSS)
# ===
set_global_style("""
    QWidget {
        background-color: #1e1e1e;
        color: #ffffff;
        font-family: Arial, sans-serif;
        font-size: 14px;
    }
    QLabel {
        padding-top: 5px;
    }
    QLabel#title_heading {
        font-size: 22px;
        font-weight: bold;
        color: #00ffcc;
        margin-bottom: 10px;
    }
    QPushButton {
        background-color: #007acc;
        color: white;
        border-radius: 4px;
        padding: 10px;
        font-weight: bold;
        margin-top: 15px;
    }
    QPushButton:hover { background-color: #0099ff; }
    QPushButton:pressed { background-color: #005c99; }
    
    QComboBox {
        padding: 6px;
        background-color: #2b2b2b;
        border: 1px solid #555;
        border-radius: 3px;
    }
    /* This fixes the missing hover highlight in dropdowns! */
    QComboBox QAbstractItemView {
        background-color: #2b2b2b;
        selection-background-color: #007acc;
        selection-color: white;
    }
    
    QScrollArea {
        border: 1px solid #444;
        background-color: #111;
        margin-top: 10px;
    }
""")

# ===
#  UI BUILDER
# ===

header = ce("h1")
header.id = "title_heading"
header.textContent = "⚙️ Settings Panel"
ba(header)

mode_label = ce("text")
mode_label.textContent = "Select Operating Mode:"
ba(mode_label)

mode_select = ce("select")
mode_select.id = "app_mode"
mode_select.options = ["Standard", "Advanced", "Developer"]
ba(mode_select)

debug_checkbox = ce("checkbox")
debug_checkbox.id = "debug_flag"
debug_checkbox.textContent = "Enable Debug Logging"
debug_checkbox.checked = True
ba(debug_checkbox)

apply_btn = ce("button")
apply_btn.textContent = "Apply Settings"
ba(apply_btn)

log_window = ce("scroll_div")
ba(log_window)

def handle_apply():
    selected = ge("app_mode").value
    debug = ge("debug_flag").checked
    
    log = ce("p")
    log.textContent = f"> Mode: {selected} | Debug: {debug}"
    log.style("color: #00ff00; font-family: monospace;") # Inline overrides still work
    ba(log, log_window)

apply_btn.onclick = handle_apply

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
```


</details>

---

<details>
<summary><b>Section: 1.1_database_connect_or_create</b></summary>


### `database_connect_or_create.py`

```python
# database_connect_or_create.py

import sqlite3

from pyside6dom import *

# Connect to the database (it creates the file automatically if it doesn't exist)
conn = sqlite3.connect('military_warehouse.db')

# Think of the cursor as the worker inside the database.
# The cursor is the tool you actually use to run SQL commands and navigate through the rows returned.
# This creates a cursor object attached to that open connection made above.
cursor = conn.cursor()

# SQL command to CREATE a table named Inventory
# Inventory table has id, part_name, quantity and price
sql_command = """
CREATE TABLE IF NOT EXISTS Inventory (
    id INTEGER PRIMARY KEY,
    part_name TEXT,
    quantity INTEGER,
    price REAL
);
"""
# REAL is a data type for a floating point number, aka decimal numbers.

# Execute and save
cursor.execute(sql_command)
conn.commit()
conn.close()

print("Military Warehouse Database and Table created successfully!")

####

init_window("Create Database", 700, 500)

status_message = ce('text')
status_message.textContent = 'Database Created'
ba(status_message)

run_app()

####

'''
This script creates a local file called military_warehouse.db and sets up a table (like a spreadsheet) with strict columns.
'''

'''
What Does the Cursor Actually Do?
The cursor handles two primary jobs:

1. Executing SQL Commands (.execute())
You tell the cursor what SQL statement to run:
cursor.execute("SELECT part_name, price FROM Inventory WHERE price > 50")

2. Fetching and Tracking Rows (.fetchone(), .fetchall())
When the database finds matching rows, the cursor acts like a bookmark pointing at the current row:

cursor.fetchone() - Grabs the next single row and moves the pointer forward by one.

cursor.fetchall() - Grabs all remaining matching rows at once as a list.

cursor.fetchmany(10) - Grabs the next 10 rows (ideal for streaming chunks of data without overloading memory).
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.2_insert_data</b></summary>


### `insert_data.py`

```python
# insert_data.py

import sqlite3
from pyside6dom import *

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command using the '?' Security Shield placeholders
sql_insert = """
INSERT INTO Inventory (part_name, quantity, price) 
VALUES (?, ?, ?)
"""

# The data safely isolated in a standard Python list
military_items = [
    ('Night Vision Goggles', 45, 2500.00),
    ('Kevlar Vest', 150, 450.50),
    ('Field Medical Kit', 300, 75.25)
]

# executemany handles the secure merge and loops through the list
cursor.executemany(sql_insert, military_items)

conn.commit() # Always commit when making changes!
conn.close()

print("Military Warehouse data securely inserted!")

####

init_window("Insert Data", 700, 500)

status_message = ce('h2')
status_message.innerHTML = 'Data Inserted Securely'
status_message.style.color = '#00ffcc'
ba(status_message)

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
```


</details>

---

<details>
<summary><b>Section: 1.3_read_data</b></summary>


### `read_data.py`

```python
# read_data.py

import sqlite3
from pyside6dom import *

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to SELECT data
sql_select = "SELECT part_name, price FROM Inventory WHERE quantity > 100;"

# Execute and fetch the results
cursor.execute(sql_select)
results = cursor.fetchall()
conn.close() # Safe to close as soon as you have the results in memory

# Start building the HTML string with standard table tags
html_data = "<table border='1' cellpadding='4' cellspacing='0'>"

html_data += "<tr><th>Part Name</th><th>Price</th></tr>"

# Loop through the database results and add a table row for each item
for row in results:
    part_name = row[0]
    # Format the price to ensure it always shows two decimal places
    price = f"${row[1]:.2f}" 
    
    # Print to console for debugging
    print(f"Item: {part_name} | Price: {price}")
    
    # Add to the HTML table
    html_data += f"<tr><td>{part_name}</td><td>{price}</td></tr>"

# Close the HTML table tag
html_data += "</table>"

####

init_window("Military Warehouse Inventory", 700, 500)

output = ce('text')
# Inject the constructed HTML string into the UI
output.innerHTML = html_data
ba(output)

run_app()

####

'''
Item: Kevlar Vest | Price: $450.5
Item: Field Medical Kit | Price: $75.25
'''

'''
Query (Read) the Data  
The SELECT command grabs the exact data requested from the database.
'''

'''
Explaining the Loop and row[0]
Let's look at the SELECT command we ran:
SELECT part_name, price FROM Inventory WHERE quantity > 100;

Because we asked for exactly two columns in that specific order, and filtered for quantities over 100, SQLite hands us a list of locked tuples that looks like this:
[
    ('Kevlar Vest', 450.50),
    ('Field Medical Kit', 75.25)
]

When we write the for loop, we are just extracting one tuple at a time:

for row in results:
    # On the first loop, row = ('Kevlar Vest', 450.50)
    
    # row[0] is the 1st item: 'Kevlar Vest'
    # row[1] is the 2nd item: 450.50
    
    print(f"Item: {row[0]} | Price: ${row[1]}")
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.4_update_data</b></summary>


### `update_data.py`

```python
# update_data.py

import sqlite3
from pyside6dom import *

init_window('Update SQLite Data', 700, 450)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Inventory System</b><br><hr><br>"
ba(title_txt)

# Connect to the database and set up the cursor
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command using the '?' Security Shield
sql_update = """
UPDATE Inventory 
SET quantity = ? 
WHERE part_name = ?
"""

# The data values securely organized in a tuple
update_values = (100, 'Kevlar Vest')

# Execute and safely merge the command with the data
cursor.execute(sql_update, update_values)
conn.commit() # Always commit when modifying data!

# Display a styled success message!
status_txt = ce('text')
status_txt.innerHTML = "<b style='color: #00ffcc;'>Status: Inventory updated successfully!</b><br><br><b>Verification (Reading live from database):</b>"
ba(status_txt)

# Consistent Security: We also use the '?' shield when querying data!
# Note the comma after 'Kevlar Vest' - this ensures Python treats it as a tuple
cursor.execute("SELECT * FROM Inventory WHERE part_name = ?;", ('Kevlar Vest',))
updated_record = cursor.fetchone()

# Always close the connection when finished
conn.close()

# Show the exact tuple returned by SQLite on the screen
verify_txt = ce('text')
# textContent prevents the tuple's brackets and quotes from being mistaken for HTML tags
verify_txt.textContent = f"Database Record: {updated_record}"
ba(verify_txt)

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
```


</details>

---

<details>
<summary><b>Section: 1.5_delete_data</b></summary>


### `delete_data.py`

```python
# delete_data.py

import sqlite3
from pyside6dom import *

init_window('Delete SQLite Data', 700, 450)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Inventory System</b><br><hr><br>"
ba(title_txt)

# Connect to the database and set up the cursor
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to DELETE existing data
sql_delete = """
DELETE FROM Inventory 
WHERE part_name = 'Night Vision Goggles';
"""

# Execute and save the changes
cursor.execute(sql_delete)
conn.commit() # Always commit when modifying or deleting data!

# Display a styled success message!
status_txt = ce('text')
status_txt.innerHTML = "<b style='color: #00ffcc;'>Status: Item successfully deleted!</b><br><br><b>Verification (Searching database for deleted item):</b>"
ba(status_txt)

# Query the database to prove it is gone
cursor.execute("SELECT * FROM Inventory WHERE part_name = 'Night Vision Goggles';")
deleted_record = cursor.fetchone()

# Always close the connection when finished
conn.close()

# Show the exact result returned by SQLite on the screen
verify_txt = ce('text')
# We add a little note explaining what 'None' means for the students
verify_txt.textContent = f"Database Record: {deleted_record} \n(A result of 'None' means the data was completely erased!)"
ba(verify_txt)

run_app()

####

'''
A crate of Night Vision Goggles was crushed during a tank training exercise. 
We use the DELETE command to completely remove that row from our active inventory.
'''

'''
CRITICAL SAFETY RULE:
Always include the WHERE clause when deleting! 
If you just write "DELETE FROM Inventory;" without the WHERE clause, 
the database will instantly delete EVERY single row in the table, wiping out your entire warehouse!
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.6_search_data</b></summary>


### `search_data.py`

```python
# search_data.py

import sqlite3
from pyside6dom import *

init_window('Search SQLite Data', 700, 500)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Database Search</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The dynamic variable we want to search for
search_term = 'Field Medical Kit'

# The SQL command using a '?' placeholder for safety
sql_search = "SELECT part_name, quantity, price FROM Inventory WHERE part_name = ?;"

# Execute the search, passing our variable inside a tuple
cursor.execute(sql_search, (search_term,))
results = cursor.fetchall()

# Display what we are searching for
header_txt = ce('text')
header_txt.innerHTML = f"<b>--- SEARCH RESULTS FOR: <span style='color: #00ffcc;'>{search_term.upper()}</span> ---</b><br>"
ba(header_txt)

# Loop through the results and build the UI dynamically
if len(results) == 0:
    # If the list is empty, show the not found message
    not_found_txt = ce('text')
    not_found_txt.textContent = "Status: Item not found in the warehouse."
    ba(not_found_txt)
else:
    # If we have results, loop through and create an element for each row
    for row in results:
        row_txt = ce('text')
        # Using innerHTML so we can selectively bold the labels
        row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> {row[1]} &nbsp;|&nbsp; <b>Price:</b> ${row[2]}<br>"
        ba(row_txt)

conn.close()

run_app()

####

'''
The Base Commander wants to look up the exact stock of a specific item without hard-coding it.
We use a Python variable and a '?' placeholder to safely pass the search term to the database.
'''

'''
CRITICAL SAFETY RULE (Preventing SQL Injection):
Never use standard Python f-strings (e.g., f"SELECT * FROM Inventory WHERE part_name = '{search_term}'") 
to pass variables into SQL. This opens the door to a cyberattack called SQL Injection. 
Always use the '?' placeholder! SQLite will safely sanitize the variable for you.
'''

'''
When web development students take input from a search bar, they might be tempted to concatenate the string directly into the SQL command (e.g., "... WHERE part_name = " + search_term). But, that is VERY DANGEROUS!

FOR SAFETY, we instead use the ? placeholder and passing the variable in a tuple, SQLite automatically sanitizes the data, protecting the database from malicious code.
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.7_sort_data</b></summary>


### `sort_data.py`

```python
# sort_data.py

import sqlite3
from pyside6dom import *

init_window('Sort SQLite Data', 700, 500)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Reorder System</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to SELECT data and sort it
# ORDER BY quantity ASC tells the database engine to put the lowest numbers at the top!
sql_sort = "SELECT part_name, quantity, price FROM Inventory ORDER BY quantity ASC;"

# Execute and fetch the results
cursor.execute(sql_sort)
results = cursor.fetchall()

# We have the data, so we can safely close the connection
conn.close()

# Display the header for the sorted data
# Using a red hex code to emphasize the critical nature of the list
header_txt = ce('text')
header_txt.innerHTML = "<b><span style='color: #ff3333;'>CRITICAL REORDER LIST (LOWEST STOCK FIRST):</span></b><br><br>"
ba(header_txt)

# Loop through the sorted results and build the UI
for row in results:
    row_txt = ce('text')
    
    # Using inline HTML to style the stock numbers so they immediately catch the eye
    row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> <span style='color: #00ffcc;'>{row[1]}</span> &nbsp;|&nbsp; <b>Unit Cost:</b> ${row[2]}<br>"
    ba(row_txt)

run_app()

####

'''
The Quartermaster needs to know which items are closest to running out.
We use the ORDER BY command to automatically sort the results before Python even receives them.
'''

'''
ASC vs DESC:
ASC (Ascending) sorts from smallest to largest (A-Z, 1-100). This is the default if you leave it blank.
DESC (Descending) sorts from largest to smallest (Z-A, 100-1). Perfect for finding the most expensive items!
'''

'''
In web development, students might be tempted to use SELECT * FROM Inventory, pull every single item into JavaScript, and then use the array.sort() method to organize them. BUT, by instead doing the sorting inside the SQL query (ORDER BY quantity ASC) is infinitely faster. By making the database do the heavy lifting before the data even reaches Python, they save memory and ensure their pyside6dom interface loads instantly.
'''

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
```


</details>

---

<details>
<summary><b>Section: 2.0_seed_data_uniform</b></summary>


### `seed_data_uniform.py`

```python
# seed_data_uniform.py

import sqlite3
from pyside6dom import *

init_window('Seed Uniform Data', 750, 650)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Database Initialization</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# Recreate the table so we start clean
# This is the ultimate "undo" button for students
cursor.execute("DROP TABLE IF EXISTS Inventory")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Inventory (
    id INTEGER PRIMARY KEY,
    part_name TEXT,
    quantity INTEGER,
    delivery_date TEXT
);
""")

# The SQL command using the '?' Security Shield placeholders
sql_insert = """
INSERT INTO Inventory (part_name, quantity, delivery_date) 
VALUES (?, ?, ?)
"""

# The 10 uniform records cleanly organized into a Python list of tuples.
# This makes it incredibly easy to read and edit compared to a massive SQL string.
military_items = [
    ('Kevlar Vest', 150, '2025-11-15'),
    ('Night Vision Goggles', 45, '2026-02-10'),
    ('Field Medical Kit', 300, '2026-08-24'),
    ('Combat Boots', 220, '2026-01-05'),
    ('Tactical Radio', 60, '2025-12-01'),
    ('MRE Case', 500, '2026-03-22'),
    ('Ammunition Crate', 80, '2026-01-30'),
    ('First Aid Pouch', 175, '2026-02-14'),
    ('Portable Generator', 12, '2025-10-09'),
    ('Camouflage Netting', 95, '2026-04-02')
]

# executemany loops through the list and safely inserts all 10 rows
cursor.executemany(sql_insert, military_items)
conn.commit()

# Display a styled success message
status_txt = ce('text')
status_txt.innerHTML = "<b style='color: #00ffcc;'>Status: Table reset and seeded with 10 uniform-date items successfully!</b><br><br><b>Verification (Live Database Contents):</b><br>"
ba(status_txt)

# Query the newly built table to prove the data is in there!
# (No question marks needed here because we aren't filtering with a WHERE clause)
cursor.execute("SELECT part_name, quantity, delivery_date FROM Inventory;")
results = cursor.fetchall()

# Always close the connection
conn.close()

# Loop through and display the freshly inserted data
for row in results:
    row_txt = ce('text')
    # We apply the aqua color specifically to the date so students see the uniformity
    row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> {row[1]} &nbsp;|&nbsp; <b>Delivery Date:</b> <span style='color: #00ffcc;'>{row[2]}</span>"
    ba(row_txt)

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
```


</details>

---

<details>
<summary><b>Section: 2.1_filter_after_date</b></summary>


### `filter_after_date.py`

```python
# filter_after_date.py

import sqlite3
from pyside6dom import *

init_window('Filter by Date', 700, 500)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Delivery Filter</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The dynamic date we want to filter by
target_date = '2026-01-01'

# SQL command to find everything delivered AFTER the target date
# Notice we are still using the '?' placeholder for security!
sql_filter = "SELECT part_name, quantity, delivery_date FROM Inventory WHERE delivery_date > ?;"

# Execute the search securely
cursor.execute(sql_filter, (target_date,))
results = cursor.fetchall()

# Always close the connection
conn.close()

# Display the filter criteria with some red emphasis
header_txt = ce('text')
header_txt.innerHTML = f"<b>--- SHIPMENTS RECEIVED AFTER <span style='color: #ff3333;'>{target_date}</span> ---</b><br><br>"
ba(header_txt)

# Loop through the results and build the UI dynamically
if len(results) == 0:
    not_found_txt = ce('text')
    not_found_txt.textContent = "No shipments found after this date."
    ba(not_found_txt)
else:
    for row in results:
        row_txt = ce('text')
        # Highlighting the date in cyan so they can visually confirm the filter worked
        row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> {row[1]} &nbsp;|&nbsp; <b>Delivered:</b> <span style='color: #00ffcc;'>{row[2]}</span><br>"
        ba(row_txt)

run_app()

'''
SHIPMENTS RECEIVED AFTER 2026-01-01
Item: Night Vision Goggles | Stock: 45 | Delivered: 2026-02-10
Item: Field Medical Kit | Stock: 300 | Delivered: 2026-08-24
Item: Combat Boots | Stock: 220 | Delivered: 2026-01-05
Item: MRE Case | Stock: 500 | Delivered: 2026-03-22
Item: Ammunition Crate | Stock: 80 | Delivered: 2026-01-30
Item: First Aid Pouch | Stock: 175 | Delivered: 2026-02-14
Item: Camouflage Netting | Stock: 95 | Delivered: 2026-04-02
'''

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
```


</details>

---

<details>
<summary><b>Section: 3.2_insert_data_with_gui</b></summary>


### `insert_data_with_gui.py`

```python
# insert_data_with_gui.py

import sqlite3
import pandas as pd
from pyside6dom import *

###
# DATABASE FUNCTIONS
###

def refresh_table():
    """Reads the latest data from the database and updates the GUI table."""
    conn = sqlite3.connect('social_media_links.db')
    theData = pd.read_sql_query("SELECT * FROM Social_Media_Links", conn)
    conn.close()
    
    # Update our PySide6DOM table_view instantly
    data_view.innerHTML = theData.to_html(index=False)

def save_new_link():
    """Grabs user input, secures it with parameterized queries, and saves it."""
    # Grab the live text typed by the user into the GUI text boxes
    user_date = date_input.value
    user_desc = desc_input.value
    user_link = link_input.value
    
    # Connect to the database
    conn = sqlite3.connect('social_media_links.db')
    cursor = conn.cursor()
    
    # The SQL command using the '?' Security Shield
    insert_sql = "INSERT INTO Social_Media_Links (date, description, link) VALUES (?, ?, ?)"
    
    # Safely merge the live user data with the SQL command
    cursor.execute(insert_sql, (user_date, user_desc, user_link))
    conn.commit()
    conn.close()
    
    # Clear the text boxes so they are ready for the next entry
    date_input.value = ""
    desc_input.value = ""
    link_input.value = ""
    
    # Refresh the visual table to show the new record!
    refresh_table()

###
# GUI DASHBOARD
###

init_window("Interactive Data Entry", 850, 750)

# Dashboard Title
title_txt = ce('h2')
title_txt.innerHTML = "Add New Social Media Link<hr>"
title_txt.style.color = '#00ffcc'
ba(title_txt)

###
# FORM INPUTS
###

# Date Input
date_label = ce('text')
date_label.innerHTML = "<b>Date (YYYY-MM-DD):</b>"
ba(date_label)
date_input = ce('input')
ba(date_input)

# Description Input
desc_label = ce('text')
desc_label.innerHTML = "<br><b>Video Description:</b>"
ba(desc_label)
desc_input = ce('input')
ba(desc_input)

# Link Input
link_label = ce('text')
link_label.innerHTML = "<br><b>URL Link:</b>"
ba(link_label)
link_input = ce('input')
ba(link_input)

###
# SUBMIT BUTTON
###

add_btn = ce('button')
add_btn.textContent = "Add Link"
# Attach our save function to the button click event
add_btn.onclick = save_new_link 
ba(add_btn)

###
# LIVE DATA TABLE
###

table_title = ce('text')
table_title.innerHTML = "<br><br><b style='color: #00ffcc;'>Live Database Records:</b><hr>"
ba(table_title)

# Create the table view component
data_view = ce('table_view')
ba(data_view)

# Run the refresh function once at startup to populate the table initially
refresh_table()

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
```


</details>

---

<details>
<summary><b>Section: 1.2_insert_data_insecure</b></summary>


### `insert_data_insecure.py`

```python
# insert_data.py

import sqlite3

from pyside6dom import *

conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to INSERT data
sql_insert = """
INSERT INTO Inventory (part_name, quantity, price) 
VALUES 
    ('Night Vision Goggles', 45, 2500.00),
    ('Kevlar Vest', 150, 450.50),
    ('Field Medical Kit', 300, 75.25);
"""

cursor.execute(sql_insert)
conn.commit() # Always commit when making changes!
conn.close()

print("Military Warehouse data inserted successfully!")

####

init_window("Insert Data", 700, 500)

status_message = ce('text')
status_message.textContent = 'Data Inserted'
ba(status_message)

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
```


</details>

---

<details>
<summary><b>Section: 1.4_update_data_insecure</b></summary>


### `update_data_insecure.py`

```python
# update_data.py

import sqlite3
from pyside6dom import *

init_window('Update SQLite Data', 700, 450)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Inventory System</b><br><hr><br>"
ba(title_txt)

# Connect to the database and set up the cursor
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# The SQL command to UPDATE existing data
sql_update = """
UPDATE Inventory 
SET quantity = 100 
WHERE part_name = 'Kevlar Vest';
"""

# Execute and save the changes
cursor.execute(sql_update)
conn.commit() # Always commit when modifying data!

# Display a styled success message!
status_txt = ce('text')
status_txt.innerHTML = "<b style='color: #00ffcc;'>Status: Inventory updated successfully!</b><br><br><b>Verification (Reading live from database):</b>"
ba(status_txt)

# Query the database to prove the quantity changed
cursor.execute("SELECT * FROM Inventory WHERE part_name = 'Kevlar Vest';")
updated_record = cursor.fetchone()

# Always close the connection when finished
conn.close()

# Show the exact tuple returned by SQLite on the screen
verify_txt = ce('text')
# textContent prevents the tuple's brackets and quotes from being mistaken for HTML tags
verify_txt.textContent = f"Database Record: {updated_record}"
ba(verify_txt)

run_app()

####

'''
A platoon just signed out 50 Kevlar Vests for deployment. 
We use the UPDATE command to change the existing quantity from 150 down to 100.
'''

'''
CRITICAL SAFETY RULE:
Always include the WHERE clause when updating! 
If you just write "UPDATE Inventory SET quantity = 100;" without the WHERE clause, 
the database will change the quantity of EVERY single item in the entire warehouse to 100!
'''

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
```


</details>

---

<details>
<summary><b>Section: 2.0_seed_data_uniform_insecure</b></summary>


### `seed_data_uniform_insecure.py`

```python
# seed_data_uniform.py

import sqlite3
from pyside6dom import *

init_window('Seed Uniform Data', 750, 650)

# Add a stylish dashboard title
title_txt = ce('text')
title_txt.innerHTML = "<b style='color: #00ffcc; font-size: 18px;'>Military Warehouse: Database Initialization</b><br><hr><br>"
ba(title_txt)

# Connect to the database
conn = sqlite3.connect('military_warehouse.db')
cursor = conn.cursor()

# Recreate the table so we start clean
# This is the ultimate "undo" button for students
cursor.execute("DROP TABLE IF EXISTS Inventory")
cursor.execute("""
CREATE TABLE IF NOT EXISTS Inventory (
    id INTEGER PRIMARY KEY,
    part_name TEXT,
    quantity INTEGER,
    delivery_date TEXT
);
""")

# Insert the 10 uniform records
# Using standard ISO 8601 format (YYYY-MM-DD)
sql_insert = """
INSERT INTO Inventory (part_name, quantity, delivery_date) 
VALUES 
    ('Kevlar Vest', 150, '2025-11-15'),
    ('Night Vision Goggles', 45, '2026-02-10'),
    ('Field Medical Kit', 300, '2026-08-24'),
    ('Combat Boots', 220, '2026-01-05'),
    ('Tactical Radio', 60, '2025-12-01'),
    ('MRE Case', 500, '2026-03-22'),
    ('Ammunition Crate', 80, '2026-01-30'),
    ('First Aid Pouch', 175, '2026-02-14'),
    ('Portable Generator', 12, '2025-10-09'),
    ('Camouflage Netting', 95, '2026-04-02');
"""

# Execute and commit the massive insertion block
cursor.execute(sql_insert)
conn.commit()

# Display a styled success message
status_txt = ce('text')
status_txt.innerHTML = "<b style='color: #00ffcc;'>Status: Table reset and seeded with 10 uniform-date items successfully!</b><br><br><b>Verification (Live Database Contents):</b><br>"
ba(status_txt)

# Query the newly built table to prove the data is in there!
cursor.execute("SELECT part_name, quantity, delivery_date FROM Inventory;")
results = cursor.fetchall()

# Always close the connection
conn.close()

# Loop through and display the freshly inserted data
for row in results:
    row_txt = ce('text')
    # We apply the aqua color specifically to the date so students see the uniformity
    row_txt.innerHTML = f"&bull; <b>Item:</b> {row[0]} &nbsp;|&nbsp; <b>Stock:</b> {row[1]} &nbsp;|&nbsp; <b>Delivery Date:</b> <span style='color: #00ffcc;'>{row[2]}</span>"
    ba(row_txt)

run_app()

####

'''
By strictly enforcing the ISO 8601 format (YYYY-MM-DD), we are writing text that can be flawlessly sorted alphabetically by the database engine. 2026-01-05 will always structurally sort before 2026-02-10. It is a brilliant computer science concept that ensures our application behaves predictably when we inevitably write an ORDER BY delivery_date command later on
'''

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
```


</details>

---

<details>
<summary><b>Section: 1.1_foundation</b></summary>


### `true_si.py`

```python
# true_si.py

from pyside6dom import *
import random

init_window('True SI', 700, 600)

a = 0
b = 0

our_tau = 1
our_con = 1
our_xor = 1
our_xnor = 1
our_and = 1
our_nand = 1
our_or = 1
our_nor = 1
our_mi = 1
our_mni = 1
our_ci = 1
our_cni = 1
our_lp = 1
our_lc = 1
our_rp = 1
our_rc = 1

def random_inputs():
    global a, b
    # randint(0, 1) ensures we strictly get 0 or 1, not floats
    a = random.randint(0, 1)
    b = random.randint(0, 1)

def thinking():
    try:
        global our_tau, our_con, our_xor, our_xnor
        global our_and, our_nand, our_or, our_nor
        global our_mi, our_mni, our_ci, our_cni
        global our_lp, our_lc, our_rp, our_rc

        our_tau = TAU(a, b)
        our_con = CON(a, b)
        
        our_xor = XOR(a, b)
        our_xnor = XNOR(a, b)
        
        our_and = AND(a, b)
        our_nand = NAND(a, b)
        our_or = OR(a, b)
        our_nor = NOR(a, b)
        
        our_mi = MI(a, b)
        our_mni = MNI(a, b)
        our_ci = CI(a, b)
        our_cni = CNI(a, b)
        
        our_lp = LP(a, b)
        our_lc = LC(a, b)
        our_rp = RP(a, b)
        our_rc = RC(a, b)
        
    except Exception as error:
        # If any gate fails, we catch the error to keep the timer alive
        print(f"Error in thinking matrix: {error}")

def show_thoughts():
    ge('results_div').textContent = (
        'TAU: ' + str(our_tau) + '\n' +
        'CON: ' + str(our_con) + '\n' +
        'XOR: ' + str(our_xor) + '\n' +
        'XNOR: ' + str(our_xnor) + '\n' +
        'AND: ' + str(our_and) + '\n' +
        'NAND: ' + str(our_nand) + '\n' +
        'OR: ' + str(our_or) + '\n' +
        'NOR: ' + str(our_nor) + '\n' +
        'MI: ' + str(our_mi) + '\n' +
        'MNI: ' + str(our_mni) + '\n' +
        'CI: ' + str(our_ci) + '\n' +
        'CNI: ' + str(our_cni) + '\n' +
        'LP: ' + str(our_lp) + '\n' +
        'LC: ' + str(our_lc) + '\n' +
        'RP: ' + str(our_rp) + '\n' +
        'RC: ' + str(our_rc) + '\n'
    )

results_div = ce('div')
results_div.id = 'results_div'
results_div.style.whiteSpace = 'pre'
results_div.style.fontSize = '30px'
results_div.style.fontFamily = 'Arial'
results_div.style.fontWeight = 'bold'
results_div.style.padding = '20px'
results_div.textContent = 'Initializing thoughts...'
ba(results_div)

# environment loop
inputs_timer = setInterval(random_inputs, 1000)
think_timer = setInterval(thinking, 1000)
results_timer = setInterval(show_thoughts, 1000)

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: 1.2_true_si_hypercube</b></summary>


### `true_si_hypercube.py`

```python
# true_si_hypercube.py

from pyside6dom import *
import random

init_window('True SI - Active Hypercube', 750, 700)

# We map each gate to its truth-table coordinate and assign its distinct logic function
hypercube_nodes = {
    "CON":  {"coords": (0, 0, 0, 0), "value": 0, "func": lambda a, b: 0},
    "AND":  {"coords": (0, 0, 0, 1), "value": 0, "func": lambda a, b: a & b},
    "MNI":  {"coords": (0, 0, 1, 0), "value": 0, "func": lambda a, b: 1 if a > b else 0},
    "LP":   {"coords": (0, 0, 1, 1), "value": 0, "func": lambda a, b: a},
    "CNI":  {"coords": (0, 1, 0, 0), "value": 0, "func": lambda a, b: 1 if b > a else 0},
    "RP":   {"coords": (0, 1, 0, 1), "value": 0, "func": lambda a, b: b},
    "XOR":  {"coords": (0, 1, 1, 0), "value": 0, "func": lambda a, b: a ^ b},
    "OR":   {"coords": (0, 1, 1, 1), "value": 0, "func": lambda a, b: a | b},
    "NOR":  {"coords": (1, 0, 0, 0), "value": 0, "func": lambda a, b: 1 - (a | b)},
    "XNOR": {"coords": (1, 0, 0, 1), "value": 0, "func": lambda a, b: 1 - (a ^ b)},
    "RC":   {"coords": (1, 0, 1, 0), "value": 0, "func": lambda a, b: 1 - b},
    "MI":   {"coords": (1, 0, 1, 1), "value": 0, "func": lambda a, b: 1 if a <= b else 0},
    "LC":   {"coords": (1, 1, 0, 0), "value": 0, "func": lambda a, b: 1 - a},
    "CI":   {"coords": (1, 1, 0, 1), "value": 0, "func": lambda a, b: 1 if b <= a else 0},
    "NAND": {"coords": (1, 1, 1, 0), "value": 0, "func": lambda a, b: 1 - (a & b)},
    "TAU":  {"coords": (1, 1, 1, 1), "value": 0, "func": lambda a, b: 1}
}

a = 0
b = 0

def random_inputs():
    global a, b
    a = random.randint(0, 1)
    b = random.randint(0, 1)

def thinking():
    # Each node now evaluates the inputs using its own specific logic function
    for gate, data in hypercube_nodes.items():
        data["value"] = data["func"](a, b)

def show_thoughts():
    display_text = f"Energy Inputs -> A: {a} | B: {b}\n"
    display_text += "=" * 32 + "\n\n"
    
    for gate, data in hypercube_nodes.items():
        coord_str = f"{data['coords'][0]}{data['coords'][1]}{data['coords'][2]}{data['coords'][3]}"
        
        # We format the string so the columns align perfectly
        display_text += f"{gate.ljust(5)} at {coord_str} : State [ {data['value']} ]\n"
    
    result_div.textContent = display_text

####

# UI Setup
set_theme('''
    body {
        background-color: rgb(15, 15, 20);
        color: rgb(0, 255, 255);
        font-family: Arial;
        font-size: 30px;
        font-weight: bold;
        padding: 20px;
    }
''')

result_div = ce('div')
result_div.style.whiteSpace = 'pre'
result_div.textContent = 'Initializing hypercube vessel...'
ba(result_div)

# Active Loops
inputs_timer = setInterval(random_inputs, 1000)
think_timer = setInterval(thinking, 1000)
results_timer = setInterval(show_thoughts, 1000)

run_app()

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherTopalian
# https://github.com/ChristopherAndrewTopalian
# https://sites.google.com/view/CollegeOfScripting
```


</details>

---

<details>
<summary><b>Section: z_local_testing</b></summary>


### `local_testing_2_back.py`

```python
import sys
import os

# Local Testing
# This grabs the folder the script is in, then goes up one or two levels to the root.
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir)) 
sys.path.insert(0, project_root)
# --------------------------
```

### `local_testing_3_back.py`

```python

import sys
import os

# Local Testing
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir))) 
sys.path.insert(0, project_root)
# --------------------------
```

### `local_testing_4_back.py`

```python
import sys
import os

# Local Testing
current_dir = os.path.dirname(os.path.abspath(__file__))

# Wrapped in one more dirname()
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(current_dir))))

sys.path.insert(0, project_root)
# --------------------------
```


</details>


---
