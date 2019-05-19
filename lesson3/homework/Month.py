# Написать код, который получает аргумент — номер месяца (от 1 до 12), и возвращающую время года,
# которому этот месяц принадлежит (зима, весна, лето или осень).
# Variant 1
month = str(input('Введите номер месяца:'))

if month == '1' or month == '01':
    print('January')
elif month == '2' or month == '02':
    print('February')
elif month == '3' or month == '03':
    print('March')
elif month == '4' or month == '04':
    print('April')
elif month == '5' or month == '05':
    print('May')
elif month == '6' or month == '06':
    print('June')
elif month == '7' or month == '07':
    print('July')
elif month == '8' or month == '08':
    print('August')
elif month == '9' or month == '09':
    print('September')
elif month == '10':
    print('October')
elif month == '11':
    print('November')
elif month == '12':
    print('December')
else:
    print('Ввели не верное число! Ожидаемый формат 1 или 2 или 12')

# Variant 2:
# d7 = {x: x ** 3 for x in (0, 1, 2, 3)}
month = {1: 'January', 2: 'February', 3: 'March', 4: 'April', \
         5: 'May', 6: 'June', 7: 'July', 8: 'August', \
         9: 'Septemder', 10: 'October', 11: 'November', 12: 'December'}

num = int(input("Введите номер месяца от 1 до 12:"))
if not (num in month):
    print('Введено не верное число!')
else:
    print(f" Month = {month[num]}.")
