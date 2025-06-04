# 32978 아 맞다 마늘

N = int(input())
L = list(input().split())
LL = list(input().split())

for i in range(N - 1) :
    L.remove(LL[i])
print(L[0])