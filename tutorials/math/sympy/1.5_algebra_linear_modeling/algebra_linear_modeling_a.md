// algebra_linear_modeling_a.md

**Linear Modeling** - building an equation to track a changing state over time.

### Question 5: Linear Modeling

**The Problem:** "A water cooler has $42$ gallons of water in it. Water leaks from the cooler at a rate of $0.5$ gallons per hour. Which of the following equations represents the number of gallons, $v$, of water remaining in the cooler $t$ hours after the leak began?"
**Choices:**
A) $v = 42 - 0.5t$
B) $v = 42 + 0.5t$
C) $v = 0.5 - 42t$
D) $v = 0.5 + 42t$

---

### 1. The Native Markdown Tutorial (`algebra_linear_modeling_a.md`)

// algebra_linear_modeling_a.md

```python
from sympy import symbols, Eq

# Define our variables: v = volume, t = time
v, t = symbols('v t')

# Define the constants given in the requirements
initial_amount = 42
leak_rate = 0.5

# Calculate total leaked over 't' hours
amount_leaked = leak_rate * t

# The remaining volume (v) equals the initial amount minus what leaked
equation = Eq(v, initial_amount - amount_leaked)

print(equation)

```

```text
Eq(v, 42 - 0.5*t)

```

### Understanding Linear Modeling (Tracking State)

When a math problem asks you to track something that changes at a steady rate over time, you are building a linear equation. In programming, this is just tracking a changing state variable.

Let's break the word problem down into variables:

#### Step 1: Find the Starting State (Initial Value)

Before the clock even starts, how much water is in the cooler?
The problem states there are $42$ gallons. This is our constant starting point.

#### Step 2: Find the Rate of Change

What is happening to the water over time?
It is *leaking* (which means subtracting) at a rate of $0.5$ gallons every hour.

If $t$ represents hours, then the total amount of water lost is:


$$0.5 \times t \quad \text{or} \quad 0.5t$$

#### Step 3: Build the Equation

We need an equation for $v$ (the volume remaining).
The remaining volume equals the starting amount minus the amount leaked.

$$v = 42 - 0.5t$$

The correct choice is **A**.

> **Python Tip:** Notice how we used SymPy's `Eq(left_side, right_side)` to build an exact representation of the equation without trying to "solve" it. Sometimes, the formula itself is the answer!

***

### 2. The PySide6 DOM Script (`algebra_linear_modeling.py`)

Here is your `pyside6dom` GUI version. This one is great because we can show the student the English word problem in the first box, and the translated Python/Math logic in the second.

```python
# algebra_linear_modeling.py

from sympy import symbols, Eq
from pyside6dom import *

init_window('Linear Modeling', 800, 600)

# 1. Math Logic
v, t = symbols('v t')
initial_amount = 42
leak_rate = 0.5

# Volume equals initial amount minus (rate * time)
eq = Eq(v, initial_amount - leak_rate * t)

# 2. UI Construction
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

```

---

Word problems are essentially just software requirements. A client tells you what a system is doing in plain English, and your job is to translate that behavior into an algorithm.

---

Notice how in the PySide6 DOM script, I used `eq.rhs`? That stands for "Right Hand Side". It allows you to pull just the `42 - 0.5*t` part out of the SymPy equation object so you can format it beautifully in your GUI as `v = 42 - 0.5*t`.

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

