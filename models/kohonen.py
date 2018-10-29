import random
<<<<<<< HEAD
learning_rate = 0.1
=======
from functools import reduce

>>>>>>> 4076235b2e3a3a462d81fda4dd66dd34e85e36f2
# Generates j initial weights with n values between 0-1
def initialize(j, n):
    return [[random.uniform(0.0, 1.0) for _ in range(j)] for _ in range(n)]

<<<<<<< HEAD
def learning(weights, input):
    return list(map(lambda x,y: list(map(lambda w, dw: w+dw, x,y)), weights, cal_delta_w(weights, input)))

def cal_delta_w(weights, input):
    global learning_rate
    return [list(map(lambda x, w: learning_rate*(x-w), input, w)) for w in weights]
=======
# Calculates the euclidean distance between two vectors
def euclideanDistance(x, w):
    return reduce((lambda i, acc: i + acc), [(xi - wi)**2 for xi, wi in zip(x, w)])**(1/2)
>>>>>>> 4076235b2e3a3a462d81fda4dd66dd34e85e36f2
