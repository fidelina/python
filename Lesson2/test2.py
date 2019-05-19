
import math

print(math.ceil(math.pi/2))

#Кортежи/Tupe
t = tuple('Hello!')
print(t)
if ('aaa' > 'b'):
    print ('Yes')
else:
    print ('no')
#строки
print(ord('ф'))
#вызываем методы обектов
print("Привет медвед, как дела?".split())


print("Привет медвед, как дела?".split('д'))

#обращение к элементам списков
s="abcde"
print(s[2]) #вывел с
print(s[2:4]) #вывел cd
print(s[len(s)-1])#вывел последнее значение
print(s[-4]) #реверсное значение, т е отсчитываем с конца
print(s[:-1]) #вернуть все, кроме последнего значения
print(s[:2]) #вывести 0,1 все кроме 2го символа!
print(None) #объект у которого свой тип данных, None type и там только 1
# значение пустота, как folse, true
print(float('inf')) #бесконечность
print(float('-inf')) #бесконечно малое значение

#генератор списков
list = [x * 2 for x in 'spam'] # умножаем каждое из символов spam на 2
print(list)
#Sorting list

list.sort(reverse=True)

print(list)
#Словари
d = {'a': 1, 'b': 2, }
print (d.get('b')) #проверить наличие ключей, если нет, вернет
#None или само значение по ключу, это безопасный метод проверки

#генерируем кортеж
d7 = {x: x ** 3 for x in (0, 1, 2, 3, 4)}
print (d7)
print(d7.keys())





