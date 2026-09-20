import math


def lagrange_interpolation(x_values, y_values, x):

    n = len(x_values)
    result = 0.0

    for i in range(n):

        term = y_values[i]

        for j in range(n):

            if i != j:
                term *= (
                    (x - x_values[j])
                    / (x_values[i] - x_values[j])
                )

        result += term

    return result


def divided_differences(x_values, y_values):

    n = len(x_values)

    table = [y_values[:]]

    for level in range(1, n):

        previous = table[level - 1]
        current = []

        for i in range(n - level):

            value = (
                previous[i + 1] - previous[i]
            ) / (
                x_values[i + level] - x_values[i]
            )

            current.append(value)

        table.append(current)

    return table


def newton_interpolation(x_values, y_values, x):

    table = divided_differences(
        x_values,
        y_values
    )

    result = table[0][0]
    product = 1.0

    for i in range(1, len(x_values)):

        product *= (
            x - x_values[i - 1]
        )

        result += (
            table[i][0] * product
        )

    return result


def forward_difference_table(y_values):

    table = [y_values[:]]

    while len(table[-1]) > 1:

        previous = table[-1]
        current = []

        for i in range(len(previous) - 1):

            current.append(
                previous[i + 1] - previous[i]
            )

        table.append(current)

    return table


def newton_forward(x_values, y_values, x):

    table = forward_difference_table(y_values)

    h = x_values[1] - x_values[0]

    u = (x - x_values[0]) / h

    result = y_values[0]
    product = 1.0

    for order in range(1, len(y_values)):

        product *= (
            u - (order - 1)
        )

        result += (
            product
            * table[order][0]
            / math.factorial(order)
        )

    return result


def backward_difference_table(y_values):

    table = [y_values[:]]

    while len(table[-1]) > 1:

        previous = table[-1]
        current = []

        for i in range(len(previous) - 1):

            current.append(
                previous[i + 1] - previous[i]
            )

        table.append(current)

    return table


def newton_backward(x_values, y_values, x):

    table = backward_difference_table(y_values)

    h = x_values[1] - x_values[0]

    u = (x - x_values[-1]) / h

    result = y_values[-1]
    product = 1.0

    for order in range(1, len(y_values)):

        product *= (
            u + (order - 1)
        )

        result += (
            product
            * table[order][-1]
            / math.factorial(order)
        )

    return result