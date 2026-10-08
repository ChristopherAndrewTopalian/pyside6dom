// foundation_a.md

```python
from sympy import symbols, Eq, solve, Rational

x = symbols('x')
# 1/2x + 3/2(x + 1) - 1/4 = 5
eq = Eq(Rational(1,2)*x + Rational(3,2)*(x + 1) - Rational(1,4), 5)
sol = solve(eq, x)
print(sol)

```

```text
[15/8]


```

Let's walk through it step-by-step using the exact logic a computer would use to parse it.

The equation is:


$$\frac{1}{2}x + \frac{3}{2}(x + 1) - \frac{1}{4} = 5$$

### Step 1: Distribute (Expand the Parentheses)

Just like passing a variable into a function, the $\frac{3}{2}$ on the outside applies to everything inside the parentheses. Multiply $\frac{3}{2}$ by $x$, and then by $1$:


$$\frac{3}{2} \times x = \frac{3}{2}x$$

$$\frac{3}{2} \times 1 = \frac{3}{2}$$

Now plug that back into the main equation:


$$\frac{1}{2}x + \frac{3}{2}x + \frac{3}{2} - \frac{1}{4} = 5$$

### Step 2: Combine Like Terms (The Variables)

Because $\frac{1}{2}x$ and $\frac{3}{2}x$ have the same denominator, you can just add their top numbers (numerators) together:


$$1 + 3 = 4$$


So, $\frac{1}{2}x + \frac{3}{2}x$ becomes $\frac{4}{2}x$.
Since $4 \div 2 = 2$, this simplifies beautifully down to just **$2x$**.

The equation is now much cleaner:


$$2x + \frac{3}{2} - \frac{1}{4} = 5$$

### Step 3: Combine the Fractions

Now handle the numbers. You need to subtract $\frac{1}{4}$ from $\frac{3}{2}$. To do this, they need a common denominator. If you multiply the top and bottom of $\frac{3}{2}$ by $2$, you get $\frac{6}{4}$.

Now subtract:


$$\frac{6}{4} - \frac{1}{4} = \frac{5}{4}$$

The equation is now:


$$2x + \frac{5}{4} = 5$$

### Step 4: Isolate x

Move the $\frac{5}{4}$ to the other side by subtracting it from $5$.
To subtract a fraction from a whole number, turn the whole number into a fraction. Since $5$ is the same as $\frac{20}{4}$:


$$\frac{20}{4} - \frac{5}{4} = \frac{15}{4}$$

Now you are left with:


$$2x = \frac{15}{4}$$

To get $x$ by itself, divide both sides by 2 (which is the same as multiplying the denominator by 2):


$$x = \frac{15}{8}$$

The correct choice is **C: 15/8**.

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

