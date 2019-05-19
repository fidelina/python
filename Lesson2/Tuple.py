#Написать собственную реализацию встроенной функции enumerate()
# применяется для итерируемых коллекций (строки, списки, словари и др.)
# и создает объект, который генерирует кортежи,
# состоящие из двух элементов - индекса элемента и самого элемента:

#Создание словаря
def tuplegen(x):
    tup = {i: x[i]  for i in range(len(x))}
    return tup
l = [1, 6, 7, 8, 9, 77, 0]
r = tuplegen(l)
print(r)

#Создание tuple
def tuplegen(x):
    r = []
    for i in range(len(x)):
        tup = (i, x[i])
        r.append(tup)
    return r

# Создание tuple, то же самое, только коротко, однострочником
def tuplegen(x):
    tup = [(i, x[i])  for i in range(len(x))]
    return tup
l = [1, 6, 7, 8, 9, 77, 0]
r = tuplegen(l)
print(r)