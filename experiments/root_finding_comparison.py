import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from src.root_finding import (
    bisection,
    newton_raphson,
    secant,
    regula_falsi
)

exact_root = 1.5213797068

# Bisection
bisection_root, bisection_data = bisection(1, 2)

# Newton-Raphson
newton_root, newton_data = newton_raphson(1.5)

# Secant
secant_root, secant_data = secant(1, 2)

# Regula Falsi
falsi_root, falsi_data = regula_falsi(1, 2)

print("Root-Finding Method Comparison")
print("-" * 65)
print(f"{'Method':<20}{'Root':<20}{'Error':<15}{'Iterations'}")
print("-" * 65)

print(f"{'Bisection':<20}{bisection_root:<20.10f}"
      f"{abs(bisection_root-exact_root):<15.10f}{len(bisection_data)}")

print(f"{'Newton-Raphson':<20}{newton_root:<20.10f}"
      f"{abs(newton_root-exact_root):<15.10f}{len(newton_data)}")

print(f"{'Secant':<20}{secant_root:<20.10f}"
      f"{abs(secant_root-exact_root):<15.10f}{len(secant_data)}")

print(f"{'Regula Falsi':<20}{falsi_root:<20.10f}"
      f"{abs(falsi_root-exact_root):<15.10f}{len(falsi_data)}")