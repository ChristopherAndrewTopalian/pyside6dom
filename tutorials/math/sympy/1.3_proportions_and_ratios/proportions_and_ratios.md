// proportions_and_ratios.md

### Question 3: Proportions and Ratios

**The Problem:** "The number of grams of carbohydrates in a 10-ounce serving of a sports drink is 20. How many grams of carbohydrates are in an 8-ounce serving of the sports drink?"
**Choices:** A) 14, B) 16, C) 18, D) 24.

---

### 1. The Native Markdown Tutorial (For the `.md` Codebook)

```markdown
// algebra_proportions.md

```python
from sympy import symbols, Eq, solve, Rational

x = symbols('x')

# 20 grams in 10 oz equals 'x' grams in 8 oz
# We use Rational(20, 10) to keep the math as pure fractions rather than decimals
eq = Eq(Rational(20, 10), x / 8)

sol = solve(eq, x)

print(sol)

```

```text
[16]

```

### Understanding Proportions

This is a classic ratio problem. When comparing two rates that are equal (like the concentration of carbohydrates in a drink), we set up a proportion.

Let's walk through the logic:

#### Step 1: Identify the Known Ratio

The problem tells us there are $20$ grams of carbohydrates in every $10$ ounces.
Written as a fraction, this is:

$$\frac{20}{10}$$

#### Step 2: Set Up the Unknown Ratio

We need to find the amount of carbohydrates ($x$) in an $8$-ounce serving.
Written as a fraction, this is:

$$\frac{x}{8}$$

#### Step 3: Create the Equation

Because the drink's recipe doesn't change, these two ratios must be perfectly equal. We set them equal to each other:

$$\frac{20}{10} = \frac{x}{8}$$

#### Step 4: Solve for $x$

First, simplify the left side. $20 \div 10 = 2$. This tells us there are $2$ grams of carbohydrates per single ounce.

$$2 = \frac{x}{8}$$

To isolate $x$, multiply both sides by $8$:

$$2 \times 8 = x$$

$$16 = x$$

The correct choice is **B: 16**.

***

### 2. The PySide6 DOM Script (For the `.py` GUI file)

```python
# algebra_proportions_gui.py

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

