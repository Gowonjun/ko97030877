# 21866 추첨을 통해 커피를 받자

n = 100
cnt = 0
flag = 0
L = list(map(int, input().split()))
for elem in L :
    if elem > n :
        flag = 1
    cnt += 1
    if cnt == 2 :
        n = 200
    elif cnt == 4 :
        n = 300
    elif cnt == 6 :
        n = 400
    elif cnt == 8 :
        n = 500
hap = sum(L)
if flag == 1 :
    print('hacker')
else :
    if hap >= 100 :
        print('draw')
    else :
        print('none')