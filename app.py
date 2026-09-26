import streamlit as st
import math
import pandas as pd

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
def download_csv(dataframe, filename):
    csv= dataframe.to_csv(index=False).encode("utf-8")
    st.download_button(label="📥 Download CSV",
                       data=csv,
                       file_name=filename,
                       mime="text/csv")


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
        #        Root Finding

        "Bisection Method",
        "Newton-Raphson Method",
        "Secant Method",
        "Regula Falsi",
        #        Linear System

        "Gaussian Elimination",
        "Gauss-Jordan Elimination",
        "LU Decomposition",
        "Jacobi Method",
        "Gauss-Seidel Method",
        #          Interpolation 

        "Lagrange Interpolation",
        "Newton Divided Difference",
        "Newton Forward Interpolation",
        "Newton Backward Interpolation",
        #           Differentiation

        "Forward Difference",
        "Backward Difference",
        "Central Difference",
        #          Differentiation Analysis
        "Differentiation Error Analysis",
        # Integration

        "Trapezoidal Rule",
        "Simpson 1/3 Rule",
        "Simpson 3/8 Rule",
        # Integration Analysis 
        "Integration Method Comparison",
        # ODE

        "Euler Method",
        "Heun Method",
        "Runge-Kutta 4 Method",
        # ODE Analysis
        "ODE Method Comparison"
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
            f = create_function(expression)
            root, data = bisection(
                f,
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
    expression = st.text_input("Enter f(x):", value="x**3 - x - 2")
    derivative_expression = st.text_input("Enter f'(x):", value = "3*x**2 - 1")

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
            f = create_function(expression)
            df = create_function(derivative_expression)

            root, data = newton_raphson(
                f,
                df,
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

        except (ValueError, ZeroDivisionError, TypeError, NameError) as error:
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
    expression = st.text_input("Enter f(x):", value="x**3 - x - 2")


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
            f = create_function(expression)

            root, data = secant(
                f,
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

        except ( ValueError, ZeroDivisionError, TypeError, NameError) as error:
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
    expression = st.text_input("Enter f(x):", value = "x**3 - x - 2")

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
            f = create_function(expression)

            root, data = regula_falsi(
                f,
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

        except (ValueError, ZeroDivisionError, TypeError, NameError) as error:
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
    n = int(n)
    st.subheader("Coefficient Matrix A")

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
    st.subheader("Right-hand Side Vector b")

    default_b = ",".join(["0"] * n)

    b_text = st.text_input(
        "Vector b",
        value=default_b
    )
    if method in ["Jacobi Method", "Gauss-Seidel Method"]:

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
                n
            )

            b = parse_values(b_text)

            if len(b) != int(n):
                raise ValueError(
                    f"Vector b must contain {n} values."
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

        except (ValueError, ZeroDivisionError, IndexError) as error:

            st.error(str(error))


# ============================================================
# LAGRANGE INTERPOLATION
# ============================================================

elif method == "Lagrange Interpolation":

    st.header(method)
    st.write("Enter corresponding x and y values separated by commas.")

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
#                   Basic Validation                     
            if len(x_values) != len(y_values):
                raise ValueError(
                    "x and y must contain the same number of values."
                )
            if len(x_values) < 2:
                raise ValueError("At least two data points are required.")
            if len(set(x_values)) != len(x_values):
                        raise ValueError("x values must be unique.")
            #           Lagrange          
            if method=="Lagrange Interpolation":

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
            h = x_values[1] - x_values[0]
            for i in range(1, len(x_values) - 1):
                current_h = ( x_values[i + 1]  -
                             x_values[i]    )
            if abs(current_h - h) > 1e-10:
                raise ValueError("Newton interpolation requires equally spaced x values.")
            

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
            h = x_values[1] - x_values[0]
            for i in range(1, len(x_values) - 1):
                current_h = (x_values[i + 1]   -  x_values[i])
                if abs(current_h  - h)  > 1e-10:
                    raise ValueError("Newton interpolation requires equally spaced x values.")

            result = newton_backward(
                x_values,
                y_values,
                x
            )
            #        Display reslt   

            st.success(
                f"Interpolated value: {result:.10f}"
            )

        except (ValueError, ZeroDivisionError, IndexError) as error:
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
            min_value=0.00000001,
            format="%.8f"
        )
    st.subheader("Optional: exact Derivative")
    exact_derivative_expression = st.text_input("Enter exact derivative  value (optional)", value="")


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
            if exact_derivative_expression.strip():
                exact_value=float(exact_derivative_expression)
                absolute_error=abs(exact_value - result)
            st.subheader("Accuracy Analysis")
            col1, col2= st.columns(2)
            with col1:
                        st.metric("Exact Derivative", f"{exact_value:.10f}")
            with col2:
                        st.metric("Absolute Error", f"{absolute_error:.10e}")

        except (ValueError, ZeroDivisionError, TypeError, NameError) as error:
            st.error(
                f"Error: {error}"
            )
# ============================================================
# DIFFERENTIATION ERROR ANALYSIS
# ============================================================

elif method == "Differentiation Error Analysis":

    st.header("Differentiation Error Analysis")

    st.write(
        "Study how the step size affects the accuracy "
        "of numerical differentiation."
    )

    expression = st.text_input(
        "Enter f(x):",
        value="x**3"
    )

    col1, col2 = st.columns(2)

    with col1:
        x = st.number_input(
            "x",
            value=2.0,
            key="error_x"
        )

    with col2:
        exact_derivative = st.number_input(
            "Exact derivative",
            value=12.0,
            key="exact_derivative"
        )

    if st.button(
        "Run Error Experiment",
        type="primary"
    ):

        try:

            f = create_function(expression)

            step_sizes = [
                0.1,
                0.05,
                0.01,
                0.005,
                0.001,
                0.0005,
                0.0001
            ]

            rows = []

            for step in step_sizes:

                forward = forward_difference(
                    f, x, step
                )

                backward = backward_difference(
                    f, x, step
                )

                central = central_difference(
                    f, x, step
                )

                rows.append({
                    "Step Size (h)": step,
                    "Forward Error": abs(
                        exact_derivative - forward
                    ),
                    "Backward Error": abs(
                        exact_derivative - backward
                    ),
                    "Central Error": abs(
                        exact_derivative - central
                    )
                })

            error_data = pd.DataFrame(rows)

            st.success(
                "Error experiment completed successfully."
            )

            st.subheader("Error Table")

            st.dataframe(
                error_data,
                use_container_width=True
            )
            st.download_button(
    label="📥 Download Error Analysis CSV",
    data=error_data.to_csv(index=False).encode("utf-8"),
    file_name="differentiation_error_analysis.csv",
    mime="text/csv"
)

            st.subheader("Error vs Step Size")

            st.line_chart(
                error_data.set_index(
                    "Step Size (h)"
                )
            )

        except (
            ValueError,
            ZeroDivisionError,
            TypeError,
            NameError
        ) as error:

            st.error(f"Error: {error}")


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
            value=1.0
        )

    n = st.number_input(
        "Number of subintervals (n)",
        min_value=1,
        max_value=10000,
        value=10,
        step=1
    )
    n = int(n)
    st.subheader("Optional: Exact Integral")
    exact_expression = st.text_input("Enter exact integral value (optionAL)", value="")


    if method == "Simpson 1/3 Rule":

        st.info(
            "For Simpson 1/3 Rule, n must be even."
        )

    elif method == "Simpson 3/8 Rule":
        st.info(
            "For Simpson 3/8 Rule, n must be divisible by 3."
        )

    if st.button("Integrate", type="primary"):

        try:

            f = create_function(expression)
            if a == b:
                raise ValueError("Lower and upper limits must be different.")
            if method == "Simpson 1/3 Rule":
                if n % 2 !=0:
                    raise ValueError("For Simpsn 1/3 Rule , n must be even.")
            elif method == "Simpson 3/8 Rule":
                if n % 3 != 0:
                    raise ValueError("For Simpson 3/8 Rule , n must be divisible by 3.")

            if method == "Trapezoidal Rule":

                result = trapezoidal(
                    f,
                    a,
                    b, 
                    n
                )

            elif method == "Simpson 1/3 Rule":
                
                result = simpson_one_third(
                    f,
                    a,
                    b,
                    n
                )

            else:

                result = simpson_three_eighth(
                    f,
                    a,
                    b,
                    n
                )

            st.success(
                f"Approximate integral: {result:.10f}"
            )
            if exact_expression.strip():
                exact_value = float( exact_expression)
                absolute_error = abs(exact_value - result)
            st.subheader("Accuracy Analysis")
            col1, col2 = st.columns(2)
            with col1: 
                        st.metric("Exact Value", f"{exact_value:.10f}")
            with col2:
                        st.metric("Absolute Error", f"{absolute_error:.10e}")
        
        except (ValueError, ZeroDivisionError, TypeError,NameError) as error:
            st.error(
                f"Error: {error}"
            )
# ============================================================
# INTEGRATION METHOD COMPARISON
# ============================================================

elif method == "Integration Method Comparison":

    st.header("Integration Method Comparison")

    st.write(
        "Compare the numerical results and absolute errors "
        "of three integration methods."
    )

    expression = st.text_input(
        "Enter f(x):",
        value="x**2"
    )

    col1, col2 = st.columns(2)

    with col1:
        a = st.number_input(
            "Lower limit (a)",
            value=0.0,
            key="comparison_a"
        )

    with col2:
        b = st.number_input(
            "Upper limit (b)",
            value=1.0,
            key="comparison_b"
        )

    n = st.number_input(
        "Number of subintervals",
        min_value=6,
        max_value=10000,
        value=12,
        step=1,
        key="comparison_integration_n"
    )

    n = int(n)

    exact_value = st.number_input(
        "Exact integral value",
        value=0.3333333333,
        format="%.10f"
    )

    if st.button(
        "Compare Methods",
        type="primary"
    ):

        try:

            f = create_function(expression)

            if n % 2 != 0:
                raise ValueError(
                    "n must be even for Simpson 1/3."
                )

            if n % 3 != 0:
                raise ValueError(
                    "n must be divisible by 3 for Simpson 3/8."
                )

            trapezoid_result = trapezoidal(
                f, a, b, n
            )

            simpson_one_result = simpson_one_third(
                f, a, b, n
            )

            simpson_three_result = simpson_three_eighth(
                f, a, b, n
            )

            comparison = pd.DataFrame({
                "Method": [
                    "Trapezoidal",
                    "Simpson 1/3",
                    "Simpson 3/8"
                ],
                "Approximation": [
                    trapezoid_result,
                    simpson_one_result,
                    simpson_three_result
                ],
                "Absolute Error": [
                    abs(
                        exact_value -
                        trapezoid_result
                    ),
                    abs(
                        exact_value -
                        simpson_one_result
                    ),
                    abs(
                        exact_value -
                        simpson_three_result
                    )
                ]
            })

            st.success(
                "Integration comparison completed successfully."
            )

            st.subheader("Comparison Results")

            st.dataframe(
                comparison,
                use_container_width=True
            )
            st.download_button(
    label="📥 Download Comparison CSV",
    data=comparison.to_csv(index=False).encode("utf-8"),
    file_name="integration_method_comparison.csv",
    mime="text/csv"
)
            st.subheader("Absolute Error Comparison")

            error_data = comparison.set_index("Method")[
                      ["Absolute Error"]
]

            st.bar_chart(error_data)

        except (
            ValueError,
            ZeroDivisionError,
            TypeError,
            NameError
        ) as error:

            st.error(f"Error: {error}")
 # ============================================================
# ODE METHODS
# ============================================================

elif method in [
    "Euler Method",
    "Heun Method",
    "Runge-Kutta 4 Method"
]:

    
    

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
    with col2:

        y0 = st.number_input(
            "Initial y₀",
            value=1.0
        )
        col1, col2 = st.columns(2)

    with col1:

        h = st.number_input(  "Step size (h)",
            value=0.1,
            min_value=0.00000001,
            format="%.8f"
        )
    with col2:

        n = st.number_input(
            "Number of steps",
            min_value=1,
            max_value=10000,
            value=10,
            step=1
        )
        n = int(n)

    if st.button("Solve", type="primary"):

        try:

            f = create_ode_function(expression)

            if method == "Euler Method":

                data = euler(
                    f,
                    x0,
                    y0,
                    h,
                    n
                )

            elif method == "Heun Method":

                data = heun(
                    f,
                    x0,
                    y0,
                    h,
                    n
                )

            else:

                data = rk4(
                    f,
                    x0,
                    y0,
                    h,
                    n
                )

            st.success(f" {method} ODE solved successfully.")

            st.subheader("Solution Table")

            st.dataframe(
                data,
                use_container_width=True
            )
            st.subheader("Final Approximation")
            final_value = data[-1]
            st.metric("Final x", f"{final_value['x']:.10f}")

            

            st.metric(
                    "Final y",
                    f"{data[-1]['y']:.10f}"
                )

        except (ValueError, ZeroDivisionError, TypeError, NameError) as error:
            st.error(
                f"Error: {error}"
            )
# ============================================================
# ODE METHOD COMPARISON
# ============================================================

elif method == "ODE Method Comparison":

    st.header("ODE Method Comparison")

    st.write(
        "Compare Euler, Heun and Runge-Kutta 4 "
        "for the same initial value problem."
    )

    st.latex(r"\frac{dy}{dx}=f(x,y)")

    expression = st.text_input(
        "Enter f(x, y):",
        value="x + y"
    )

    col1, col2 = st.columns(2)

    with col1:
        x0 = st.number_input(
            "Initial x₀",
            value=0.0,
            key="comparison_x0"
        )

    with col2:
        y0 = st.number_input(
            "Initial y₀",
            value=1.0,
            key="comparison_y0"
        )

    col1, col2 = st.columns(2)

    with col1:
        h = st.number_input(
            "Step size (h)",
            value=0.1,
            min_value=0.00000001,
            format="%.8f",
            key="comparison_h"
        )

    with col2:
        n = st.number_input(
            "Number of steps",
            min_value=1,
            max_value=10000,
            value=10,
            step=1,
            key="comparison_n"
        )

    n = int(n)

    if st.button(
        "Compare Methods",
        type="primary"
    ):

        try:

            f = create_ode_function(expression)

            euler_data = euler(
                f, x0, y0, h, n
            )

            heun_data = heun(
                f, x0, y0, h, n
            )

            rk4_data = rk4(
                f, x0, y0, h, n
            )

            st.success(
                "All three ODE methods solved successfully."
            )

            # --------------------------------------------
            # Comparison table
            # --------------------------------------------

            comparison = pd.DataFrame({
                "Method": [
                    "Euler",
                    "Heun",
                    "RK4"
                ],
                "Final x": [
                    euler_data[-1]["x"],
                    heun_data[-1]["x"],
                    rk4_data[-1]["x"]
                ],
                "Final y": [
                    euler_data[-1]["y"],
                    heun_data[-1]["y"],
                    rk4_data[-1]["y"]
                ]
            })

            st.subheader("Final Value Comparison")

            st.dataframe(
                comparison,
                use_container_width=True
            )
            st.download_button(
    label="📥 Download ODE Comparison CSV",
    data=comparison.to_csv(index=False).encode("utf-8"),
    file_name="ode_method_comparison.csv",
    mime="text/csv"
)

            # --------------------------------------------
            # Graph
            # --------------------------------------------

            graph_data = pd.DataFrame({
                "x": [
                    row["x"]
                    for row in euler_data
                ],
                "Euler": [
                    row["y"]
                    for row in euler_data
                ],
                "Heun": [
                    row["y"]
                    for row in heun_data
                ],
                "RK4": [
                    row["y"]
                    for row in rk4_data
                ]
            })

            st.title("Method Comparison Graph")

            st.line_chart(
                graph_data,
                x="x",
                y=["Euler", "Heun", "RK4"]
            )

        except (
            ValueError,
            ZeroDivisionError,
            TypeError,
            NameError
        ) as error:

            st.error(f"Error: {error}")