def f(x):
    return x**3
def forward_difference(x, h):
    return (f(x + h) - f(x)) / h
def backward_difference(x, h):
    return (f(x) - f(x - h)) / h
def central_difference(x, h):
    return (f(x + h) - f(x - h)) /(2*h)
x = 2
exact = 3 * x**2
step_sizes=[0.1, 0.01, 0.001, 0.0001, 0.00001]
print("Numerical Differentiation Comparison")
print()
print(f"{'h':>10}   |  "
      f"{'Forward error':>15}   |  "
      f"{'Backward error':>15}   |  "
      f"{'Central error':>15}")
print("-" * 65)
for h in step_sizes:
    forward_error=abs(forward_difference(x, h) - exact)
    backward_error=abs(backward_difference(x, h) - exact)
    central_error=abs(central_difference(x, h) - exact)
    print(f"{h:10.5f}  |  "
          f"{forward_error:15.10f}   |  "
          f"{backward_error:15.10f}   |  "
          f"{central_error:15.10f}")