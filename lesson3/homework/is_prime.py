#Написать функцию is_prime, принимающую 1 аргумент — число от 0 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

def is_prime(x:int ):
    if 0 <= x <= 1000:
        list_div = [2, 3, 5, 11]
        for i in list_div:
            if x % i == 0:
                return False
        for j in range(2, x - 1):
            if x % j == 0:
                return False
        return True

f = is_prime(23)
print(f)


