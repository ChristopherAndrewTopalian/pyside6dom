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

