mygen = (x*x for x in range(3))
print(mygen)
for i in mygen:
    print(i)
print(mygen)
for i in mygen:
    print(i)

mygen2 = (x*x for x in range(3))
print(list(mygen2))
print(list(mygen2))
