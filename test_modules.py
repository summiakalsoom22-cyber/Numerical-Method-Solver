from src.root_finding import bisection
from src.linear_system import gaussian_elimination
from src.interpolation import lagrange_interpolation
from src.differentiation import central_difference
from src.integration import simpson_one_third
from src.ode import rk4


# Test Bisection
root, _ = bisection(1, 2)
print("Bisection:", root)


# Test Gaussian Elimination
A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

b = [8, -11, -3]

solution = gaussian_elimination(
    [row[:] for row in A],
    b[:]
)

print("Gaussian Elimination:", solution)


# Test Lagrange Interpolation
x_values = [0, 1, 2, 3]
y_values = [1, 3, 2, 5]

result = lagrange_interpolation(
    x_values,
    y_values,
    1.5
)

print("Lagrange:", result)


# Test Central Difference
def function(x):
    return x**3


result = central_difference(
    function,
    2,
    0.01
)

print("Central Difference:", result)


# Test Simpson's 1/3 Rule
def integration_function(x):
    return x**2


result = simpson_one_third(
    integration_function,
    0,
    2,
    10
)

print("Simpson 1/3:", result)


# Test RK4
def ode_function(x, y):
    return x + y


result = rk4(
    ode_function,
    0,
    1,
    0.1,
    10
)

print("RK4 final value:", result[-1]["y"])


print("\nAll module tests completed.")