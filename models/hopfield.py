w = []

def storage(set_a, set_b):
    global w
    a, b = len(set_a[0]), len(set_b[0])
    w = [[0 for x in range(b)] for y in range(a)]
    for i in range(a):
        for j in range(b):
            sum = 0
            for xy_index in range(len(set_a)):
                x = set_a[xy_index]
                y = set_b[xy_index]
                sum += x[i] * y[j]
            w[i][j] = sum
