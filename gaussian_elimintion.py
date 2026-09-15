def gaussian_eliminaion(A, b):
    n = len(b)
    # Forward elimination with partial pivoting
    for k in range(n - 1):
        # find the row with the largest pivot
        pivot_row = max(range(k, n), key=lambda i: abs(A[i][k]))
        # swap rows
        A[k], A[pivot_row] = A[pivot_row], A[k]
        b[k], b[pivot_row] = b[pivot_row], b[k]
        if abs(A[k][k]) < 1e-12:
            raise ValueError("Matrix is singular or nearly singular")
        # eliminate entries below the pivot
        for i in range(k + 1, n):
            factor = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] = A[i][j] - factor * A[k][j]
            b[i] = b[i] - factor * b[k]
            # Back substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        total = 0
        for j in range(i + 1, n):
            total += A[i][j] * x[j]
        if abs(A[i][i]) < 1e-12:
                raise ValueError("Matrix is singular or nearly singular")
        x[i] = (b[i] - total) / A[i][i]
    return x
# test system
A = [[2, 1, -1], [-3, -1, 2], [-2, 1, 2]]
b = [8, -11, -3]
solution = gaussian_eliminaion(A, b)
print("Solution:")
for i, value in enumerate(solution):
    print(f"x{i + 1} = {value:.6f}")