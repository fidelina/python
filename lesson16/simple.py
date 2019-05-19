t = type(2.5)(2)
print(type(t))
print(int(27e30))
a = [15, 20, 25, 30, 35]
print(a[::2])
#l = [m1, m2, m3] #заведомо извесно, что у объектов есть методы age, len, хотим отсортировать по возрасту
#def key_m(man):
#   return man.age
#l.sort(key=key_m)
#or
#l.sort(key=lambda x:x.age)

#set позволяет проводить опирации с  множествами
s1 = {1,2,3}
s2 = {2,3,4}
print(s1|s2) #объединение
print(s1&s2)

#for k,v in iters: достать ключь и значение при прогоне


