import numpy as np


a = np.array([1, 2, 3])
print(a)
print('______________')
print(type(a))
print('______________')
b = np.array([[1.5, 2, 3], [4, 5, 6]])
print(b)
print('______________')
b = np.array([[1.5, 2, 3], [4, 5, 6]], dtype=np.complex)
print(b)
print('______________')
print(np.zeros((3, 5)))
print('______________')
print(np.ones((2, 2, 2)))
print('______________')
print(np.eye(8))
print('______________')
np.empty((3, 3))
print('______________')
np.empty((3, 3)) #используется для тестов, например для тестирования картинок или логики
print('______________')
def f1(i, j):
    return 3 * i + j

print(np.fromfunction(f1, (3, 4)))
print(np.fromfunction(f1, (3, 3)))
