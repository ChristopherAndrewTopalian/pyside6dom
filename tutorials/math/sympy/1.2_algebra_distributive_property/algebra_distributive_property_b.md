// foundation_b.md

```python
from sympy import symbols, Mul

r, s = symbols('r s')
sum_rs = r + s

# Way 1: Default SymPy (Auto-Distributes)
expr_default = 5 * sum_rs
print("Default SymPy Output:", expr_default)

# Way 2: Exact Structure (For Multiple Choice Tests)
expr_exact = Mul(5, sum_rs, evaluate=False)
print("Multiple Choice Format:", expr_exact)

```

```text
Default SymPy Output: 5*r + 5*s
Multiple Choice Format: 5*(r + s)

```

### The "Too Smart" Calculator

When preparing for college placement tests like the ACCUPLACER, you will often run into situations where the mathematically "simplified" answer is not the one on the multiple-choice list.

The prompt asks for **$5$ times as much as the sum of $r$ and $s$**.

#### Way 1: The Distributive Property (How Computers Think)

By default, Python's SymPy engine applies the **Distributive Property**. When it sees `5 * (r + s)`, it immediately multiplies the 5 by everything inside the parentheses.

* $5 \times r = 5r$
* $5 \times s = 5s$
It outputs `5*r + 5*s`. Mathematically, this is 100% correct.

#### Way 2: The Structural Form (How Tests are Written)

Standardized tests often want to see if you know how to build the logic structure, not just simplify it. They want you to group the sum first.

To force Python to output the exact multiple-choice answer without doing the math for you, we use `Mul()` with the `evaluate=False` flag. This tells the engine to build the expression exactly as written:

$$(r + s) \times 5$$

If you ever solve a multiple-choice math problem and your answer looks different from the choices, check to see if the test simply left the equation in its structural, un-distributed form!

//----//

// Dedicated to God the Father  

// Copyright (c) 2026-present Christopher Andrew Topalian  
   
// Apache License
   Version 2.0, January 2004
   http://www.apache.org/licenses/  

// GitHub: https://github.com/ChristopherAndrewTopalian/pyside6dom

// PyPI: https://pypi.org/project/pyside6dom/

// https://github.com/ChristopherAndrewTopalian  

// https://github.com/ChristopherTopalian  

// https://sites.google.com/view/CollegeOfScripting

