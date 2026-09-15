import math

from src.root_finding import bisection
from src.linear_system import gaussian_elimination
from src.interpolation import lagrange_interpolation
from src.differentiation import central_difference
from src.integration import simpson_one_third
from src.ode import rk4


def test_bisection():

    root, _ = bisection(1, 2)

    assert abs(root - 1.5213797) < 1e-5


def test_gaussian_elimination():

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

    expected = [2, 3, -1]

    for actual, target in zip(solution, expected):
        assert abs(actual - target) < 1e-6


def test_lagrange():

    x_values = [0, 1, 2, 3]
    y_values = [1, 3, 2, 5]

    result = lagrange_interpolation(
        x_values,
        y_values,
        1.5
    )

    assert abs(result - 2.4375) < 1e-6


def test_central_difference():

    def f(x):
        return x**3

    result = central_difference(
        f,
        2,
        0.001
    )

    assert abs(result - 12) < 1e-5


def test_simpson():

    def f(x):
        return x**2

    result = simpson_one_third(
        f,
        0,
        2,
        10
    )

    assert abs(result - 8 / 3) < 1e-10


def test_rk4():

    def f(x, y):
        return x + y

    data = rk4(
        f,
        0,
        1,
        0.1,
        10
    )

    numerical = data[-1]["y"]

    exact = 2 * math.exp(1) - 2

    assert abs(numerical - exact) < 1e-4