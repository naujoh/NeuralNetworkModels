import random

def generate_weights(inputs_q): return [random.uniform(-0.5, 0.5) for n in range(inputs_q+1)]

def train(learning_rate, epoch_q, dataset, weights):
    return train(learning_rate, epoch_q-1, dataset, converge(dataset, learning_rate, weights)) if (epoch_q > 0) else converge(dataset, learning_rate, weights)

def converge(dataset, learning_rate, weights):
    head, *tail = dataset
    return adjust_w(weights, learning_rate, head) if tail == [] else converge(tail, learning_rate, adjust_w(weights, learning_rate, head))

def adjust_w(weights, learning_rate, data):
    return list(map(lambda w, delta_w: w+delta_w, weights, calculate_delta_w(learning_rate, data, weights)))

def calculate_delta_w(learning_rate, data, weights):
    *body, last = data
    return [learning_rate * (last-predict(body, weights)) * elem for elem in body]+[learning_rate*(last-predict(body, weights))]

def predict(input, weights):
    return 1.0 if sum(list(map(lambda w,x: w*x, weights, input))) + weights[-1] >= -weights[-1] else 0.0