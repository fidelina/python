def test(a, b):
    print('Process {} and {}'.format(a, b))


test(1, 1)


def my_decorator(fn):
    def wrap(a, b):
        print('Start my function')
        fn(a, b)
        print('End my function')

    return wrap


# @ - метка, что функция
# будет обернута декоратором
@my_decorator
def test(a, b):
    print('Process', a, b)


test(1, 1)


# фактически, обертка декоратором
# это тоже самое, что и:
def test(a, b):
    print('Process', a, b)


test = my_decorator(test)
test(1, 2)  # желаемый результат
