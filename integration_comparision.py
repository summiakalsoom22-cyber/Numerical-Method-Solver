def f(x):
    return x**2
def trapezodial(a, b, n):
    h=(b - a)/n
    total=(f(a) + f(b)) / 2
    for i in range(1, n):
        total += f(a + i * h)
    return h*total
def simpson_one_third(a, b, n):
    if n % 2 != 0:
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
def simpson_three_eight(a, b, n):
    if n % 3 != 0:
        raise ValueError("n must be divisible by 3.")
    h = (b - a) / n
    total = f(a) + f(b)
    for i in range(1, n):
        x= a + i * h
        if i % 3 ==0:
            total += 2*f(x)
        else:
            total +=3*f(x)
    return (3 * h / 8) * total
a=0
b=2
exact=8/3
n_values=[6, 12, 24, 48, 96]
print("Integration Accuracy Comparision")
print()
print(f"{'n':>5}   |  "
      f"{'Trapezodial':>15}    |  "
      f"{'Simpson 1/3':>15}    |  "
      f"{'Simpson 3/8':>15}")
print("-" * 60)
for n in n_values:
    trap_error=abs(trapezodial(a, b, n) - exact)
    simpson_one_error=abs(simpson_one_third(a, b, n) - exact)
    simpson_three_error=abs(simpson_three_eight(a, b, n) - exact)
    print(f"{n:5d}   |  "
          f"{trap_error:15.10f}   |  "
          f"{simpson_one_error:15.10f}   |  "
          f"{simpson_three_error:15.10f}")