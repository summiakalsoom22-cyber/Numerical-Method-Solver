import math

from src.root_finding import ( bisection, newton_raphson, secant, regula_falsi)
from src.linear_system import ( gaussian_elimination, gauss_jordan, lu_decomposition, jacobi, gauss_seidel)
from src.interpolation import ( lagrange_interpolation, newton_interpolation, newton_forward, newton_backward)
from src.differentiation import( central_difference, forward_difference, backward_difference)
from src.integration import ( simpson_one_third, trapezoidal, simpson_three_eighth)
from src.ode import ( rk4, euler, heun)


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
def test_newton_raphson():
    root, _ = newton_raphson(1.5)
    assert abs(root - 1.5213797068) < 1e-5


def test_secant():
    root, _ = secant(1, 2)
    assert abs(root - 1.5213797068) < 1e-5


def test_regula_falsi():
    root, _ = regula_falsi(1, 2)
    assert abs(root - 1.5213797068) < 1e-5


def test_gauss_jordan():
    A = [
        [2, 1, -1],
        [-3, -1, 2],
        [-2, 1, 2]
    ]
    b = [8, -11, -3]

    result = gauss_jordan(A, b)

    assert all(abs(result[i] - [2, 3, -1][i]) < 1e-6
               for i in range(3))


def test_lu_decomposition():
    A = [
        [4, 3],
        [6, 3]
    ]
    b = [10, 12]

    result = lu_decomposition(A, b)

    assert all(abs(result[i] - [1, 2][i]) < 1e-6
               for i in range(2))


def test_jacobi():
    A = [
        [10, 1, 1],
        [2, 10, 1],
        [2, 2, 10]
    ]
    b = [12, 13, 14]

    result = jacobi(A, b)

    expected = [1, 1, 1]

    assert all(abs(result[i] - expected[i]) < 1e-5
               for i in range(3))


def test_gauss_seidel():
    A = [
        [10, 1, 1],
        [2, 10, 1],
        [2, 2, 10]
    ]
    b = [12, 13, 14]

    result = gauss_seidel(A, b)

    expected = [1, 1, 1]

    assert all(abs(result[i] - expected[i]) < 1e-5
               for i in range(3))


def test_newton_interpolation():
    x_values = [0, 1, 2, 3]
    y_values = [1, 3, 2, 5]

    result = newton_interpolation(x_values, y_values, 1.5)

    assert abs(result - 2.4375) < 1e-6


def test_newton_forward():
    x_values = [0, 1, 2, 3]
    y_values = [1, 3, 2, 5]

    result = newton_forward(x_values, y_values, 1.5)

    assert abs(result - 2.4375) < 1e-6


def test_newton_backward():
    x_values = [0, 1, 2, 3]
    y_values = [1, 3, 2, 5]

    result = newton_backward(x_values, y_values, 1.5)

    assert abs(result - 2.4375) < 1e-6


def test_forward_difference():
    f = lambda x: x**3

    result = forward_difference(f, 2, 0.0001)

    assert abs(result - 12) < 0.01


def test_backward_difference():
    f = lambda x: x**3

    result = backward_difference(f, 2, 0.0001)

    assert abs(result - 12) < 0.01


def test_trapezoidal():
    f = lambda x: x**2

    result = trapezoidal(f, 0, 2, 100)

    assert abs(result - 8/3) < 1e-3


def test_simpson_three_eighth():
    f = lambda x: x**2

    result = simpson_three_eighth(f, 0, 2, 6)

    assert abs(result - 8/3) < 1e-6


def test_euler():
    f = lambda x, y: x + y

    result = euler(f, 0, 1, 0.1, 10)

    assert abs(result[-1]["y"] - 3.1874849202) < 1e-6
def test_euler_error():
    f = lambda x, y: x + y

    x0 = 0
    y0 = 1
    h = 0.1
    n = 10

    result = euler(f, x0, y0, h, n)

    euler_value = result[-1]["y"]

    # Exact solution: y = 2e^x - x - 1
    exact_value = 2 * math.exp(1) - 1 - 1

    error = abs(euler_value - exact_value)

    assert error < 0.25
def test_euler_error_vs_step_size():
    f = lambda x, y: x + y

    x0 = 0
    y0 = 1
    x_end = 1

    exact_value = 2 * math.exp(1) - 1 - 1

    errors = []

    for h in [0.1, 0.05, 0.01]:
        n = int((x_end - x0) / h)

        result = euler(f, x0, y0, h, n)
        euler_value = result[-1]["y"]

        error = abs(euler_value - exact_value)
        errors.append(error)

    assert errors[1] < errors[0]
    assert errors[2] < errors[1]


def test_heun():
    f = lambda x, y: x + y

    result = heun(f, 0, 1, 0.1, 10)

    assert abs(result[-1]["y"] - 3.4365636569) < 0.01