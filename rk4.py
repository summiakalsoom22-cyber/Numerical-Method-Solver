def f(x, y):
    return x + y
def rk4(x0, y0, h, n):
    data=[]
    x=x0
    y=y0
    for integration in range(n + 1):
        data.append({ "integration": integration, "x": x, "y": y })
        k1 = f(x, y)
        k2 = f(x + h / 2, y + (h / 2) *k1)
        k3 = f(x + h / 2, y + (h / 2)*k2)
        k4 = f(x + h, y + h * k3)
        y = y + (h / 6) * (k1 + 2 * k2 + 2 * k3 + k4)
        x = x + h
    return data
x0=0
y0=1
h=0.1
n=10
data = rk4(x0, y0, h, n)
print("Runge_Kutta 4th Order Method")
print()
print(f"{'Integration':>10}   |  "
      f"{'x':>10}   |  "
      f"{'y':>12}")
print("-" * 40)
for row in data:
    print(f"{row['integration']:>10}    |  "
          f"{row['x']:>10.4f}    |  "
          f"{row['y']:>12.8f}")
                     