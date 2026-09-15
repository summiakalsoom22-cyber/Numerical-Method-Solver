def gauss_seidel(A, b, tolerance=1e-6, max_iterations=100):

    n = len(b)

    # Initial guess
    x = [0.0] * n

    data = []

    for iteration in range(1, max_iterations + 1):

        x_old = x[:]

        for i in range(n):

            if abs(A[i][i]) < 1e-12:
                raise ValueError("Zero diagonal element.")

            total = 0

            for j in range(n):

                if j != i:
                    total += A[i][j] * x[j]

            # x[j] may already contain a NEW value
            x[i] = (b[i] - total) / A[i][i]

        # Calculate error
        error = max(
            abs(x[i] - x_old[i])
            for i in range(n)
        )

        data.append({
            "iteration": iteration,
            "x": x[:],
            "error": error
        })

        if error < tolerance:
            return x, data

    return x, data


# Test system
A = [
    [10, 1, 1],
    [2, 10, 1],
    [2, 2, 10]
]

b = [12, 13, 14]

solution, data = gauss_seidel(A, b)

print("Solution:")

for i, value in enumerate(solution):
    print(f"x{i + 1} = {value:.6f}")

print("\nNumber of iterations:", len(data))

print("\nIteration |          x1 |          x2 |          x3 |       Error")
print("-" * 70)

for row in data:
    print(
        f"{row['iteration']:>9} | "
        f"{row['x'][0]:>10.6f} | "
        f"{row['x'][1]:>10.6f} | "
        f"{row['x'][2]:>10.6f} | "
        f"{row['error']:.8f}"
    )