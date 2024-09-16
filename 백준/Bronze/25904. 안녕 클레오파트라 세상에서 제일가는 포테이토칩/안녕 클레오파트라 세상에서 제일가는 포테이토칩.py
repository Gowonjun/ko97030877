N, X = map(int, input().split())
L = list(map(int, input().split()))
flag = True
while flag :
    for i in range(N) :
        if L[i] >= X :
            X += 1
        else :
            print(i + 1)
            flag = False
            break