i = 0
while i != 5:
    i += 1
    if i == 3:
        break
print(i)


while True:
    i += 1
    print(i)
    if i == 6:
        print("Значение дошло до 6")
        break
else:
    print('здесь можно сохранить список в бд выполнив save.db')

while i !=21:
    i += 1
    if not i % 2:
        print(i)
    else:
        continue