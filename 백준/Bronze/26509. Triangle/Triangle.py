# 26509 Triangle

n = int(input())
for _ in range(n) :
    L1 = list(map(int, input().split()))
    L2 = list(map(int, input().split()))
    L1.sort()
    L2.sort()
    #print(L1, L2)
    if L1[0] ** 2 + L1[1] ** 2 == L1[2] ** 2 and L1 == L2 :
        print('YES')
    else :
        print('NO')