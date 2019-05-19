# Во втором задании вам необходимо написать консольную утилиту, используя argparse.
# Она должна принимать позиционный аргумент dirpath - это будет директория, внутри которой утилита создаст новую папку.
# Название новой папки будет зависеть от указанных опций. Если указана опция -y, то в назнании присуствует текущий год.
# Если -m, то номер текущего месяца. Если -d, то номер текущего дня. Опции можно комбинировать, подробности на примере.
# Если папка с заданным названием уже существует, то нужно просто выводить предупреждение об этом и больше ничего не делать.
# Если не указано ни одной опции, то утилита должна создать папку с именем 'unknown'.
# Чтобы узнать текущий месяц, день или год, нужно прочитать атрибуты объекта,
# который появится в результате вызова функции datetime.now() библиотеки datetime.
# Способ создания папки Вам придется найти самим.

import argparse
import os
import sys
import time


parser = argparse.ArgumentParser()
parser.add_argument("dirpath", help="path to new dir")
parser.add_argument("-y", "--year", #action='time.strftime("%Y")',
                    help="year")
parser.add_argument("-m", "--month", #action='time.strftime("%m")',
                    help="month")
parser.add_argument("-d", "--day", #action='time.strftime("%d")',
                    help="day")

if not os.path.exists(os.path.dirname(dirpath)):
    os.makedirs()
args = parser.parse_args()
answer = args.number**2
y = time.strftime("%Y")
print(y)

if os.fspath == args.dirpath:
    if args.year:
        os.mkdir()
#    print("the square of {} equals {}".format(args.number, answer))
else:
    print(answer)