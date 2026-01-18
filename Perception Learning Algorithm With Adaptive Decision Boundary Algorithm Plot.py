import numpy as np
import matplotlib.pyplot as plt

def perceptron_learning(X, d, learning_rate=1, epochs=10):

    n_samples, n_features = X.shape

    w = np.zeros(n_features + 1)

    X_bias = np.c_[np.ones((n_samples, 1)), X]

    print("Initial Weights:", w)

    for epoch in range(epochs):
        print(f"\nEpoch {epoch + 1}")
        error_count = 0

        for i in range(n_samples):
            y = np.dot(w, X_bias[i])
            output = 1 if y >= 0 else -1

            # Check if prediction is wrong
            if output != d[i]:
                error_count += 1
                w = w + learning_rate * d[i] * X_bias[i]
                print(f"Updated weights (sample {i + 1}): {w}")

        print(f"Errors in epoch {epoch + 1}: {error_count}")
        if error_count == 0:
            print("Converged.")
            break

    print("\nFinal Weights:", w)
    return w


def plot_decision_boundary(X, d, w):
    plt.figure(figsize=(7, 5))

    # Plot class points
    for i in range(len(d)):
        if d[i] == 1:
            plt.scatter(X[i, 0], X[i, 1], color='blue', marker='o', label='Class 1' if i == 0 else "")
        else:
            plt.scatter(X[i, 0], X[i, 1], color='red', marker='x', label='Class -1' if i == 0 else "")

    # Decision boundary line: w0 + w1*x + w2*y = 0 → y = (-w0 - w1*x)/w2
    x_values = np.linspace(np.min(X[:, 0]) - 1, np.max(X[:, 0]) + 1, 100)
    y_values = (-w[0] - w[1] * x_values) / w[2]
    plt.plot(x_values, y_values, color='green', label='Decision Boundary')

    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.legend()
    plt.title('Adaptive Decision Boundary (Perceptron Learning)')
    plt.grid(True)
    plt.show()


# Input samples (X1, X2)
X = np.array([
    [2, 3],
    [4, 2],
    [3, 6],
    [1, 4]
])

# Target labels (+1 or -1)
d = np.array([1, 1, -1, -1])

# Train perceptron
weights = perceptron_learning(X, d, learning_rate=1, epochs=10)

# Plot decision boundary
plot_decision_boundary(X, d, weights)