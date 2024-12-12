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
    def softmax(x):
        exp_x = np.exp(x - np.max(x, axis=0, keepdims=True))
        return exp_x / np.sum(exp_x, axis=0, keepdims=True)

    @staticmethod
    def softmax_gradient(output, labels):
        return output - labels

class Loss:
    @staticmethod
    def cross_entropy(predictions, labels):
        n_samples = labels.shape[1]
        log_likelihood = -np.log(predictions[labels.argmax(axis=0), range(n_samples)])
        return np.sum(log_likelihood) / n_samples

class Optimizer:
    def __init__(self, learning_rate):
        self.learning_rate = learning_rate

    def update_weights(self, layer, grad_weights):
        layer.weights -= self.learning_rate * grad_weights

    def update_bias(self, layer, grad_bias):
        layer.bias -= self.learning_rate * grad_bias

class NeuralNetwork:
    def __init__(self, layers):
        self._layers = layers
        self._optimizer = Optimizer(learning_rate=0.01)
        self._loss = Loss()
        self._output = None

    def forward_step(self, inputs):
        for layer, activation in self._layers:
            z = np.dot(layer.weights, inputs) + layer.bias
            layer.output = activation.function(z)
            inputs = layer.output
        self._output = inputs

    def backward_step(self, inputs, labels):
        da = Activation.softmax_gradient(self._output, labels)

        for index in reversed(range(len(self._layers))):
            layer, activation = self._layers[index]

            if index == 0:
                prev_layer_output = inputs
            else:
                prev_layer, _ = self._layers[index - 1]
                prev_layer_output = prev_layer.output

            dz = da
            layer.grad_weights = np.dot(dz, prev_layer_output.T) / inputs.shape[1]
            layer.grad_bias = np.mean(dz, axis=1, keepdims=True)
            da = np.dot(layer.weights.T, dz)

            self._optimizer.update_weights(layer, layer.grad_weights)
            self._optimizer.update_bias(layer, layer.grad_bias)

    def train(self, inputs, labels, epochs):
        for epoch in range(epochs):
            self.forward_step(inputs)
            loss = self._loss.cross_entropy(self._output, labels)
            self.backward_step(inputs, labels)
            print(f"Epoch {epoch + 1}/{epochs}, Loss: {loss}")

if __name__ == "__main__":
    np.random.seed(42)

    layers = [
        (Layer(2, 3), Activation(np.tanh, lambda x: 1 - np.tanh(x)**2)),
        (Layer(3, 2), Activation(Activation.softmax, None))
    ]
    nn = NeuralNetwork(layers)

    # Random data: 2 input features, 10 samples, 2 output classes
    inputs = np.random.rand(2, 10)
    labels = np.zeros((2, 10))
    for i in range(10):
        labels[np.random.randint(0, 2), i] = 1

    nn.train(inputs, labels, epochs=10)
