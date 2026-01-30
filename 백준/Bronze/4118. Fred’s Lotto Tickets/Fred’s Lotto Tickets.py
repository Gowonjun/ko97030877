# 4118  Fred’s Lotto Tickets

while True :
    N = int(input())
    if N == 0 :
        break
    s = []
    for _ in range(N) :
        L = list(map(int, input().split()))
        for elem in L :
            s.append(elem)
    s = set(s)
    s = list(s)
    if len(s) == 49 :
        print('Yes')
    else :
        print('No')