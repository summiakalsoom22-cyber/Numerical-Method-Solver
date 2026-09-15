def f(x):
    return x**2
def trapezodial(a, b, n):
    h =(b - a) / n
    total=(f(a) + f(b)) / 2
    for i in range(1, n):
        x=a + i * h
        total += f(x)
    return h *total
a=0
b=2
n=10
numerical=trapezodial(a, b, n)
#exact integral
exact=8/3
error=abs(numerical - exact)
print(f"Numerical integral: {numerical:.8f}")
print(f"Exact integal: {exact:.8f}")
print(f"Absolute error: {error:.8f}")