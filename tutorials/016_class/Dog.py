# Dog.py

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

