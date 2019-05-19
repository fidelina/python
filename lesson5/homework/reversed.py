#Отсортировать список по возростанию
from typing import List

def reversed_sort(arr: List[int]):
    sort_arr = []
    max_i = arr[0]
    for j in range(0, len(arr)):
        for i in range(0, len(arr)):
            if arr[i] > max_i:
                max_i = arr[i]
            continue
        arr.remove(max_i)
        sort_arr.append(max_i)
        if not (len(arr) == 0):
            max_i = arr[0]
        else:
            break
    return sort_arr

l = [4, 7, 8, 1, 2, 6]

print(reversed_sort(l))

#Реализацию функции reversed: ф-ия принимает список, возращает его, но элементы расположенны в обратном порядке
def revers(l: List[int]):
    z = []
    for i in range(len(l)):
        z.insert(-i, l[i])
    return z


print(revers([4, 7, 8, 1, 2, 6]))