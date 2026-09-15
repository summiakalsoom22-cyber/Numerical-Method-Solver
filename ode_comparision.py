import math
def f(x, y):
    return x + y
def exact_solution(x):
    return 2 * math.exp(x) - x - 1
def euler(x0, y0, h, n):
    x= x0
    y= y0
    for _ in range(n):
        y=y+h*f(x, y)
        x=x+h
    return y
def heun(x0, y0, h, n):
    x=x0
    y=y0
    for _ in range(n):
        slope1=f(x, y)
        y_predict=y + h * slope1
        x_new=x+h
        slope2=f(x_new, y_predict)
        y = y + (h / 2) * (slope1 + slope2)
        x = x_new
    return y
def rk4(x0, y0, h, n):
    x=x0
    y=y0
    for _ in range(n):
        k1=f(x, y)
        k2=f(x+h/2,y+h*k1/2)
        k3=f(x+h/2,y+h*k2/2)
        k4=f(x+h,y+h*k3)
        y=y+(h/6)*(k1+2*k2+2*k3+k4)
        x=x+h
    return y
x0=0
y0=1
x_final=1
exact=exact_solution(x_final)
step_sizes=[0.1, 0.05, 0.025, 0.0125]
print("ODE Accuracy Comparision")
print()
print(f"Exact solution at x = 1: {exact:.10f}")
print()
print(f"{'h':>10}   |  "
      f"{'Euler Error':>15}    |  "
      f"{'Heun Error':>15}    |   "
      f"{'RK4 Error':>15}")
print("-" * 65)
for h in step_sizes:
    n=round((x_final - x0) / h)
    euler_error=abs(euler(x0, y0, h, n) - exact)
    heun_error=abs(heun(x0, y0, h, n) - exact)
    rk4_error=abs(rk4(x0, y0, h, n) - exact)
    print(f"{h:10.4f}   |  "
          f"{euler_error:15.10e}   |  "
          f"{heun_error:15.10e}   |  "
          f"{rk4_error:15.10e}")