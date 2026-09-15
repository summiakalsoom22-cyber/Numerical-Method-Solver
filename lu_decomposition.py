def lu_decomposition(A, b):
    n = len(A)
    # create L and U
    L = [[0.0] * n for _ in range(n)]
    U = [row[:] for row in A]  
    # Diagonal of L is 1
    for i in range(n):
        L[i][i] = 1.0
    # LU decomposition
    for k in range(n - 1):
        if abs(U[k][k]) < 1e-12:
            raise ValueError("Zero pivot encountered.")
        for i in range(k + 1, n):
            factor = U[i][k] / U[k][k]
            L[i][k] = factor
            for j in range(k, n):
                U[i][j] -= factor * U[k][j]
    # farward substitution: Ly = b
    y = [0.0] * n
    for i in range(n):
        total = 0
        for j in range(i):
            total += L[i][j] * y[j]
        y[i] = b[i] - total
    # backward substitution: Ux = y
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        total = 0
        for j in range(i + 1, n):
            total += U[i][j] * x[j]
        x[i] = (y[i] - total) / U[i][i]
    return L, U, x
# test system
A = [[2, 1, -1],
     [-3, -1, 2],
     [-2, 1, 2]]
b = [8, -11, -3]
L, U, solution = lu_decomposition(A, b)
print("L matrix:")
for row in L:
    print(row)
print("\nU matrix:")
for row in U:
    print(row)
print("\nSolution:")
for i, value in enumerate(solution):
    print(f"x{i + 1} = {value:.6f}")
