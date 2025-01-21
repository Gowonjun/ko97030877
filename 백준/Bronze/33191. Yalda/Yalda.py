# 33191 Yalda

N = 3
b = int(input())
L = []
for i in range(N) :
    L.append(int(input()))

flag = 0
cnt = 1
for elem in L :
    if elem <= b :
        b -= elem
        flag = 1
        if cnt == 1 :
            print('Watermelon')
        elif cnt == 2 :
            print('Pomegranates')
        elif cnt == 3 :
            print('Nuts')
        break
    cnt += 1
#w = int(input())
#p = int(input())
#n = int(input())
if flag == 0 :
    print('Nothing')