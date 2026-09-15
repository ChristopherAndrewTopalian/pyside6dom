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

