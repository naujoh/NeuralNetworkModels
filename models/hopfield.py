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
    a, b = len(set_a), len(set_b)
    w = [[0 for x in range(b)] for y in range(a)]
    I = [[0 for x in range(b)] for y in range(a)]
    for i in range(a):
        for j in range(b):
            sum = 0
            if i == j:
                I[i][j] = 1
            else:
                sum = set_a[i] * set_a[i] + set_b[j] * set_b[j] - 2 * I[i][j]
            w[i][j] = sum

def test():
    y1 = []
    y2 = []
    for row in I:
        sum1 = 0
        sum2 = 0
        for i in range(len(row)):
            sum1 += row[i] * set_a[i]
            sum2 += row[i] * set_b[i]
        if sum1 > 0:
            y1.append(1)
        elif sum1 < 0:
            y1.append(-1)
        else:
            y1.append(0)
        if sum2 > 0:
            y2.append(1)
        elif sum2 < 0:
            y2.append(-1)
        else:
            y2.append(0)
    return y1 == set_a and y2 == set_b
