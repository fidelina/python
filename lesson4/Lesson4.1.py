print (set({1,2,3} & {4,3,2}))
print (set({1,2,3} | {4,3,2}))

print(all([]))

#Работа с текстом
f = open('f.xtx', 'wt') # w - создавать каждый раз новый файл
                        # a - дописать в существующий файл
f.write("Hello! \nI'm starting study Python")
f.close()
f = open('f.xtx', "rt")
print(f.read())

#Работа с байтами
t = open('t.xtx', 'wb') # w - создавать каждый раз новый файл
                        # a - дописать в существующий файл
t.write(b'Hello!')
t.close()
t = open('t.xtx', 'rb')
t.read()

