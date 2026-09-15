def trapezoidal(f, a, b, n):

    h = (b - a) / n

    total = (f(a) + f(b)) / 2

    for i in range(1, n):
        total += f(a + i * h)

    return h * total


def simpson_one_third(f, a, b, n):

    if n % 2 != 0:
        raise ValueError("n must be even.")

    h = (b - a) / n

    total = f(a) + f(b)

    for i in range(1, n):

        x = a + i * h

        if i % 2 == 0:
            total += 2 * f(x)
        else:
            total += 4 * f(x)

    return (h / 3) * total


def simpson_three_eighth(f, a, b, n):

    if n % 3 != 0:
        raise ValueError("n must be divisible by 3.")

    h = (b - a) / n

    total = f(a) + f(b)

    for i in range(1, n):

        x = a + i * h

        if i % 3 == 0:
            total += 2 * f(x)
        else:
            total += 3 * f(x)

    return (3 * h / 8) * total