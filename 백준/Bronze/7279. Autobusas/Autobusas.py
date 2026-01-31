# 7279  Autobusas

N, K = map(int, input().split())
A = 0
L = [0]
for _ in range(N) :
    a, b = map(int, input().split())
    A += a
    A -= b
    res = A - K
    if res > 0 :
        L.append(res)
    #print(A)
print(max(L))