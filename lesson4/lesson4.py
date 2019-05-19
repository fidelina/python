x =""
while len(x) < 5 or len(x) > 5:
    x = list(input("Input new number"))
    break
else:
    for i in range(len(x)):
        print(x + 1, "Цифра", x[i])
