# Один из простых вариантов сортировки - сортировка выбором.

# arr = [0,3,24,2,3,7]
# // здесь реализованный алгоритм
# // на выходе должен получится список, содержащий [0, 2, 3, 3, 7, 24]

arr = [0, 3, 24, 2, 3, 7]
sort_arr = []
min_i = arr[0]
for j in range(0, len(arr)):
    for i in range(0, len(arr)):
        if arr[i] < min_i:
            min_i = arr[i]
        continue
    arr.remove(min_i)
    sort_arr.append(min_i)
    if not(len(arr) == 0):
        min_i = arr[0]
    else:
        break
print(sort_arr)
