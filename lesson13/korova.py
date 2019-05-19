import random

randnum = str(random.randint(1000, 9999))
print(randnum)
while True:
    usernum = input('Введите число четырехзначное')
    cow = 0
    bull = 0
    bull_ = 0
    if usernum == randnum:
        print(f'Congratulation! {randnum} is right!')
        break
    else:
        for i in range(4):
            if usernum[i] == randnum[i]:
                cow += 1
            else:
                if usernum[i] in randnum:
                    bull_ += 1
    #    for j in str(usernum):
    #        if j in randnum:
    #            bull += 1

        print(f'cow={cow}, bull={bull}, bull_={bull_}')
