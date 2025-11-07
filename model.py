import numpy as np

class ActivationFunctions:
    pass

class Neuron:
    def __init__(self, bias=0, activation_function=None):
        self.bias = bias
        self.activation_function = None
        if activation_function is not None:
            self.activation_function = activation_function
        self.weights = np.array([1])

    def feedforward(self, z: float) -> float:
        output = np.sum(np.dot(self.weights, z)) + self.bias
        if self.activation_function is not None:
            output = self.activation_function(output)
        return output
    
    


if __name__ == '__main__':
    pass