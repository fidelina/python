import math


def graph(fun, list):
    for i in list:
        count = int(fun(i))
        print(i,': ' + '#' * count)

graph(math.sqrt, [9, 25, 100])

