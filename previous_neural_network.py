import numpy as np

# Sigmoid activation function and its derivative
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)  # Derivative of sigmoid assuming x has already been activated

# Network parameters (initial weights, biases, and learning rate)
inputs = np.array([0.05, 0.10])
target_outputs = np.array([0.01, 0.99])
learning_rate = 0.5

# Initial weights
weights_input_hidden = np.array([[0.15, 0.20], [0.25, 0.30]])  # weights w1, w2, w3, w4
weights_hidden_output = np.array([[0.40, 0.45], [0.50, 0.55]])  # weights w5, w6, w7, w8

# Biases
bias_hidden = 0.35
bias_output = 0.60

# Forward propagation
# Step 1: Calculate hidden layer activations
hidden_input = np.dot(inputs, weights_input_hidden) + bias_hidden
hidden_output = sigmoid(hidden_input)

# Step 2: Calculate output layer activations
final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
final_output = sigmoid(final_input)

# Calculate error (Mean Squared Error)
error = 0.5 * (target_outputs - final_output) ** 2
total_error = np.sum(error)

print("Initial Total Error:", total_error)

# Backpropagation
# Output layer error and gradient
output_errors = target_outputs - final_output
output_delta = output_errors * sigmoid_derivative(final_output)

# Hidden layer error and gradient
hidden_errors = output_delta.dot(weights_hidden_output.T)
hidden_delta = hidden_errors * sigmoid_derivative(hidden_output)

# Update weights and biases
weights_hidden_output += learning_rate * np.outer(hidden_output, output_delta)
weights_input_hidden += learning_rate * np.outer(inputs, hidden_delta)

# Bias updates
bias_output += learning_rate * output_delta
bias_hidden += learning_rate * hidden_delta

# Forward pass after weight updates to see improved output
hidden_input = np.dot(inputs, weights_input_hidden) + bias_hidden
hidden_output = sigmoid(hidden_input)
final_input = np.dot(hidden_output, weights_hidden_output) + bias_output
final_output = sigmoid(final_input)

# Calculate new error
new_error = 0.5 * (target_outputs - final_output) ** 2
new_total_error = np.sum(new_error)

print("Updated Total Error:", new_total_error)
print("Updated Weights from Input to Hidden:", weights_input_hidden)
print("Updated Weights from Hidden to Output:", weights_hidden_output)
print("Updated Biases:", bias_hidden, bias_output)
