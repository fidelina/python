import numpy as np

def f2(i, j):
    return j % 2

print(np.fromfunction(f2, (3, 4)))


