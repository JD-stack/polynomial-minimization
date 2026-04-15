# Polynomial Minimization using Gradient Descent

## Problem
Find the minimum of a 1-D polynomial using an iterative approach.

## Approach
I used gradient descent to iteratively move towards the minimum.

Instead of computing the derivative analytically, I approximated it numerically using:

f'(x) ≈ (f(x+h) - f(x-h)) / (2h)

## Key Ideas
- Move in opposite direction of slope
- Repeat until convergence
- Use small learning rate for stability

## Observations
- Learning rate affects convergence speed
- Very large learning rate causes divergence
- Initial starting point can affect the result

## How to Run
python main.py
