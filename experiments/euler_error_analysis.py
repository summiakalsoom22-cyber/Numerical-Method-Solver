import math
import sys
from pathlib import Path

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

print("Euler Method Error Analysis")
print("-" * 60)
print(f"{'h':<10}{'Euler Value':<20}{'Exact Value':<20}{'Error'}")
print("-" * 60)

for h in step_sizes:
    n = int((x_end - x0) / h)

    result = euler(f, x0, y0, h, n)

    euler_value = result[-1]["y"]
    exact_value = exact_solution(x_end)
    error = abs(euler_value - exact_value)

    print(f"{h:<10}{euler_value:<20.10f}{exact_value:<20.10f}{error:.10f}")