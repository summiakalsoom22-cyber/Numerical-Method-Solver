def f(x):
    return x**3
def central_difference(x, h):
    return (f(x + h) - f(x - h) / 2*h)
x=2
h=0.01
numerical=central_difference(x, h)
exact= 3 * x**2
error = abs(numerical - exact)
print(f"Numerical derivative: {numerical:.8f}")
print(f"Exact derivative: {exact:.8f}")
print(f"Asolute error: {error:.8f}")