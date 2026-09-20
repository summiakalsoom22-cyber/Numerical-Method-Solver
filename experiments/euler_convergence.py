import math

errors = {
    0.1: 0.2490787367,
    0.05: 0.1299682466,
    0.01: 0.0269359981
}

step_sizes = list(errors.keys())

print("Euler Method: Observed Order of Convergence")
print("-" * 50)

for i in range(len(step_sizes) - 1):
    h1 = step_sizes[i]
    h2 = step_sizes[i + 1]

    E1 = errors[h1]
    E2 = errors[h2]

    p = math.log(E1 / E2) / math.log(h1 / h2)

    print(f"h = {h1} to h = {h2}:  p = {p:.4f}")