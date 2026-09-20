import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.linear_system import (
    gaussian_elimination,
    gauss_jordan,
    lu_decomposition,
    jacobi,
    gauss_seidel
)

A = [
    [2, 1, -1],
    [-3, -1, 2],
    [-2, 1, 2]
]

b = [8, -11, -3]

print("Linear System Method Comparison")
print("-" * 60)

# Gaussian Elimination
gaussian_solution = gaussian_elimination(A, b)

# Gauss-Jordan
gauss_jordan_solution = gauss_jordan(A, b)

# LU Decomposition
lu_solution = lu_decomposition(A, b)

# Jacobi
jacobi_solution = jacobi(A, b)

# Gauss-Seidel
seidel_solution = gauss_seidel(A, b)

print("Gaussian Elimination:", gaussian_solution)
print("Gauss-Jordan:        ", gauss_jordan_solution)
print("LU Decomposition:    ", lu_solution)
print("Jacobi:              ", jacobi_solution)
print("Gauss-Seidel:        ", seidel_solution)