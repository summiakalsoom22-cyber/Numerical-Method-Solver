import math
import sys
from pathlib import Path
import matplotlib.pyplot as plt

# Allow Python to find the src folder
sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.ode import euler


# Differential equation:
# dy/dx = x + y
def f(x, y):
    return x + y


# Exact solution:
# y = 2e^x - x - 1
def exact_solution(x):
    return 2 * math.exp(x) - x - 1


x0 = 0
y0 = 1
x_end = 1

step_sizes = [0.1, 0.05, 0.01]
errors = []

exact_value = exact_solution(x_end)

for h in step_sizes:
    n = int((x_end - x0) / h)

    result = euler(f, x0, y0, h, n)

    euler_value = result[-1]["y"]
    error = abs(euler_value - exact_value)

    errors.append(error)


# Plot error against step size
plt.plot(step_sizes, errors, marker="o")

plt.xlabel("Step size (h)")
plt.ylabel("Absolute error")
plt.title("Euler Method: Error vs Step Size")

plt.grid(True)
plt.show()