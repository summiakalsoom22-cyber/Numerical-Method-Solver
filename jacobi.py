def jacobi(A, b, tolerance=1e-6, max_iteration=100):
    n = len(b)
    # initial guess
    x = [0.0] * n
    data = []
    for iteration in range(1, max_iteration + 1):
        x_new = [0.0] * n
        for i in range(n):
            if abs(A[i][i]) < 1e-12:
                raise ValueError("Zero diagonal element.")
            total = 0
            for j in range(n):
                if j != i:
                    total += A[i][j] * x[j]
            x_new[i] = (b[i] - total) / A[i][i]
        # calculate error
        error = max(abs(x_new[i] - x[i]) for i in range(n)) 
        data.append({"iteration": iteration, "x": x_new[:], "error": error}) 
        x = x_new
        if error < tolerance:
            return x, data
# test system
A = [
    [10, 1, 1],
    [2, 10, 1],
    [2, 2, 10]
]
b = [12, 13, 14]
solution, data = jacobi(A, b)
print("solution:")
for i, value in enumerate(solution):
    print(f"x{i + 1} = {value:.6f}")
print("\nNumber of iteration:", len(data))
print("\nIteration  |       x1  |      x2  |       x3  |     error")
print("-" * 70)
for row in data:
    print(f"{row['iteration']:>9}  | " f"{row['x'][0]:>10.6f}  | " f"{row['x'][1]:>10.6f}  | " f"{row['x'][2]:>10.6f}  | " 
            f"{row['error']:.8f}")
    