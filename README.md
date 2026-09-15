# Numerical Methods Solver
A Python-based mathematical computing toolkit implementing numerical methods for root finding, linear systems, interpolation, differentiation, integration, and ordinary differential equations.
## About

This project is a collection of numerical methods implemented in Python.

The goal is to understand how numerical algorithms work mathematically and translate those algorithms into reusable Python functions.

The project also includes automated tests and numerical error/convergence experiments.
## Implemented Methods

### Root Finding
- Bisection Method
- Newton-Raphson Method
- Secant Method
- Regula Falsi Method

### Linear Systems
- Gaussian Elimination
- Gauss-Jordan Elimination
- LU Decomposition
- Jacobi Method
- Gauss-Seidel Method

### Interpolation
- Lagrange Interpolation
- Newton Divided Difference
- Newton Forward Interpolation
- Newton Backward Interpolation

### Numerical Differentiation
- Forward Difference
- Backward Difference
- Central Difference

### Numerical Integration
- Trapezoidal Rule
- Simpson's 1/3 Rule
- Simpson's 3/8 Rule

### Ordinary Differential Equations
- Euler Method
- Heun Method
- Runge-Kutta 4th Order (RK4)
## Technologies

- Python 3
- Git
- GitHub
- Pytest
## Project Structure

```text
Numerical-Methods-Solver/
├── README.md
├── .gitignore
├── src/
│   ├── root_finding.py
│   ├── linear_systems.py
│   ├── interpolation.py
│   ├── differentiation.py
│   ├── integration.py
│   └── ode.py
├── tests/
│   └── test_methods.py
├── test_modules.py
└── ...
## Installation

Clone the repository:

```bash
git clone https://github.com/summiakalsoom22-cybr/Numerical-Methods-Solver.git
cd Numerical-Methods-Solver

Install the testing package:

```bash
python -m pip install pytest
## Testing

The project uses Pytest for automated testing.

Run the test suite with:

```bash
python -m pytest
## Project Goals

This project was developed to strengthen my understanding of numerical methods, algorithm design, Python programming, and numerical error analysis.

Future improvements will include:

- Additional automated tests
- Convergence and error visualizations
- More robust input validation
- An interactive user interface