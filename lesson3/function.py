def my_sum(my_list):
    s = 0
    for i in my_list:
        s += i
    return s

print(my_sum([1,2,3,4,5,6,7,8,9,10]))

#аргументы по умолчанию
def test(a, b = 10 ):
    return a + b

print (test(1,1))

#def list_sum(my_list, initvalue=0)
# с помощью * в параметрах прокидывается
# любое количество
def test(a, *args):
    print("a: {}".format(a))
    for arg in args:
        return print(arg)


test(1,3)
test(1,2,3,4,5)
my_list = [2, 3, 4]
my_dict = {'b':2}
#test(**my_dict)
#def save(**kwargs):
    # kwargs - это любой элемент, например таблицы, путь и т д
#if 'path' #сохраним в файл
#if 'table' #сохраним в БД табицу

#######################

test_x = lambda x: x*x
print(test_x(3))
#определяем функцию прямо при вызове фильтра-функции
rest = filter(lambda x: x > 10, [1, 2, 3, 4, 10, 11, 12])
print (list(rest))

def test(x: int)->str:
    return x

#чтобы сделать подскахку,что мы ожидаем на вход в функцию
#лист
from typing import List
def test(x: List[int]):
    return x