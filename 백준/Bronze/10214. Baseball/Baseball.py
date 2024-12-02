# 10214 Baseball

n = 9
T = int(input())
for _ in range(T) :
    cntY = 0
    cntK = 0
    for i in range(n) :
        Y, K = map(int, input().split())
        cntY += Y
        cntK += K
    if cntY > cntK :
        print('Yonsei')
    elif cntY < cntK :
        print('Korea')
    else :
        print('Draw')