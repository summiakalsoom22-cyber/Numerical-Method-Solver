def f(x):
    return x**3 - x - 2


def df(x):
    return 3 * x**2 - 1


def newton_raphson(x0, tolerance=1e-6, max_iterations=100):

    data = []

    x = x0

    for iteration in range(1, max_iterations + 1):

        fx = f(x)
        dfx = df(x)

        if dfx == 0:
            raise ValueError("Derivative is zero.")

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


root, data = newton_raphson(1.5)

print("Approximate root:", root)
print("Number of iterations:", len(data))

print("\nIteration |          x |       f(x) |      Error")
print("-" * 55)

for row in data:
    print(
        f"{row['iteration']:>9} | "
        f"{row['x']:.8f} | "
        f"{row['f(x)']:.8f} | "
        f"{row['error']:.8f}"
    )