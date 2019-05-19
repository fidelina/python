from typing import List

# line = list(input("Input new number"))
line = (1, 5, 23, 90, 100, 1, 4)


def maxim(x: List[int]) -> int:
    # maxim='-inf'
    maxim = line[0]
    for i in range(len(x)):
        if line[i] > maxim:
            maxim = x[i]
        continue
    return print(maxim)


maxim(line)
