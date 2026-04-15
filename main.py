import matplotlib.pyplot as plt

def f(x):
    return x**4 - 3*x**3 + 2

def derivative(f, x, h=1e-5):
    return (f(x + h) - f(x - h)) / (2 * h)

def gradient_descent(f, x0, lr=0.01, max_iter=1000, tol=1e-6):
    x = x0
    history = []

    for i in range(max_iter):
        history.append(x)

        grad = derivative(f, x)
        new_x = x - lr * grad

        if abs(new_x - x) < tol:
            break

        x = new_x

    return x, history

# Run
x_min, history = gradient_descent(f, x0=0.5)

print("Minimum x:", x_min)
print("Minimum value:", f(x_min))

# Try different starting points
for start in [-1, 0, 1, 2]:
    x, _ = gradient_descent(f, start)
    print(f"Start {start} → Min at {x}")

# Plot convergence
plt.plot(history)
plt.title("Convergence of x")
plt.xlabel("Iterations")
plt.ylabel("x value")
plt.show()
