import numpy as np

# AND gate dataset
X = np.array([[0,0],[0,1],[1,0],[1,1]])
y = np.array([0,0,0,1])

# Initialize weights and bias
w = np.zeros(2)
b = 0
lr = 0.1
epochs = 10

# Activation function
def step(z):
    return 1 if z >= 0 else 0

# Training
for _ in range(epochs):
    for i in range(len(X)):
        z = np.dot(X[i], w) + b
        y_pred = step(z)
        error = y[i] - y_pred
        w += lr * error * X[i]
        b += lr * error

print("Weights:", w)
print("Bias:", b)

# Testing
for i in range(len(X)):
    print(X[i], "->", step(np.dot(X[i], w) + b))
