l = list('sample')
print(l)
num_list = list((1, 2, 3))
print(num_list)
list1 = []
list2 = ["a", ['m', 'n'], 3]
print(list2)
list1 = [x * 2 for x in 'spam']
print(list1)
list2 = [x + '!' for x in list1 if x != 'aa']
print(list2)

sort = sorted([5, 2, 3, 1, 4])
print(sort)

list1 = [5, 2, 3, 1, 4]
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

