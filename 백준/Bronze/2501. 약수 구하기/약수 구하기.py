N, K = map(int, input().split())
L = []
for i in range(1, N + 1) :
    if N % i == 0 :
        L.append(i)
L.sort()
try :
    print(L[K - 1])
except :
    print(0)