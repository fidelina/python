#библиотека multiprotion - запустить мультипроцессоровность
#suprocess - запустить другую программу
#Popen - позволяет создать экземпляр в процессе и получить и перехватить
#записать веременную и считать

#поток как альтернатива процессам. Поток = thread
#Поток унарная минимальная опирация в ОС
#В рамках одного процесса

# Без поточности
import random
import time

def compute(number):
    # что-то долго вычисляем
    print('Старт вычислений №{}'.format(number))
    sleeping = random.randint(1, 5)
    time.sleep(sleeping)
    print('Конец вычислений №{}. Затрачено {} секунд'.format(number, sleeping))

start = time.time()
# считаем что-то много раз с разными параметрами
for i in range(5):
    compute(i)
print('Общее время вычислений в секундах: {}'.format(int(time.time() - start)))


import threading
import random
import time


def compute(number):
    # что-то долго вычисляем тем же способом
    print('Старт вычислений №{}'.format(number))
    sleeping = random.randint(1, 5)
    time.sleep(sleeping)
    print('Конец вычислений №{}. Затрачено {} секунд'.format(number, sleeping))

start = time.time()
# считаем что-то много раз с разными параметрами
threads = []
for i in range(5):
    thr = threading.Thread(target=compute, args=(i,))
    thr.start()
    threads.append(thr)

for thr in threads:
    thr.join()
print('Общее время вычислений в секундах: {}'.format(int(time.time() - start)))

