# 34308 Abby's Absolutes

N, K = map(int, input().split())
L = list(map(int, input().split()))
LL = []
for i in range(K) :
    if N - L[i] < L[i] - 1 :
        print(N, end = ' ')
    else :
        print(1, end = ' ')