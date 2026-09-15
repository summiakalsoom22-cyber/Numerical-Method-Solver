def f(x):
    return x**3
def forward_difference(x, h):
    return(f(x + h) - f(x)) / h
x=2
exact = 3 * x**2
step_sizes = [0.1, 0.01, 0.001, 0.0001, 0.00001]
print("Forward Difference Error Analysis")
print()
print("      h | Numerical  Derivative  |       Error")
print("-" * 50)
for h in step_sizes:
    numerical=forward_difference(x, h)
error = abs(numerical - exact)
print( f"{h:8.5f}  | "  f"{numerical:20.10f}  | "  f"{error:.10f}")
