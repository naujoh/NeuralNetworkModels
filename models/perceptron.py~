import random

bias = 0.0
weights = []
learning_rate = 0.0
epoch_quantity = 0

def setup(_input_quantity, _learning_rate, _epoch_quantity, _bias = 0.0):
    global weights
    global bias
    global learning_rate
    global epoch_quantity
    learning_rate = _learning_rate
    epoch_quantity = _epoch_quantity
    bias = _bias
    for i in range(_input_quantity):
        weights.append(random.uniform(0.0, 1.0))

def predict(input):
    global bias
    global weights
    activation = bias
    for i in range(len(weights)):
        activation += weights[i] * input[i]
    return 1.0 if activation >= 0.0 else 0.0

def train(dataset):
    global epoch_quantity
    global weights
    global learning_rate
    global bias
    for epoch in range(epoch_quantity):
        for row in dataset:
            prediction = predict(row)
            error = row[-1] - prediction
            bias += learning_rate * error
            for i in range(len(weights)):
                weights[i] = weights[i] + learning_rate * error * row[i]
