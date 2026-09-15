import math
def farword_difference_table(y_values):
    table=[y_values[:]]
    while len(table[-1])>1:
        previous=table[-1]
        current=[]
        for i in range(len(previous) -1):
            current.append(previous[i + 1] - previous[i])
        table.append(current)
    return table
def newton_farword(x_values, y_values, x):
    table=farword_difference_table(y_values)
    h = x_values[1] - x_values[0]
    u = (x - x_values[0]) / h
    result = y_values[0]
    product = 1.0
    for order in range(1, len(y_values)):
        product *= (u - (order - 1))
        result += (product * table[order][0] / math.factorial(order))
    return result, table
# equally spaced data
x_values = [0, 1, 2, 3]
y_values = [1, 3, 2, 5]
x = 0.5
result, table = newton_farword(x_values, y_values, x)
print(f"interpolated value at x = {x}: {result:.6f}")
print("\nfarword difference table:")
for row in table:
    print([round(value, 6) for value in row])