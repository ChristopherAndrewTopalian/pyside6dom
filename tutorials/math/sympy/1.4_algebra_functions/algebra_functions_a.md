// question4_a.md

### Question 4: Function Evaluation

**The Problem:** "If $f(x) = -3x + 5$, what is the value of $f(-2)$?"
**Choices:** A) $-1$, B) $1$, C) $11$, D) $-11$.

This is a massive concept for computer science because algebraic functions and programming functions are essentially the exact same thing. We are just passing an argument (`-2`) into a parameter (`x`).

---

### 1. The Native Markdown Tutorial (`algebra_functions.md`)

```markdown
// algebra_functions.md

```python
from sympy import symbols

x = symbols('x')

# Define the expression (the function's return value)
f_x = -3*x + 5

# Substitute -2 in place of x
result = f_x.subs(x, -2)

print(result)

```

```text
11

```

### Understanding Functions and Substitution

In algebra, the notation $f(x)$ translates directly to how we write functions in programming. It means "a function named $f$ that takes an input parameter called $x$."

The problem gives us the function definition:


$$f(x) = -3x + 5$$

It then asks for the value of $f(-2)$. In programming terms, it is asking you to call the function and pass `-2` as the argument.

#### Step 1: Substitute the Variable

Everywhere you see an $x$ in the equation, replace it with $-2$. Always use parentheses when substituting negative numbers to avoid mixing up your positive and negative signs!

$$-3(-2) + 5$$

#### Step 2: Multiply

Multiply $-3$ by $-2$. Remember the rule: a negative times a negative equals a positive.

$$6 + 5$$

#### Step 3: Add

Add the remaining numbers together.

$$11$$

The correct choice is **C: 11**.

> **Python Tip:** In SymPy, we handle this exact process using the `.subs()` method, which tells the engine to substitute a specific value into our symbolic variable.

***

### 2. The PySide6 DOM Script (`algebra_functions_gui.py`)

Here is the GUI version. It introduces the `.subs()` (substitute) method, which is how SymPy handles variable assignment on the fly.

```python
# algebra_functions_gui.py

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

```

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

