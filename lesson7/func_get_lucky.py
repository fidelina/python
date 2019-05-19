import math

#a = (7, 77, 777, 67, 70, 00, 9)
def get_lucky(a):
    x = []
    for i in a:
        if '7' in str(i):
            x.append(i)
    return x

#z = get_lucky([7, 77, 777, 67, 70, 00, 9])

#print(z)

class Circle:


    r = 0

    def __init__(self, r):
        self.r = r
        self.diam = 2 * r


    def area(self):
        return math.pi * self.r * self.r


    def __lt__(self, other):
        return self.r < other

    def __gt__(self, other):
        return self.r > other

    def __eq__(self, other):
        return  self.r == other

    def __ne__(self, other):
        return  self.r != other


x = 5
y = 7
z = x - y
z = z * z

r = get_lucky([127, 619, 70007, 345])

print(r)

c1 = Circle(7)
c2 = Circle(7.5)

print(c1 != c2)