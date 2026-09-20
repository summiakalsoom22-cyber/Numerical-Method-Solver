import streamlit as st
import math

# ============================================================
# IMPORT YOUR EXISTING NUMERICAL METHODS
# ============================================================

from src.root_finding import (
    bisection,
    newton_raphson,
    secant,
    regula_falsi
)

from src.linear_system import (
    gaussian_elimination,
    gauss_jordan,
    lu_decomposition,
    jacobi,
    gauss_seidel
)

from src.interpolation import (
    lagrange_interpolation,
    newton_interpolation,
    newton_forward,
    newton_backward
)

from src.differentiation import (
    forward_difference,
    backward_difference,
    central_difference
)

from src.integration import (
    trapezoidal,
    simpson_one_third,
    simpson_three_eighth
)

from src.ode import (
    euler,
    heun,
    rk4
)


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Numerical Method Solver",
    page_icon="📐",
    layout="wide"
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def create_function(expression):
    """
    Convert a user-entered mathematical expression
    into a Python function of x.
    """

    allowed = {
        "x": None,
        "math": math,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "abs": abs
    }

    def f(x):
        allowed["x"] = x
        return eval(expression, {"__builtins__": {}}, allowed)

    return f


def create_ode_function(expression):
    """
    Convert a user-entered ODE expression
    into a Python function of x and y.
    """

    allowed = {
        "x": None,
        "y": None,
        "math": math,
        "sin": math.sin,
        "cos": math.cos,
        "tan": math.tan,
        "exp": math.exp,
        "log": math.log,
        "sqrt": math.sqrt,
        "pi": math.pi,
        "e": math.e,
        "abs": abs
    }

    def f(x, y):
        allowed["x"] = x
        allowed["y"] = y
        return eval(expression, {"__builtins__": {}}, allowed)

    return f


def parse_values(text):
    """
    Convert comma-separated numbers into a list of floats.

    Example:
    1, 2, 3, 4
    """

    return [
        float(value.strip())
        for value in text.split(",")
        if value.strip()
    ]


def parse_matrix(text, n):
    """
    Convert rows of a matrix entered as comma-separated values.

    Example for 2x2:

    1,2
    3,4
    """

    rows = text.strip().splitlines()

    if len(rows) != n:
        raise ValueError(
            f"Please enter exactly {n} rows."
        )

    matrix = []

    for row in rows:

        values = [
            float(value.strip())
            for value in row.split(",")
            if value.strip()
        ]

        if len(values) != n:
            raise ValueError(
                f"Each row must contain exactly {n} values."
            )

        matrix.append(values)

    return matrix


# ============================================================
# TITLE
# ============================================================

st.title("📐 Numerical Method Solver")

st.write(
    "A Python-based numerical computing application "
    "for solving mathematical problems using numerical methods."
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("📚 Numerical Methods")

method = st.sidebar.selectbox(
    "Choose a method:",
    [
        "Home",

        "Bisection Method",
        "Newton-Raphson Method",
        "Secant Method",
        "Regula Falsi",

        "Gaussian Elimination",
        "Gauss-Jordan Elimination",
        "LU Decomposition",
        "Jacobi Method",
        "Gauss-Seidel Method",

        "Lagrange Interpolation",
        "Newton Divided Difference",
        "Newton Forward Interpolation",
        "Newton Backward Interpolation",

        "Forward Difference",
        "Backward Difference",
        "Central Difference",

        "Trapezoidal Rule",
        "Simpson 1/3 Rule",
        "Simpson 3/8 Rule",

        "Euler Method",
        "Heun Method",
        "Runge-Kutta 4 Method"
    ]
)


# ============================================================
# HOME
# ============================================================

if method == "Home":

    st.header("Welcome! 👋")

    st.write(
        "Welcome to the Numerical Method Solver."
    )

    st.write(
        "This application provides a collection of "
        "fundamental numerical methods implemented in Python."
    )

    st.divider()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("🔍 Root Finding")
        st.write(
            "Bisection, Newton-Raphson, Secant "
            "and Regula Falsi."
        )

    with col2:
        st.subheader("🧮 Linear Systems")
        st.write(
            "Gaussian Elimination, Gauss-Jordan, "
            "LU, Jacobi and Gauss-Seidel."
        )

    with col3:
        st.subheader("📈 Interpolation")
        st.write(
            "Lagrange, Newton Divided Difference, "
            "Forward and Backward interpolation."
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("📐 Differentiation")
        st.write(
            "Forward, Backward and Central Difference."
        )

    with col2:
        st.subheader("∫ Integration")
        st.write(
            "Trapezoidal, Simpson 1/3 and Simpson 3/8."
        )

    with col3:
        st.subheader("📊 ODEs")
        st.write(
            "Euler, Heun and Runge-Kutta 4."
        )

    st.divider()

    st.info(
        "Select a numerical method from the sidebar "
        "to start solving a problem."
    )


# ============================================================
# BISECTION
# ============================================================

elif method == "Bisection Method":

    st.header("Bisection Method")

    expression = st.text_input(
        "Enter f(x):",
        value="x**3 - x - 2"
    )

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input(
            "Lower bound (a)",
            value=1.0
        )

    with col2:
        b = st.number_input(
            "Upper bound (b)",
            value=2.0
        )

    tolerance = st.number_input(
        "Tolerance",
        value=0.000001,
        format="%.8f"
    )

    max_iterations = st.number_input(
        "Maximum iterations",
        min_value=1,
        max_value=10000,
        value=100,
        step=1
    )

    if st.button("Solve", type="primary"):

        try:
            # Bisection in your module uses its own f(x),
            # so it currently works with x^3-x-2.
            root, data = bisection(
                a,
                b,
                tolerance=tolerance,
                max_iterations=max_iterations
            )

            st.success(
                f"Approximate Root: {root:.10f}"
            )

            st.dataframe(
                data,
                use_container_width=True
            )

        except ValueError as error:
            st.error(str(error))


# ============================================================
# NEWTON-RAPHSON
# ============================================================

elif method == "Newton-Raphson Method":

    st.header("Newton-Raphson Method")

    st.info(
        "The current Newton-Raphson implementation uses "
        "f(x) = x³ - x - 2 and its derivative."
    )

    x0 = st.number_input(
        "Initial guess (x₀)",
        value=1.5
    )

    tolerance = st.number_input(
        "Tolerance",
        value=0.000001,
        format="%.8f"
    )

    max_iterations = st.number_input(
        "Maximum iterations",
        min_value=1,
        max_value=10000,
        value=100,
        step=1
    )

    if st.button("Solve", type="primary"):

        try:

            root, data = newton_raphson(
                x0,
                tolerance=tolerance,
                max_iterations=max_iterations
            )

            st.success(
                f"Approximate Root: {root:.10f}"
            )

            st.dataframe(
                data,
                use_container_width=True
            )

        except ValueError as error:
            st.error(str(error))


# ============================================================
# SECANT
# ============================================================

elif method == "Secant Method":

    st.header("Secant Method")

    st.info(
        "The current Secant implementation uses "
        "f(x) = x³ - x - 2."
    )

    col1, col2 = st.columns(2)

    with col1:
        x0 = st.number_input(
            "Initial value x₀",
            value=1.0
        )

    with col2:
        x1 = st.number_input(
            "Initial value x₁",
            value=2.0
        )

    tolerance = st.number_input(
        "Tolerance",
        value=0.000001,
        format="%.8f"
    )

    max_iterations = st.number_input(
        "Maximum iterations",
        min_value=1,
        max_value=10000,
        value=100,
        step=1
    )

    if st.button("Solve", type="primary"):

        try:

            root, data = secant(
                x0,
                x1,
                tolerance=tolerance,
                max_iterations=max_iterations
            )

            st.success(
                f"Approximate Root: {root:.10f}"
            )

            st.dataframe(
                data,
                use_container_width=True
            )

        except ValueError as error:
            st.error(str(error))


# ============================================================
# REGULA FALSI
# ============================================================

elif method == "Regula Falsi":

    st.header("Regula Falsi Method")

    st.info(
        "The current Regula Falsi implementation uses "
        "f(x) = x³ - x - 2."
    )

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input(
            "Lower bound (a)",
            value=1.0
        )

    with col2:
        b = st.number_input(
            "Upper bound (b)",
            value=2.0
        )

    tolerance = st.number_input(
        "Tolerance",
        value=0.000001,
        format="%.8f"
    )

    max_iterations = st.number_input(
        "Maximum iterations",
        min_value=1,
        max_value=10000,
        value=100,
        step=1
    )

    if st.button("Solve", type="primary"):

        try:

            root, data = regula_falsi(
                a,
                b,
                tolerance=tolerance,
                max_iterations=max_iterations
            )

            st.success(
                f"Approximate Root: {root:.10f}"
            )

            st.dataframe(
                data,
                use_container_width=True
            )

        except ValueError as error:
            st.error(str(error))


# ============================================================
# LINEAR SYSTEMS
# ============================================================

elif method in [
    "Gaussian Elimination",
    "Gauss-Jordan Elimination",
    "LU Decomposition",
    "Jacobi Method",
    "Gauss-Seidel Method"
]:

    st.header(method)

    n = st.number_input(
        "Number of variables",
        min_value=2,
        max_value=10,
        value=3,
        step=1
    )

    st.write(
        "Enter the coefficient matrix A. "
        "Use one row per line and commas between values."
    )

    default_matrix = "\n".join(
        [
            ",".join(
                "1" if i == j else "0"
                for j in range(n)
            )
            for i in range(n)
        ]
    )

    matrix_text = st.text_area(
        "Matrix A",
        value=default_matrix,
        height=150
    )

    default_b = ",".join(["0"] * n)

    b_text = st.text_input(
        "Vector b",
        value=default_b
    )

    tolerance = st.number_input(
        "Tolerance",
        value=0.000001,
        format="%.8f"
    )

    max_iterations = st.number_input(
        "Maximum iterations",
        min_value=1,
        max_value=10000,
        value=100,
        step=1
    )

    if st.button("Solve", type="primary"):

        try:

            A = parse_matrix(
                matrix_text,
                int(n)
            )

            b = parse_values(b_text)

            if len(b) != int(n):
                raise ValueError(
                    f"Vector b must contain {int(n)} values."
                )

            # Fresh copies because some methods modify matrices.
            A_copy = [row[:] for row in A]
            b_copy = b[:]

            if method == "Gaussian Elimination":

                solution = gaussian_elimination(
                    A_copy,
                    b_copy
                )

            elif method == "Gauss-Jordan Elimination":

                solution = gauss_jordan(
                    A_copy,
                    b_copy
                )

            elif method == "LU Decomposition":

                solution = lu_decomposition(
                    A_copy,
                    b_copy
                )

            elif method == "Jacobi Method":

                solution = jacobi(
                    A_copy,
                    b_copy,
                    tolerance=tolerance,
                    max_iterations=max_iterations
                )

            else:

                solution = gauss_seidel(
                    A_copy,
                    b_copy,
                    tolerance=tolerance,
                    max_iterations=max_iterations
                )

            st.success("System solved successfully.")

            st.subheader("Solution")

            for i, value in enumerate(solution, start=1):

                st.metric(
                    f"x{i}",
                    f"{value:.10f}"
                )

        except (ValueError, ZeroDivisionError) as error:

            st.error(str(error))


# ============================================================
# LAGRANGE INTERPOLATION
# ============================================================

elif method == "Lagrange Interpolation":

    st.header("Lagrange Interpolation")

    x_text = st.text_input(
        "x values",
        value="0,1,2,3"
    )

    y_text = st.text_input(
        "y values",
        value="1,2,5,10"
    )

    x = st.number_input(
        "Find y at x =",
        value=1.5
    )

    if st.button("Interpolate", type="primary"):

        try:

            x_values = parse_values(x_text)
            y_values = parse_values(y_text)

            if len(x_values) != len(y_values):
                raise ValueError(
                    "x and y must contain the same number of values."
                )

            result = lagrange_interpolation(
                x_values,
                y_values,
                x
            )

            st.success(
                f"Interpolated value: {result:.10f}"
            )

        except ValueError as error:
            st.error(str(error))


# ============================================================
# NEWTON DIVIDED DIFFERENCE
# ============================================================

elif method == "Newton Divided Difference":

    st.header("Newton Divided Difference Interpolation")

    x_text = st.text_input(
        "x values",
        value="0,1,2,3"
    )

    y_text = st.text_input(
        "y values",
        value="1,2,5,10"
    )

    x = st.number_input(
        "Find y at x =",
        value=1.5
    )

    if st.button("Interpolate", type="primary"):

        try:

            x_values = parse_values(x_text)
            y_values = parse_values(y_text)

            if len(x_values) != len(y_values):
                raise ValueError(
                    "x and y must contain the same number of values."
                )

            result = newton_interpolation(
                x_values,
                y_values,
                x
            )

            st.success(
                f"Interpolated value: {result:.10f}"
            )

        except (ValueError, ZeroDivisionError) as error:
            st.error(str(error))


# ============================================================
# NEWTON FORWARD
# ============================================================

elif method == "Newton Forward Interpolation":

    st.header("Newton Forward Interpolation")

    x_text = st.text_input(
        "x values",
        value="0,1,2,3"
    )

    y_text = st.text_input(
        "y values",
        value="1,2,5,10"
    )

    x = st.number_input(
        "Find y at x =",
        value=1.5
    )

    if st.button("Interpolate", type="primary"):

        try:

            x_values = parse_values(x_text)
            y_values = parse_values(y_text)

            if len(x_values) != len(y_values):
                raise ValueError(
                    "x and y must contain the same number of values."
                )

            if len(x_values) < 2:
                raise ValueError(
                    "At least two data points are required."
                )

            result = newton_forward(
                x_values,
                y_values,
                x
            )

            st.success(
                f"Interpolated value: {result:.10f}"
            )

        except (ValueError, ZeroDivisionError) as error:
            st.error(str(error))


# ============================================================
# NEWTON BACKWARD
# ============================================================

elif method == "Newton Backward Interpolation":

    st.header("Newton Backward Interpolation")

    x_text = st.text_input(
        "x values",
        value="0,1,2,3"
    )

    y_text = st.text_input(
        "y values",
        value="1,2,5,10"
    )

    x = st.number_input(
        "Find y at x =",
        value=1.5
    )

    if st.button("Interpolate", type="primary"):

        try:

            x_values = parse_values(x_text)
            y_values = parse_values(y_text)

            if len(x_values) != len(y_values):
                raise ValueError(
                    "x and y must contain the same number of values."
                )

            if len(x_values) < 2:
                raise ValueError(
                    "At least two data points are required."
                )

            result = newton_backward(
                x_values,
                y_values,
                x
            )

            st.success(
                f"Interpolated value: {result:.10f}"
            )

        except (ValueError, ZeroDivisionError) as error:
            st.error(str(error))


# ============================================================
# DIFFERENTIATION
# ============================================================

elif method in [
    "Forward Difference",
    "Backward Difference",
    "Central Difference"
]:

    st.header(method)

    expression = st.text_input(
        "Enter f(x):",
        value="x**3"
    )

    col1, col2 = st.columns(2)

    with col1:

        x = st.number_input(
            "x",
            value=2.0
        )

    with col2:

        h = st.number_input(
            "Step size (h)",
            value=0.01,
            format="%.8f"
        )

    if st.button("Differentiate", type="primary"):

        try:

            f = create_function(expression)

            if method == "Forward Difference":

                result = forward_difference(
                    f,
                    x,
                    h
                )

            elif method == "Backward Difference":

                result = backward_difference(
                    f,
                    x,
                    h
                )

            else:

                result = central_difference(
                    f,
                    x,
                    h
                )

            st.success(
                f"Approximate derivative: {result:.10f}"
            )

        except Exception as error:
            st.error(
                f"Error: {error}{error}"
            )


# ============================================================
# INTEGRATION
# ============================================================

elif method in [
    "Trapezoidal Rule",
    "Simpson 1/3 Rule",
    "Simpson 3/8 Rule"
]:

    st.header(method)

    expression = st.text_input(
        "Enter f(x):",
        value="x**2"
    )

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input(
            "Lower limit (a)",
            value=0.0
        )

    with col2:

        b = st.number_input(
            "Upper limit (b)",
            value=2.0
        )

    n = st.number_input(
        "Number of subintervals (n)",
        min_value=1,
        max_value=10000,
        value=10,
        step=1
    )

    if method == "Simpson 1/3 Rule":

        st.info(
            "For Simpson 1/3 Rule, n must be even."
        )

    if method == "Simpson 3/8 Rule":
        st.info(
            "For Simpson 3/8 Rule, n must be divisible by 3."
        )

    if st.button("Integrate", type="primary"):

        try:

            f = create_function(expression)

            if method == "Trapezoidal Rule":

                result = trapezoidal(
                    f,
                    a,
                    b,
                    int(n)
                )

            elif method == "Simpson 1/3 Rule":
                result = simpson_one_third(
                    f,
                    a,
                    b,
                    int(n)
                )

            else:

                result = simpson_three_eighth(
                    f,
                    a,
                    b,
                    int(n)
                )

            st.success(
                f"Approximate integral: {result:.10f}"
            )

        except Exception as error:
            st.error(
                f"Error: {error}"
            )
 # ============================================================
# ODE METHODS
# ============================================================

elif method in [
    "Euler Method",
    "Heun Method",
    "Runge-Kutta 4 Method"
]:

    st.header(method)

    st.write(
        "Solve the first-order differential equation:"
    )

    st.latex(
        r"\frac{dy}{dx} = f(x,y)"
    )

    expression = st.text_input(
        "Enter f(x, y):",
        value="x + y"
    )

    col1, col2 = st.columns(2)

    with col1:

        x0 = st.number_input(
            "Initial x₀",
            value=0.0
        )

        y0 = st.number_input(
            "Initial y₀",
            value=1.0
        )

    with col2:

        h = st.number_input(
            "Step size (h)",
            value=0.1,
            format="%.4f"
        )

        n = st.number_input(
            "Number of steps",
            min_value=1,
            max_value=10000,
            value=10,
            step=1
        )

    if st.button("Solve", type="primary"):

        try:

            f = create_ode_function(expression)

            if method == "Euler Method":

                data = euler(
                    f,
                    x0,
                    y0,
                    h,
                    int(n)
                )

            elif method == "Heun Method":

                data = heun(
                    f,
                    x0,
                    y0,
                    h,
                    int(n)
                )

            else:

                data = rk4(
                    f,
                    x0,
                    y0,
                    h,
                    int(n)
                )

            st.success("ODE solved successfully.")

            st.subheader("Solution Table")

            st.dataframe(
                data,
                use_container_width=True
            )

            if data:

                st.metric(
                    "Final y",
                    f"{data[-1]['y']:.10f}"
                )

        except Exception as error:
            st.error(
                f"Error: {error}"
            )