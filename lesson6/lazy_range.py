#l = lazy_range(1, 5)
def lazy_range():
    for i in [1, 2, 3, 4]:
        print('now i process {}'.format(i))
        yield i

l = lazy_range()
print(l)
for i in l:
    print(i)
