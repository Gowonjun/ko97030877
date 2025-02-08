n = int(input())
for i in range(1, n + 1) :
    print('Scenario #%d:' % i)
    L = list(map(int, input().split()))
    L.sort()
    #print(L)
    if pow(L[0], 2) + pow(L[1], 2) == pow(L[2], 2) :
        print('yes')
    else :
        print('no')
    print()