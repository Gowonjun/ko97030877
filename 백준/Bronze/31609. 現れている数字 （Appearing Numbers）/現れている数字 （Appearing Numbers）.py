L = []
N = int(input())
if N == 1 :
    L = int(input())
    print(L)
else :
    cnt = 0
    L = list(map(int, input().split()))
    for i in range(len(L)) :
        if L.count(L[i]) > 1 :
            L[i] = ' '
            cnt += 1
    for i in range(cnt) :
        L.remove(' ')
    L.sort()
    for elem in L :
        print(elem)