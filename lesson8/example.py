import dis

a=5
d=1

def fun(a,b):
    c=0
    if a == d:
        c=a+d
    else:
        c=a-d
    return c


print(dis.dis(fun))