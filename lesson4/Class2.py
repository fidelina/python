
class Employee:
#Конструктор класса, что с объектом происходит на момент создания объекта:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login = (first_name[0] + last_name).lower()

# __init__ - конструктор класса, аналогично джаве и плюсам

    def say(self, word):
        print("{} say {}".format(self, word))
 #   def __repr__(self, ):
  #      return print("Employee-to")

e1 = Employee('Al', 'Rid')

print(e1)

#Наследование объектов, создаем дочерний объект,
# который наследует все от Employee (если указано 2 родителя
# и совпадают методы, то 2й перетирает 1го родителя)

class Manager(Employee):
    def __init__(self, first_name, last_name, employees):
        super().__init__(first_name, last_name) # чтобы дочерний класс переопределить с уникальным значением
        self.employees = employees #а вот и новый аттребут, который мы добавили

    def get_employees_count(self):
        return len(self.employees)


