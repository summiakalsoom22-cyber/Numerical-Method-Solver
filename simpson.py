def f(x):
    return x**2
def simpson_one_third(a, b, n):
    if n % 2 !=0:
        raise ValueError("n must be even.")
    h=(b - a) / n
    total=f(a) + f(b)
    for i in range(1, n):
        x= a + i * h
        if i % 2==0:
            total +=2*f(x)
        else:
            total +=4*f(x)
    return (h / 3) * total
a=0
b=2
n=10
numerical=simpson_one_third(a, b, n)
exact=8/3
error=(numerical - exact)
print(f"Numerical integral: {numerical:.8f}")
print(f"Exact integral: {exact:.8f}")
print(f"Absolute error: {error:.8f}")