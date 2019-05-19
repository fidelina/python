#Реализацию встроенной функции len: функция принимает список, возвращает его длину
from typing import List


def my_len(l: List[int]):
    if l != []:
        i = 0
        while l != []:
            i += 1
            l.pop()
    else:
        return 0
    return i

y = [1, 2, 3, 4, 5]
print(my_len(y))
