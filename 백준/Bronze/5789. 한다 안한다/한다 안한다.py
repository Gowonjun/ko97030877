N = int(input())
for i in range(N) :
    L = list(input())
    while True :
        if len(L) == 2 :
            break
        del L[0]
        del L[-1]
    if L[0] == L[1] :
        print('Do-it')
    else :
        print('Do-it-Not')