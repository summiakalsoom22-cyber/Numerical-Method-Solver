def divided_difference(x_values, y_values):
    n = len(x_values)
    table = [y_values[:]]
    for level in range(1, n):
        previous = table[level - 1]
        current = []
        for i in range(n - level):
            value = (previous[i + 1] - previous[i]) / (x_values[i + level] - x_values[i])
            current.append(value)
        table.append(current)
    return table
def newton_interpolation(x_values, y_values, x):
    table = divided_difference(x_values, y_values)
    result = table[0][0]
    product = 1.0
    for i in range(1, len(x_values)):
        product *= (x - x_values[i - 1])
        result += table[i][0] * product
    return result, table
# Data points
x_values = [0, 1, 2, 4]
y_values = [1, 3, 2, 5]
# Point where we want an estimate
x = 1.5
result, table = newton_interpolation(x_values, y_values, x)
print(f"interpolated value at x = {x}: {result:.6f}")
print("\nDivided Difference Table:")
for row in table:
    print([round(value, 6) for value in row])
