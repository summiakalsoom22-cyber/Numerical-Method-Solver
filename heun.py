def f(x, y):
    return x + y
def heun(x0, y0, h, n):
    data=[]
    x=x0
    y=y0
    for integration in range(n + 1):
        data.append({ "integration": integration, "x": x, "y": y })
        slope1=f(x, y)
        y_predict=y+h*slope1
        x_new =x + h
        slope2 = f(x_new, y_predict)
        y = y + (h / 2) * (slope1 + slope2)
        x=x_new
    return data
x0=0
y0=1
h=0.1
n=10
data = heun(x0, y0, h, n)
print("Heun's Method")
print()
print(f"{'Integration':>10}   |  "
      f"{'x':>10}   |  "
      f"{'y':>12}")
print("-" * 40)
for row in data:
    print(f"{row['integration']:>10}    |  "
          f"{row['x']:>10.4f}    |  "
          f"{row['y']:>12.8f}")
                     