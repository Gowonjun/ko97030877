# 35271 자대 배치

N, M = map(int, input().split())
A = list(map(int, input().split()))
L = [0] * M
LL = [0] * N
for i in range(N) :
    a, b, c = map(int, input().split())
    if L[a - 1] < A[a - 1] :
        L[a - 1] += 1
        LL[i] += a
    elif L[b - 1] < A[b - 1] :
        L[b - 1] += 1
        LL[i] += b
    elif L[c - 1] < A[c - 1] :
        L[c - 1] += 1
        LL[i] += c
    else :
        LL[i] = -1
for elem in LL :
    print(elem, end = ' ')