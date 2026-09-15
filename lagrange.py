def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result
# Data points
x_data = [0, 1, 2, 3]
y_data = [1, 3, 2, 5]
#point where we want an estimate
x = 1.5
result = lagrange_interpolation(x_data, y_data, x)
print(f"The estimated value at x = {x}: {result:.6f}")