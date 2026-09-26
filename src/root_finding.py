def bisection(f, a, b, tolerance=1e-6, max_iterations=100):

    if f(a) * f(b) >= 0:
        raise ValueError(
            "The interval must contain a sign change."
        )

    data = []

    for iteration in range(1, max_iterations + 1):

        c = (a + b) / 2
        error = (b - a) / 2

        data.append({
            "iteration": iteration,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": f(c),
            "error": error
        })

        if abs(f(c)) < tolerance or error < tolerance:
            return c, data

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    return c, data


def newton_raphson(
    f,
    df,
    x0,
    tolerance=1e-6,
    max_iterations=100
):

    data = []
    x = x0

    for iteration in range(1, max_iterations + 1):

        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError(
                "Derivative is zero."
            )

        x_new = x - fx / dfx
        error = abs(x_new - x)

        data.append({
            "iteration": iteration,
            "x": x_new,
            "f(x)": f(x_new),
            "error": error
        })

        if error < tolerance:
            return x_new, data

        x = x_new

    return x, data


def secant(
    f,
    x0,
    x1,
    tolerance=1e-6,
    max_iterations=100
):

    data = []

    for iteration in range(1, max_iterations + 1):

        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            raise ValueError(
                "Division by zero."
            )

        x2 = (
            x1
            - fx1 * (x1 - x0)
            / (fx1 - fx0)
        )

        error = abs(x2 - x1)

        data.append({
            "iteration": iteration,
            "x": x2,
            "f(x)": f(x2),
            "error": error
        })

        if error < tolerance:
            return x2, data

        x0 = x1
        x1 = x2

    return x2, data


def regula_falsi(
    f,
    a,
    b,
    tolerance=1e-6,
    max_iterations=100
):

    if f(a) * f(b) >= 0:
        raise ValueError(
            "The interval must contain a sign change."
        )

    data = []

    for iteration in range(1, max_iterations + 1):

        fa = f(a)
        fb = f(b)

        c = (
            a * fb - b * fa
        ) / (fb - fa)

        error = (
            abs(c - a)
            if iteration > 1
            else abs(b - a)
        )

        data.append({
            "iteration": iteration,
            "a": a,
            "b": b,
            "c": c,
            "f(c)": f(c),
            "error": error
        })

        if abs(f(c)) < tolerance:
            return c, data

        if fa * f(c) < 0:
            b = c
        else:
            a = c

    return c, data