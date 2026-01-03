import numpy as np

class DenseLayer:
    def __init__(self, n_inputs, n_neurons):
        # 0.1 * randn is a common trick to keep weights small for stability
        self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
        self.bias = np.zeros((1, n_neurons))

    def forward(self, inputs):
        # We perform the Dot Product
        self.output = np.dot(inputs, self.weights) + self.bias
        # CRITICAL: Pass the baton to the next runner
        return self.output 

# --- Usage ---
layer1 = DenseLayer(2, 3) # 2 Inputs -> 3 Neurons
X = np.array([[1, 2]])    # A batch of data

output = layer1.forward(X)
print("Output Shape:", output.shape) # Should be (1, 3)
print("Output Values:\n", output)
