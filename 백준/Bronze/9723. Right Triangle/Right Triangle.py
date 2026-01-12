# 9723  Right Triangle

T = int(input())
for i in range(T) :
    L = list(map(int, input().split()))
    L.sort()
    #print(L)
    if pow(L[0], 2) + pow(L[1], 2) == pow(L[2], 2) :
        s = 'YES'
    else :
        s = 'NO'
    print('Case #%d: %s' % ((i + 1), s))