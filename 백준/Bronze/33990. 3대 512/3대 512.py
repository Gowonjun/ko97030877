# 33990 3대 512

N = int(input())
L = []
for _ in range(N) :
    A, B, C = map(int, input().split())
    hap = A + B + C
    if hap >= 512 :
        L.append(hap)
if len(L) == 0 :
    print(-1)
else :
    L.sort()
    print(L[0])