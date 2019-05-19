#Определить, симметричен ли заданный во входном файле текст.

f = open('simmetr.txt', 'wt') # w - создавать каждый раз новый файл
                        # a - дописать в существующий файл
f.write("adejjeda")
f.close()
f = open('simmetr.txt', "rt")

with f as file:
    for line in f.readlines():
        for word in line.split():
            for i in range(0, int(len(word)/2)):
                if word[0] == word[-1]:

            bad_word = False
            for char in word:
                if char.isdigit():
                    print(word)
                    bad_word = True
            if not bad_word:
                list_new_file.append(word)
        list_new_file.append('\n')
text = ' '.join(list_new_file)

print(list_new_file)
print(text)
new_file.write(text)
new_file.close()

