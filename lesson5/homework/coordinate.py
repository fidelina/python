#Напишите класс "Координата". При создании объекта должны приниматься значение оси X и значение оси Y.
# Класс должен иметь метод, который возращает число от 1 до 4, тем самым показывая, в каком участке находится точка.
#* Класс должен иметь метод, способный определить длинну прямой, которая соединяет координату (0, 0) до вашей координаты

class Coordinate():
    x = 0
    y = 0

    def __init__(self, x: int, y: int) -> int:
        self.x = x
        self.y = y

    def sector(self):
        if self.x > 0:
            if self.y > 0:
                return 1
            else:
                return 4
        else:
            if self.y > 0:
                return 2
            else:
                return 3

    def len_line(self):
        return  (self.y * self.y + self.x * self.x) ** 0.5

    def __repr__(self):
        return '({}'.format(self.x) + ', {})'.format(self.y)


a = Coordinate(-1, -1)
print(a.sector())
print(a)
a = Coordinate(-1, 1)
print(a.sector())
print(a)
a = Coordinate(1, -1)
print(a.sector())
print(a)
a = Coordinate(1, 1)
print(a.sector())
print(a)
a = Coordinate(3, 4)
len = a.len_line()
print(len)
