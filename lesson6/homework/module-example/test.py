import my_module
import sys


print('print __name__ in test.py: {}'.format(__name__))

# это удобно, можно запускать любой файл как обычную программу
# даже с аргументами

def my_program(*args):
    print('Моя программа начала работу. '
          'Ее аргументы: {}'.format(args))

if __name__ == '__main__':
    print('Эта программа запущена сама по себе. '
          'Как обычная программа')
    my_program(*sys.argv)
else:
    print('Меня импортировали в другой модуль. '
          'Поэтому написанная функция не запускается, '
          'ее будут использовать другие.')