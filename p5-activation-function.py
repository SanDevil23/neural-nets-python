import numpy as np
import spiralData as spiral
# import nnfs                 # neural network from scratch

X = [[1,2,3,2.5],
    [2.0,5.0,-1.0,2.0],
    [-1.5,2.7,3.3,-0.8]]

X,y = spiral.create_data(100,3)


# inputs = [0,2,-1,3.3, -2.7, 1.1, 2.2, -100]

# output = []


# # RELU functionality
# for i in inputs:
#     if (i>0):
#         output.append(i)
#     elif (i<=0):
#         output.append(0)


# print(output)
class Layer_Dense:
    def __init__(self, n_inputs, n_neurons):
        self.weights = 0.10 * np.random.randn(n_inputs, n_neurons)
        self.biases = np.zeros((1, n_neurons))


    def forward(self, inputs):
        self.output  = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)                     # implementing ReLU


layer1 = Layer_Dense(2,5)
# layer2 = Layer_Dense(5,2)

activ_ReLU = Activation_ReLU()


print("Before Activation Function")
layer1.forward(X)
print(layer1.output)


print("After Activation Function")
activ_ReLU.forward(layer1.output)
print(activ_ReLU.output)



# layer2.forward(layer1.output)
# print(layer2.output)