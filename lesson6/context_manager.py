import time

fp = open("./file.txt", "w")
fp.write("Hello, World")
fp.close()
# простой пример - работа с файлом
# файл нужно закрывать самому


with open("./file.txt", "w") as fp:
   fp.write("Hello, World")
#  c with файл закроется сам, как только уйдет из его блока

class TestManager:
    start = 0
    def __enter__(self):
        print('Сейчас начнется код внутри менеджера')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Код выполнился. Инфа об ошибке: тип - {}'.format(exc_type))

with TestManager():
     print(1 + 1)

