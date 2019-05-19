# Легко создать свой итератор
# важно лишь поддержать интерфейс итератора
# то есть методы __iter__ и __next__
class Fibonacci:
   def __init__(self, N):
     self.n, self.a, self.b, self.max = 0, 0, 1, N
   def __iter__(self):
     # сами себе итератор: в классе есть метод next()
     return self
   def __next__(self):
      if self.n < self.max:
        a, self.n, self.a, self.b = self.a, self.n+1, self.b, self.a+self.b
        return a
      else:
        raise StopIteration


f = Fibonacci(10)

for i in f:
    print(i)

