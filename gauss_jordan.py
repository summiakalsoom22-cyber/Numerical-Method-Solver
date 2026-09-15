def gauss_jordan(A, b):
    n=len(A)
    # create augment matrix

    augmented = [A[i][:] + [b[i]] for i in range(n)]
    for k in range(n):
        # Partial pivoting
        pivot_row = max(range(k, n), key=lambda i: abs(augmented[i][k]))
        augmented[k], augmented[pivot_row] = (augmented[pivot_row], augmented[k])
        pivot = augmented[k][k]
        if abs(pivot) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular.")

        # Make pivot element equal to 1
        for j in range(k, n + 1):
            augmented[k][j] /= pivot

        # eliminare above and below pivot
        for i in range(n):
            if i != k:
                factor = augmented[i][k]
                for j in range(k, n + 1):
                    augmented[i][j] -= factor * augmented[k][j]
    # Extract solution
    solution = [augmented[i][n] for i in range(n)]
    return solution
# test system
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]
solution = gauss_jordan(A, b)
print("Solution:")
for i, value in enumerate(solution):
    print(f"x{i + 1} = {value:.6f}")
    