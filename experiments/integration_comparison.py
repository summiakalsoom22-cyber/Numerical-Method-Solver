import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.integration import (
    trapezoidal,
    simpson_one_third,
    simpson_three_eighth
)


# Function to integrate
def f(x):
    return x**2


# Integral:
# ∫₀¹ x² dx = 1/3
a = 0
b = 1
n = 6

exact_value = 1 / 3

trapezoidal_result = trapezoidal(f, a, b, n)
simpson_one_third_result = simpson_one_third(f, a, b, n)
simpson_three_eighth_result = simpson_three_eighth(f, a, b, n)

print("Integration Method Comparison")
print("-" * 70)

print(f"Trapezoidal:       {trapezoidal_result:.10f}")
print(f"Simpson 1/3:       {simpson_one_third_result:.10f}")
print(f"Simpson 3/8:       {simpson_three_eighth_result:.10f}")
print(f"Exact value:       {exact_value:.10f}")

print("\nAbsolute Errors")
print("-" * 70)

print(
    f"Trapezoidal:       "
    f"{abs(trapezoidal_result - exact_value):.10f}"
)

print(
    f"Simpson 1/3:       "
    f"{abs(simpson_one_third_result - exact_value):.10f}"
)

print(
    f"Simpson 3/8:       "
    f"{abs(simpson_three_eighth_result - exact_value):.10f}"
)