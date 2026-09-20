import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.interpolation import (
    lagrange_interpolation,
    newton_interpolation,
    newton_forward,
    newton_backward
)

x = [0, 1, 2, 3]
y = [1, 3, 7, 13]

value = 1.5
exact_value = 4.75

lagrange_result = lagrange_interpolation(x, y, value)
newton_result = newton_interpolation(x, y, value)
forward_result = newton_forward(x, y, value)
backward_result = newton_backward(x, y, value)

print("Interpolation Method Comparison")
print("-" * 60)

print(f"Lagrange:                  {lagrange_result:.10f}")
print(f"Newton Divided Difference: {newton_result:.10f}")
print(f"Newton Forward:            {forward_result:.10f}")
print(f"Newton Backward:           {backward_result:.10f}")
print(f"Exact value:               {exact_value:.10f}")