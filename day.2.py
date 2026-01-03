#non linear
import numpy as np
class DenseLayer:
  def __init__(self, n_inputs, n_neurons):
    self.weights = 0.1 * np.random.randn(n_inputs, n_neurons)
    self.biases = np.zeros((1, n_neurons))
  def forward(self, inputs):
    self.output = np.dot(inputs, self.weights) + self.biases
    return self.output
  def reLU(self, inputs):
    return np.maximum(0, inputs)
layer1 = DenseLayer(3, 6)
layer2 = DenseLayer(6, 6)
x = np.array([[2, 3, 4]])

out1 = layer1.forward(x)
activation1 = layer1.reLU(out1)
finaloutput = layer2.forward(activation1)

print("Final Output:", finaloutput)