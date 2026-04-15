# Polynomial Minimization using Gradient Descent

## Overview
This project implements an iterative approach to find the minimum of a 1-D polynomial function using gradient descent.

## Approach
- Used gradient descent to iteratively reach the minimum
- Approximated derivative numerically using central difference:
  (f(x+h) - f(x-h)) / (2h)
- Added convergence-based stopping condition

## Key Observations
- Learning rate affects convergence speed and stability
- Different initial values may lead to different minima
- Numerical approximation works well for general functions

## Features
- Works for any function
- Adjustable parameters (learning rate, tolerance)
- Convergence tracking

## How to Run
python main.py

## Repository Structure
- main.py → implementation
- notebook.ipynb → experimentation (optional)
