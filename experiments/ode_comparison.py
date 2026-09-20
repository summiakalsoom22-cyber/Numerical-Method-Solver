import math
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.ode import euler, heun, rk4


def f(x, y):
    return x + y


def exact_solution(x):
    return 2 * math.exp(x) - x - 1


x0 = 0
y0 = 1
h = 0.1
n = 10
x_end = 1

exact_value = exact_solution(x_end)

# Euler
euler_result = euler(f, x0, y0, h, n)
euler_value = euler_result[-1]["y"]
euler_error = abs(euler_value - exact_value)

# Heun
heun_result = heun(f, x0, y0, h, n)
heun_value = heun_result[-1]["y"]
heun_error = abs(heun_value - exact_value)

# RK4
rk4_result = rk4(f, x0, y0, h, n)
rk4_value = rk4_result[-1]["y"]
rk4_error = abs(rk4_value - exact_value)

print("ODE Method Comparison")
print("-" * 60)
print(f"Exact value at x = 1: {exact_value:.10f}")
print("-" * 60)

print(f"Euler : {euler_value:.10f}   Error: {euler_error:.10f}")
print(f"Heun  : {heun_value:.10f}   Error: {heun_error:.10f}")
print(f"RK4   : {rk4_value:.10f}   Error: {rk4_error:.10f}")