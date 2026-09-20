Numerical Methods Solver

A Python-based numerical computing toolkit implementing fundamental numerical methods for root finding, linear systems, interpolation, differentiation, integration, and ordinary differential equations (ODEs).

The project focuses on understanding the mathematical algorithms behind numerical methods and translating them into reusable Python implementations.

It also includes automated testing, numerical experiments, error analysis, and convergence analysis.

Implemented Methods

Root Finding

- Bisection Method
- Newton-Raphson Method
- Secant Method
- Regula Falsi Method

Linear Systems

- Gaussian Elimination
- Gauss-Jordan Elimination
- LU Decomposition
- Jacobi Method
- Gauss-Seidel Method

Interpolation

- Lagrange Interpolation
- Newton Divided Difference
- Newton Forward Interpolation
- Newton Backward Interpolation

Numerical Differentiation

- Forward Difference
- Backward Difference
- Central Difference

Numerical Integration

- Trapezoidal Rule
- Simpson's 1/3 Rule
- Simpson's 3/8 Rule

Ordinary Differential Equations

- Euler Method
- Heun Method
- Runge-Kutta 4th Order (RK4)

Error and Convergence Analysis

The project includes experiments comparing numerical methods and studying numerical error.

Examples include:

- Euler method error analysis
- Error versus step-size analysis
- Observed order of convergence
- Root-finding method comparison
- Interpolation method comparison
- Numerical integration comparison
- Numerical differentiation comparison
- Linear system method comparison

Technologies

- Python 3
- Pytest
- Git
- GitHub
- Matplotlib
- Jupyter Notebook

Project Structure

Numerical Method Solver/
│
├── src/
│   ├── differentiation.py
│   ├── integration.py
│   ├── interpolation.py
│   ├── linear_system.py
│   ├── ode.py
│   └── root_finding.py
│
├── tests/
│   └── test_methods.py
│
├── experiments/
│   ├── differentiation_comparison.py
│   ├── differentiation_error_plot.py
│   ├── euler_convergence.py
│   ├── euler_error_analysis.py
│   ├── euler_error_plot.py
│   ├── integration_comparison.py
│   ├── interpolation_comparison.py
│   ├── linear_system_comparison.py
│   ├── ode_comparison.py
│   └── root_finding_comparison.py
│
├── notebooks/
│   └── convergence_analysis.ipynb
│
├── README.md
├── requirements.txt
└── .gitignore

Installation

Clone the repository:

git clone https://github.com/summiakalsoom22-cyber/Numerical-Method-Solver.git
cd Numerical-Method-Solver

Install the required packages:

python -m pip install -r requirements.txt

Running the Tests

The project uses Pytest for automated testing.

Run:

python -m pytest

Current test status:

24 passed

Running an Experiment

For example, to run the root-finding comparison:

python experiments/root_finding_comparison.py

To run the Euler error analysis:

python experiments/euler_error_analysis.py

To view the differentiation error plot:

python experiments/differentiation_error_plot.py

Project Goals

This project was developed to strengthen my understanding of:

- Numerical analysis
- Mathematical algorithms
- Python programming
- Algorithm implementation
- Numerical error
- Convergence analysis
- Automated testing
- Scientific computing

The project is also intended as a portfolio project demonstrating the practical application of mathematical concepts through programming.

Future Improvements

Possible future improvements include:

- Additional automated tests
- More numerical methods
- More error and convergence experiments
- Improved input validation
- Interactive visualizations
- An interactive user interface
- Performance comparisons for larger systems

Author

Summia Kalsoom

BS Mathematics Student

GitHub: "summiakalsoom22-cyber"