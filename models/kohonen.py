import random

# Generates j initial weights with n values between 0-1
def initialize(j, n):
    [[random.uniform(0.0, 1.0) for _ in range(j)] for _ in range(n)]
