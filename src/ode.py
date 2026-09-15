def euler(f, x0, y0, h, n):

    data = []

    x = x0
    y = y0

    for iteration in range(n + 1):

        data.append({
            "iteration": iteration,
            "x": x,
            "y": y
        })

        y = y + h * f(x, y)
        x = x + h

    return data


def heun(f, x0, y0, h, n):

    data = []

    x = x0
    y = y0

    for iteration in range(n + 1):

        data.append({
            "iteration": iteration,
            "x": x,
            "y": y
        })

        slope1 = f(x, y)

        y_predict = y + h * slope1
        x_new = x + h

        slope2 = f(x_new, y_predict)

        y = y + (h / 2) * (slope1 + slope2)
        x = x_new

    return data


def rk4(f, x0, y0, h, n):

    data = []

    x = x0
    y = y0

    for iteration in range(n + 1):

        data.append({
            "iteration": iteration,
            "x": x,
            "y": y
        })

        k1 = f(x, y)

        k2 = f(
            x + h / 2,
            y + (h / 2) * k1
        )

        k3 = f(
            x + h / 2,
            y + (h / 2) * k2
        )

        k4 = f(
            x + h,
            y + h * k3
        )

        y = y + (h / 6) * (
            k1 + 2 * k2 + 2 * k3 + k4
        )

        x = x + h

    return data