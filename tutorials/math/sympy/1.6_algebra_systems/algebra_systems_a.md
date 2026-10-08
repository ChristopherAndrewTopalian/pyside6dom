// algebra_systems_a.md

**Systems of Equations**.

In programming, a system of equations is just a program with two variables and two rules (constraints) that must both evaluate to `True` at the exact same time.

### Question 6: Systems of Equations

**The Problem:** "What is the solution $(x, y)$ to the following system of equations?"
Equation 1: $2x - 3y = 12$
Equation 2: $x + y = 1$
**Choices:** A) $(3, -2)$, B) $(-3, -6)$, C) $(3, 2)$, D) $(-3, 6)$.

---

### 1. The Native Markdown Tutorial (`algebra_systems.md`)

```markdown
// algebra_systems.md

```python
from sympy import symbols, Eq, solve

# We now have two variables to track
x, y = symbols('x y')

# Define both constraints (equations)
eq1 = Eq(2*x - 3*y, 12)
eq2 = Eq(x + y, 1)

# Pass both equations into solve() as a tuple
solution = solve((eq1, eq2), (x, y))

print(solution)

```

```text
{x: 3, y: -2}

```

### Understanding Systems of Equations

When you have two unknown variables ($x$ and $y$), you need two separate equations to figure out what they are. To solve this manually, we use a programming concept called **Substitution**: we isolate one variable, and substitute it into the other equation.

Let's break it down:

#### Step 1: Isolate a Variable

Look at the second equation: $x + y = 1$. It is very easy to isolate $y$ here.
Subtract $x$ from both sides to get $y$ by itself:

$$y = 1 - x$$

#### Step 2: Substitute into the Other Equation

Now that we know $y$ is exactly the same thing as $(1 - x)$, we can swap that into our first equation.
The original first equation is:

$$2x - 3y = 12$$

Substitute our new $y$ value in:

$$2x - 3(1 - x) = 12$$

#### Step 3: Solve for $x$

Distribute the $-3$ into the parentheses (remembering that $-3 \times -x = +3x$):

$$2x - 3 + 3x = 12$$

Combine your $x$'s:

$$5x - 3 = 12$$

Add $3$ to the other side:

$$5x = 15$$

Divide by $5$:

$$x = 3$$

#### Step 4: Find $y$

Now that we know $x = 3$, plug it back into our easy equation from Step 1:

$$y = 1 - x$$

$$y = 1 - 3$$

$$y = -2$$

Our final answer is $x = 3$ and $y = -2$, written as the coordinate pair $(3, -2)$.

The correct choice is **A: (3, -2)**.

> **Python Tip:** SymPy handles this instantly. By passing a tuple of equations `(eq1, eq2)` and a tuple of variables `(x, y)` into the `solve()` function, it automatically maps the constraints and returns a dictionary with the exact values!

***

### 2. The PySide6 DOM Script (`algebra_systems_gui.py`)

Here is how you display it in your GUI. Because SymPy returns a Python dictionary (like `{x: 3, y: -2}`) for systems of equations, we can format the output directly into a standard $(x, y)$ coordinate format for the student.

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

```

This is where the magic of combining Python with math really shines. A student doing this on paper might get lost in the negative signs during the distribution step, but looking at the script shows them that it's all just data being passed between functions!