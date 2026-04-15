# Polynomial Minimization using Gradient Descent

## Problem
Find the minimum of a 1-D polynomial using an iterative approach.

## Approach
I used gradient descent to iteratively find the minimum of the function.

Instead of computing the derivative analytically, I approximated it numerically using the central difference method:

f'(x) ≈ (f(x+h) - f(x-h)) / (2h)

## Key Ideas
- Move opposite to the slope (gradient descent)
- Repeat until convergence
- Use small learning rate for stability

## Observations
- Learning rate affects convergence speed
- Too large learning rate causes divergence
- Initial starting point can affect which minimum is reached

## How to Run
python main.py

## Extensions
- Could use second derivative (Newton’s method)
- Could extend to multi-dimensional optimization
- Could use adaptive learning rate
