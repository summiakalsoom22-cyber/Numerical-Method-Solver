def f(x):
    return x**2
def simpson_three_eight(a, b, n):
    if n % 3 !=0:
        raise ValueError("n must be divisible by 3.")
    h=(b - a) / n
    total=f(a) + f(b)
    for  i in range(1, n):
        x=a + i *h
        if i % 3==0:
            total +=2*f(x)
        else:
            total +=3*f(x)
    return (3*h/8)*total
a=0
b=2
n=12
numerical=simpson_three_eight(a, b, n)
exact=8/3
error=abs(numerical - exact)
print(f"Numerical integral: {numerical:.8f}")
print(f"Exact integral: {exact:.8f}")
print(f"Absolute error: {error:.8f}")