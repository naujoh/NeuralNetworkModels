w = []
set_a = []
set_b = []
I = []

def storage(_set_a, _set_b):
    global w
    global set_a
    global set_b
    global I
    set_a = _set_a
    set_b = _set_b
    a, b = len(set_a[0]), len(set_b[0])
    w = [[0 for x in range(b)] for y in range(a)]
    I = [[0 for x in range(b)] for y in range(a)]
    for i in range(a):
        for j in range(b):
            sum = 0
            if i == j:
                I[i][j] = 1
            else:
                sum = set_a[0][i] * set_a[0][i] + set_b[0][j] * set_b[0][j] - 2 * I[i][j]
            w[i][j] = sum
