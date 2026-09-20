def gaussian_elimination(A, b):

    n = len(b)

    for k in range(n - 1):

        pivot_row = max(
            range(k, n),
            key=lambda i: abs(A[i][k])
        )

        A[k], A[pivot_row] = A[pivot_row], A[k]
        b[k], b[pivot_row] = b[pivot_row], b[k]

        if abs(A[k][k]) < 1e-12:
            raise ValueError(
                "Matrix is singular or nearly singular."
            )

        for i in range(k + 1, n):

            factor = A[i][k] / A[k][k]

            for j in range(k, n):
                A[i][j] -= factor * A[k][j]

            b[i] -= factor * b[k]

    x = [0.0] * n

    for i in range(n - 1, -1, -1):

        total = 0

        for j in range(i + 1, n):
            total += A[i][j] * x[j]

        if abs(A[i][i]) < 1e-12:
            raise ValueError(
                "Matrix is singular or nearly singular."
            )

        x[i] = (b[i] - total) / A[i][i]

    return x


def gauss_jordan(A, b):

    n = len(b)

    augmented = [
        A[i][:] + [b[i]]
        for i in range(n)
    ]

    for k in range(n):

        pivot_row = max(
            range(k, n),
            key=lambda i: abs(augmented[i][k])
        )

        augmented[k], augmented[pivot_row] = (
            augmented[pivot_row],
            augmented[k]
        )

        pivot = augmented[k][k]

        if abs(pivot) < 1e-12:
            raise ValueError(
                "Matrix is singular or nearly singular."
            )

        for j in range(k, n + 1):
            augmented[k][j] /= pivot

        for i in range(n):

            if i != k:

                factor = augmented[i][k]

                for j in range(k, n + 1):
                    augmented[i][j] -= factor * augmented[k][j]

    return [
        augmented[i][n]
        for i in range(n)
    ]


def lu_decomposition(A, b):

    n = len(A)

    L = [[0.0] * n for _ in range(n)]
    U = [row[:] for row in A]

    for i in range(n):
        L[i][i] = 1.0

    for k in range(n - 1):

        if abs(U[k][k]) < 1e-12:
            raise ValueError("Zero pivot encountered.")

        for i in range(k + 1, n):

            factor = U[i][k] / U[k][k]
            L[i][k] = factor

            for j in range(k, n):
                U[i][j] -= factor * U[k][j]

    y = [0.0] * n

    for i in range(n):

        total = 0

        for j in range(i):
            total += L[i][j] * y[j]

        y[i] = b[i] - total

    x = [0.0] * n

    for i in range(n - 1, -1, -1):

        total = 0

        for j in range(i + 1, n):
            total += U[i][j] * x[j]

        x[i] = (y[i] - total) / U[i][i]

    return  x


def jacobi(A, b, tolerance=1e-6, max_iterations=100):

    n = len(b)
    x = [0.0] * n
    data = []

    for iteration in range(1, max_iterations + 1):

        x_new = [0.0] * n

        for i in range(n):

            if abs(A[i][i]) < 1e-12:
                raise ValueError("Zero diagonal element.")

            total = 0

            for j in range(n):

                if j != i:
                    total += A[i][j] * x[j]

            x_new[i] = (b[i] - total) / A[i][i]

        error = max(
            abs(x_new[i] - x[i])
            for i in range(n)
        )

        data.append({
            "iteration": iteration,
            "x": x_new[:],
            "error": error
        })

        x = x_new

        if error < tolerance:
            return x

    return x


def gauss_seidel(A, b, tolerance=1e-6, max_iterations=100):

    n = len(b)
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

            x[i] = (b[i] - total) / A[i][i]

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
            return x

    return x