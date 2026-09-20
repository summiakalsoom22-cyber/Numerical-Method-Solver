import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.differentiation import (
    forward_difference,
    backward_difference,
    central_difference
)


# Function
def f(x):
    return x**3


# Exact derivative of x^3 is 3x^2
x = 2
exact_value = 3 * x**2

# Different step sizes
step_sizes = [0.1, 0.01, 0.001]


print("Differentiation Method Comparison")
print("-" * 80)
print(
    f"{'h':<10}"
    f"{'Forward':<20}"
    f"{'Backward':<20}"
    f"{'Central':<20}"
)
print("-" * 80)


for h in step_sizes:

    forward_result = forward_difference(f, x, h)
    backward_result = backward_difference(f, x, h)
    central_result = central_difference(f, x, h)

    print(
        f"{h:<10}"
        f"{forward_result:<20.10f}"
        f"{backward_result:<20.10f}"
        f"{central_result:<20.10f}"
    )


print("\nExact derivative:")
print(f"f'({x}) = {exact_value:.10f}")


print("\nAbsolute Errors")
print("-" * 80)
print(
    f"{'h':<10}"
    f"{'Forward Error':<20}"
    f"{'Backward Error':<20}"
    f"{'Central Error':<20}"
)
print("-" * 80)


for h in step_sizes:

    forward_result = forward_difference(f, x, h)
    backward_result = backward_difference(f, x, h)
    central_result = central_difference(f, x, h)

    forward_error = abs(forward_result - exact_value)
    backward_error = abs(backward_result - exact_value)
    central_error = abs(central_result - exact_value)

    print(
        f"{h:<10}"
        f"{forward_error:<20.10f}"
        f"{backward_error:<20.10f}"
        f"{central_error:<20.10f}"
    )