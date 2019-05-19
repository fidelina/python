#Напишите свой менеджер контекста, замеряющий и показывающий время исполнения кода внутри него
import time

class logger:
    start = time.time()
    def __enter__(self):
        self.start = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        #print(f'Код выполнялся {stop - start}. Инфа об ошибке: тип - {exc_type}')
        print("Elapsed time: {:.3f} sec".format(time.time() - self.start))

with logger():
     time.sleep(2)
