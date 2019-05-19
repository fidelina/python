d1 = {}
d2 = {'a':1, 'b': '2'}
d3 = dict(a=1, b='2')
d4 = dict([('a', 1), ('b', '2')])
d5 = dict.fromkeys(['a', 'b'])
print(d5)
d6 = dict.fromkeys(['a', 'b'], 2)
print(d6)

d7 = {x: x ** 3 for x in (0, 1, 2, 3)}
print(d7)
print(d7[3])
del d7[1]
print(d7)
example = 2 in d7
print(example)

user = {
'name': 'Олег',
    'email': 'oleg@example.com',
    'address': {
        'city': 'Москва',
        'street': 'Тверская'
    },
    'hobby': ['рисование', 'пение']
}
print(user['name'], user['address']['city'], user['hobby'])