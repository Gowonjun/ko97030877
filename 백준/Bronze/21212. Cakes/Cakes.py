# 21212 Cakes

L = []
N = int(input())
for i in range(N) :
    a, b = map(int, input().split())
    L.append(b // a)
print(min(L))