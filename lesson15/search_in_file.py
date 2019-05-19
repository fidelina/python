#В данном текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
f = open('f.xtx', 'wt') # w - создавать каждый раз новый файл
                       # a - дописать в существующий файл
f.write("Hello! \nI'm starting, study Python3")
f.close()
f = open('f.xtx', "rt")
new_file = open('new.txt', 'wt')
list_new_file = list()
with f as file:
    for line in f.readlines():
#        r = re.findall(word, line)
        for word in line.split():
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

