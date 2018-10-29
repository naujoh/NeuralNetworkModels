import random
from functools import reduce

# Generates j initial weights with n values between 0-1
def initialize(j, n):
    return [[random.uniform(0.0, 1.0) for _ in range(j)] for _ in range(n)]

# Calculates the euclidean distance between two vectors
def euclideanDistance(x, w):
    return reduce((lambda i, acc: i + acc), [(xi - wi)**2 for xi, wi in zip(x, w)])**(1/2)
