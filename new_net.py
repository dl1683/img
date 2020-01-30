import numpy as np
import math

"""X=np.array(([0,0,1],[0,1,1],[1,0,1],[1,1,1]), dtype=float)#samples
y=np.array(([0],[1],[1],[0]), dtype=float) #samples

NN=NeuralNetwork(X,y)
"""
#We use sigmoid instead of ReLu because it's closer to exponential functions
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def softmax(X):
    expo = np.exp(X)
    expo_sum = np.sum(np.exp(X))
    return expo/expo_sum

#We need this because 3 layer things (as with pixels) are often nonlinear. We could also use a 
#Taylor series approximation to fine tune weights but that adds a layer of complexity with a large cost
#for incremental benefits.
def sigmoid_derivative(x):
    #dy/dx = f(x)' = f(x) * (1 - f(x))
    sig=sigmoid(x)
    return sig* (1-sig)

# Class definition
class NeuralNetwork:
    def __init__(self, x,y):
        self.input = x
        self.weights1= np.random.rand(self.input.shape[1],4) # considering we have 4 nodes in the hidden layer
        self.weights2 = np.random.rand(4,1)
        self.y = y
        self.output = np. zeros(y.shape)
        
    def feedforward(self):
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))
        self.layer2 = sigmoid(np.dot(self.layer1, self.weights2))
        return self.layer2
        
    def backprop(self):
        d_weights2 = np.dot(self.layer1.T, 2*(self.y -self.output)*sigmoid_derivative(self.output))
        d_weights1 = np.dot(self.input.T, np.dot(2*(self.y -self.output)*sigmoid_derivative(self.output), self.weights2.T)*sigmoid_derivative(self.layer1))

        #simple weight adjustment
        self.weights1 += d_weights1
        self.weights2 += d_weights2

    def train(self, X, y):
        self.output = self.feedforward()
        self.backprop()
        
    def info(self):
        return [self.x,self.weights1,self.weights2,self.output]

def trainData(pixel,gray):
    NN.train(pixel, gray)

def create(pixel, gray):
    NN = NeuralNetwork(X,y)

"""
for i in range(1500): # trains the NN 1,000 times
    if i % 100 ==0: 
        print ("for iteration # " + str(i) + "\n")
        print ("Input : \n" + str(X))
        print ("Actual Output: \n" + str(y))
        print ("Predicted Output: \n" + str(NN.feedforward()))
        print ("Loss: \n" + str(np.mean(np.square(y - NN.feedforward())))) # mean sum squared loss
        print ("\n")
NN.train(X,y)  
"""
