#Составить программу, которая будет считывать введённое пятизначное число.
# После чего, каждую цифру этого числа необходимо вывести в новой строке.

#x = int(input('Введите пятизначное число:'))
#Variant 1
x = 12345
print(x // 10000) # 1 digits of numbers
print(x % 10000 // 1000)
print (x % 1000 // 100)
print (x % 100 // 10)
print (x % 10)

#Variant 2
w = True
while w:
    x1 = input('Введите пятизначное число:')
    print(x1)
    x = list(x1)
    lenx = len(x)
    if lenx == 5:
        w = False
        for i in range(1, 6):
            print(i, ' цифра равна ' + x[i-1])
    else:

        print(f"Вы ввели число в {lenx} символов")

