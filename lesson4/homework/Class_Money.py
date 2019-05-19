#Класс Деньги для работы с денежными суммами.
#Один объект должен иметь два аттрибута: рубли и копейки.
#Объект должен иметь метод, возращающий эквивалент
# объекта только в копейках в виде целого числа.
#На экран объект должен выводится как "x руб. y коп."
#Реализовать сложение, вычитание и операции сравнения
# между объектами деньгами (для этого есть специальные
# магические методы).

class Money:

    rub = 0
    kop = 0

    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def __repr__(self):
        return '{}'.format(self.rub) + 'руб. {}'.format(self.kop) + 'коп'

    def penny_count(self):
        return self.rub * 100 + self.kop

    def __add__(self, other):
        add = self.penny_count() + other.penny_count()
        r = add // 100
        k = add % 100
        return Money(r, k)

    def __sub__(self, other):
        sub = self.penny_count() - other.penny_count()
        r = sub // 100
        k = sub % 100
        return Money(r, k)

    def __lt__(self, other):
        return self.penny_count() < other.penny_count()

    def __gt__(self, other):
        return self.penny_count() > other.penny_count()

    def __eq__(self, other):
        return  self.penny_count() == other.penny_count()

m1 = Money(3, 30) # создаем объект равным 3 рублям и 30 копейкам

penny = m1.penny_count()

print('m1 в копейках равен {}'.format(penny))
# "m1 в копейках равен 330'

print(type(m1))
# int

m2 = Money(4, 95)

m3 = m1 + m2

print('Мы получили {}'.format(m3))
# на экране появится "Мы получили 8руб. 25 коп."

if m1 == m2:
    print('{} и {} равны'.format(m1, m2))
elif m1 > m2:
    print('{} больше чем {}'.format(m1, m2))
else:
    print('{} меньше чем {}'.format(m1, m2))