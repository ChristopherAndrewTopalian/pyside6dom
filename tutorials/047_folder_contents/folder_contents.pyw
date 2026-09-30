# folder_contents.pyw

from pyside6dom import *

init_window('Folder Contents', 700, 600)

folder_contents = os.listdir()

output_txt = ce('textarea')
output_txt.value = folder_contents
output_txt.style.fontFamily = 'Arial'
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

