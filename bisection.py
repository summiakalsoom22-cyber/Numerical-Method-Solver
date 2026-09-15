def f(x):
    return x**3 - x - 2
def bisection(a, b, tolerance=1e-6, max_iterations=100):
    if f(a) * f(b) >= 0:
        raise ValueError("The interval must contain a sign change")
    data = []
    for iteration in range(1, max_iterations + 1):
            c = (a + b) / 2
            error = (b - a) /2
            data.append({"iteration":
iteration,
                "a": a,
                "b": b,
                "c": c,
                "f(c)": f(c),
                "error": error
    })
            if abs(f(c)) < tolerance or error < tolerance:
                return c, data
            if f(a) * f(c) < 0:
                b=c
            else:
                a=c
    return c, data
root, data = bisection(1, 2)
print("Approximate root:", root)
print("Number of iterations:", len(data))
print("\n Iteration |      a   |   b  |      c  |     f(c)  |  Error")
print("-" * 75)
for row in data:
    print(f"{row['iteration']:>9} | "
          f"{row['a']:.8f} | "
          f"{row['b']:.8f} | "
          f"{row['c']:.8f} | "
          f"{row['f(c)']:.8f} | "
          f"{row['error']:.8f}")
           