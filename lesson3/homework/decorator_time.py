#Написать декоратор timeit, которые с помощью метода time библиотеки time  будет выводить вам время исполнения​ ф-ии по её завершению
#import is_prime
import time

def factorial(x):
    f = 1
    for i in range(1, x + 1):
        f = f * i
    return f

print(factorial(4))

def timeit(fn):
    def wrap(*args):
        start = time.time()
        print(          'Стартовал в ', start)
        res = fn(*args)
        stop = time.time()
        print("завершился в ", stop)
        diff = stop - start
        print(diff)
        return res
    return wrap

#@timeit
#def sum(*args):
#    return {}
#l = [1, 8, 9, 23456789, 123456789, 123456789, 1232456789, 1232454678909, 1234567890]
#sum(l)
#@timeit
#def time.sleep(*args):
#    return {}

factorial = timeit(factorial)

f = factorial(12345)
print(f)

