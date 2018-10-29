import random
learning_rate = 0.1
# Generates j initial weights with n values between 0-1
def initialize(j, n):
    return [[random.uniform(0.0, 1.0) for _ in range(j)] for _ in range(n)]

def learning(weights, input):
    return list(map(lambda x,y: list(map(lambda w, dw: w+dw, x,y)), weights, cal_delta_w(weights, input)))

def cal_delta_w(weights, input):
    global learning_rate
    return [list(map(lambda x, w: learning_rate*(x-w), input, w)) for w in weights]
