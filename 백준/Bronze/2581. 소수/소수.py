# 2581 소수
# 실패
L = []
i = int(input())
fin = int(input())
if i == 1 and fin == i :
    print(-1)
else :
    if i == 1 :
        i = 2
    while True :
        flag = 0
        for j in range(2, i) :
            if i % j == 0 :
                flag = 1
                break
        if flag == 0 :
            L.append(i)
        i += 1
        if i > fin :
            break
    if len(L) == 0 :
        print(-1)
    else :
        print(sum(L))
        print(min(L))
    #print(L)