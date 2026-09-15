def f(x, y):
    return x + y
def euler(x0, y0, h, n):
    data=[]
    x=x0
    y=y0
    for integration in range(n + 1):
        data.append({ "integration": integration, "x": x, "y": y })
        y=y+h*f(x, y)
        x =x + h
    return data
x0=0
y0=1
h=0.1
n=10
data = euler(x0, y0, h, n)
print("Euler's Method")
print()
print(f"{'Integration':>10}   |  "
      f"{'x':>10}   |  "
      f"{'y':>12}")
print("-" * 40)
for row in data:
    print(f"{row['integration']:>10}    |  "
          f"{row['x']:>10.4f}    |  "
          f"{row['y']:>12.8f}")
                     