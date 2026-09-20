import sys
from pathlib import Path
import matplotlib.pyplot as plt

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.differentiation import (
    forward_difference,
    backward_difference,
    central_difference
)


def f(x):
    return x**3


x = 2
exact_value = 12

step_sizes = [0.1, 0.01, 0.001, 0.0001]

forward_errors = []
backward_errors = []
central_errors = []


for h in step_sizes:

    forward_result = forward_difference(f, x, h)
    backward_result = backward_difference(f, x, h)
    central_result = central_difference(f, x, h)

    forward_errors.append(
        abs(forward_result - exact_value)
    )

    backward_errors.append(
        abs(backward_result - exact_value)
    )

    central_errors.append(
        abs(central_result - exact_value)
    )


plt.figure()

plt.loglog(
    step_sizes,
    forward_errors,
    marker="o",
    label="Forward Difference"
)

plt.loglog(
    step_sizes,
    backward_errors,
    marker="o",
    label="Backward Difference"
)

plt.loglog(
    step_sizes,
    central_errors,
    marker="o",
    label="Central Difference"
)

plt.xlabel("Step size (h)")
plt.ylabel("Absolute Error")
plt.title("Differentiation Methods: Error vs Step Size")

plt.legend()
plt.grid(True)

plt.show()