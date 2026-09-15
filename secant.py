def f(x):
    return x**3 - x - 2
def secant(x0, x1, tolerance=1e-6, max_iterations=100):

    data = []

    for iteration in range(1, max_iterations + 1):

        fx0 = f(x0)
        fx1 = f(x1)

        if fx1 - fx0 == 0:
            raise ValueError("Division by zero.")
        x2 =x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        error = abs(x2 - x1)

        data.append({
            "iteration": iteration,
            "x": x2,
            "f(x)": f(x2),
            "error": error
        })

        if error < tolerance:
            return x2, data
        x0=x1
        x1=x2

    return x2, data
root, data = secant(1, 2)

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