# scalars_vectors_matrices.py

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

