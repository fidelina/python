# Вы же создатите текстовое отображение папок и вложенных файлов:
#•Создайте класс BaseNode, которые принимает в констукторе имя и сохраняет его у себя. А также имеет метод __repr__, который ничего не делает.
#•Создайте класс File, который будет наследником  BaseNode. У него должен быть переопределен метод __repr__,
# который должен возвращать строку 'file: "<имя файла>"'.
#•Создайте класс Dir,   который будет наследником BaseNode. У него должно быть хранилище вложенных в него файлов и папок.
# Должен быть метод add, добавляющий файл или папку. Должен быть метод remove, удаляющий вложенную в него ранее файл или папку.
# И переопределен метод __repr__, который будет возвращать строку 'directory: <имя папки> (<перечисление вложенных папок и
# файлов через запятую или слово empty, если папка пуста>).

#В итоге у Вас должен написанный ниже код работать так, как в примере. Внимательно изучите пример, он даст все подсказки
# (включая знание об аргуметнах, которые должны принимать методы и т. д.). Посмотрите примеры реализации этого паттерна,
# она достаточно проста на любом языке.
from typing import List


class BaseNode:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        pass
    def save(self, name):
        pass
    def add(self, name):
        pass
    def remove(self, name):
        self.name = None
        return print(f"{self.name} is deleted")

class File(BaseNode):

    def __repr__(self):
        super().__repr__()
        return f"file: '{self.name}'"

class Dir(BaseNode):

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.list = []
#    def __init__(self) -> None:
#        self._children: List[BaseNode] = []


    def save(self, name):
        pass

#    def add(self, *args):
#        d = []
#        if args == type(Dir):
#            d.append(self.name())

#        for child in self.name:
#            results.append(child())
#        return d

    def add(self, d):
        self.list.append(d)
#        dir.parent = self


    def remove(self, name):
        self.list.pop()
        pass

    def __repr__(self):
        super().__repr__()

        return f"directory: '{self.name}'"

f1 = File('file1')
print(f1)
d1 = Dir('dir1')
print(d1)
d2 = Dir('dir2')
d1.add(d2)
print(d1)