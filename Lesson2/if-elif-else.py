#вывести на экан тип объекта
x = [1,2,3]
print(x)

#проверить тип данных переменной
x = int ('3')
print(type(x))

from random import randint
number = randint(1,19)
z = int(input('Введите целое число:'))
if z == number:
    print("Угадали")
    print('Bye!')
elif z > number:
    print("число больше загаданного")
elif z < number:
    print("число меньше загаданного")
print("принт за условием")
