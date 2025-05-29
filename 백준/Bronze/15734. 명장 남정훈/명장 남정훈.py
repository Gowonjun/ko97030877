# 15734 명장 남정훈

L, R, A = map(int, input().split())

while True :
    if L > R :
        if A > 0 :
            R += 1
            A -= 1
        else :
            break
    elif L < R :
        if A > 0 :
            L += 1
            A -= 1
        else :
            break
    else :
        break
if A % 2 == 0 :
    print(min(L, R) * 2 + A)    
else :
    print(min(L, R) * 2 + A - 1)