import numpy as np

class Layer:
    def __init__(self, input_size, output_size):
        self.weights = np.random.randn(output_size, input_size) * 0.01
        self.bias = np.zeros((output_size, 1))
        self.output = None
        self.grad_weights = None
        self.grad_bias = None

class Activation:
    def __init__(self, function, gradient):
        self.function = function
        self.gradient = gradient

    @staticmethod
    def relu(x):
        return np.maximum(0, x)

    @staticmethod
    def relu_gradient(x):
        return np.where(x > 0, 1, 0)

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def sigmoid_gradient(x):
        sig = Activation.sigmoid(x)
        return sig * (1 - sig)

class Loss:
    @staticmethod
    def mse(predictions, labels):
        return np.mean(np.square(predictions - labels))

    @staticmethod
    def mse_gradient(predictions, labels):
        return 2 * (predictions - labels) / labels.size

class Optimizer:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate
        self.layer_number = None

    def update_weights(self, layer, grad_weights):
        layer.weights -= self.learning_rate * grad_weights

    def update_bias(self, layer, grad_bias):
        layer.bias -= self.learning_rate * grad_bias

class NeuralNetwork:
    def __init__(self, layers, regularization_factor=0.01):
        self._layers = layers
        self._num_layers = len(layers)
        self._regularization_factor = regularization_factor
        self._optimizer = Optimizer(learning_rate=0.01)
        self._loss = Loss()
        self._num_examples = None
        self._input = None
        self._output = None

    def forward_step(self, inputs):
        self._input = inputs
        for layer, activation in self._layers:
            z = np.dot(layer.weights, inputs) + layer.bias
            layer.output = activation.function(z)
            inputs = layer.output
        self._output = inputs

    def backward_step(self, labels):
        da = self._loss.mse_gradient(self._output, labels)

        for index in reversed(range(self._num_layers)):
            layer, activation = self._layers[index]

            if index == 0:
                prev_layer_output = self._input
            else:
                prev_layer, prev_activation = self._layers[index - 1]
                prev_layer_output = prev_activation.function(prev_layer.output)

            dz = np.multiply(da, activation.gradient(layer.output))
            layer.grad_weights = np.dot(dz, prev_layer_output.T) / self._num_examples
            layer.grad_weights += (self._regularization_factor / self._num_examples) * layer.weights
            layer.grad_bias = np.mean(dz, axis=1, keepdims=True)
            da = np.dot(layer.grad_weights.T, dz)

            self._optimizer.update_weights(layer, layer.grad_weights)
            self._optimizer.update_bias(layer, layer.grad_bias)

    def train(self, inputs, labels, epochs):
        self._num_examples = inputs.shape[1]
        for epoch in range(epochs):
            self.forward_step(inputs)
            self.backward_step(labels)
            loss = self._loss.mse(self._output, labels)
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss}")

if __name__ == "__main__":
    np.random.seed(42)

    layers = [
        (Layer(2, 3), Activation(Activation.relu, Activation.relu_gradient)),
        (Layer(3, 1), Activation(Activation.sigmoid, Activation.sigmoid_gradient))
    ]
    nn = NeuralNetwork(layers)

    inputs = np.random.rand(2, 10)
    labels = np.random.rand(1, 10)

    nn.train(inputs, labels, epochs=10)
