#Создаем класс монитор:
class monitor():
    pass

m = monitor()
#Завершилось создание класса

#метод, это функция привязанная к классу
#методы вызываются через точку m.on()



# Поля и методы класса

class Employee:
    """Работник"""

    first_name = "Unknown" # поля
    last_name = "Unknown"

    def get_full_name(self): # методы
        return self.first_name + ' ' + self.last_name

e = Employee()

# обращаться к аттрибутам и методам нужно через точку
print(e.first_name)

fullname = e.get_full_name()
print(fullname)


employee1 = Employee()
# аттрибуты можно править:
employee1.first_name = "Al"
employee1.last_name = "Rid"
print(employee1.get_full_name())

employee1.middle_name = "Rock"
print(employee1.middle_name)



