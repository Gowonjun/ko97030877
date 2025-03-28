# 30032 알파벳 뒤집기

N, D = map(int, input().split())
for _ in range(N) :
    L = list(input())
    if D == 1 :
        for i in range(N) :
            if L[i] == 'd' :
                L[i] = 'q'
            elif L[i] == 'b' :
                L[i] = 'p'
            elif L[i] == 'q' :
                L[i] = 'd'
            else :
                L[i] = 'b'
    else :
        for i in range(N) :
            if L[i] == 'd' :
                L[i] = 'b'
            elif L[i] == 'b' :
                L[i] = 'd'
            elif L[i] == 'q' :
                L[i] = 'p'
            else :
                L[i] = 'q'
    print(''.join(L))