#Написать ф-ию wave, которая будет принимать строку, а возвращать список строк с такими же символами, но один из символов будет заглавным
#wave("hello") => ["Hello", "hEllo", "heLlo", "helLo", "hellO"]

from typing import List

def wave(x: str) -> List[str]:
    list_fn = []
    for i in range(0, len(x)):
        a = x[:i] + x[i].upper() + x[i+1:]
#        y.replace(y[i], a)
        list_fn.append(a)
    return list_fn


x = str("hello")
y = x[0].upper()
w = wave('hello')
print(w)
