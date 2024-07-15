N, P, S = map(int, input().split())
for i in range(S) :
    L = list(map(int, input().split()))
    del L[0]
    if P in L :
        print('KEEP')
    else :
        print('REMOVE')