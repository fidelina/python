#Написать класс  Rectangle, который имеет длину и ширину
# и методы вычисления периметра и площади.
#•Создайте класс Square.
# Он должен иметь такие же методы,
# что и прямоугольник
#•Подумайте над тем, можно ли применить наследование
# при создании двух этих классов

class Rectangle:
    """Rectangle-My-Class"""

    len = "Unknown" # поля
    wi = "Unknown"
    def __init__(self, len, wi):
        self.len = len
        self.wi = wi

    def sq(self):
        """Calculate square"""
        sq = self.len * self.wi
        return sq

    def per(self):
        """Calculate perimeter"""
        per = 2 * self.len + 2 * self.wi
        return per

    def __repr__(self):
        return 'Object is {}'.format(self.len) + ', {}'.format(self.wi)

object1 = Rectangle(5,7)
per_rec = object1.per()
sq_rec = object1.sq()
print(per_rec)
print(sq_rec)
print(object1)

class Square(Rectangle):
    def __init__(self, len):
        self.len = len
        self.wi = len

object2 = Square(5)
per_sq = object2.per()
sq_sq = object2.sq()
print(per_sq)
print(sq_sq)

