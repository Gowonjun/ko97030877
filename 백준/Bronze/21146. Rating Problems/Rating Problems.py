# 21146 Rating Problems

L = []
n, k = map(int, input().split())
for i in range(k) :
    L.append(int(input()))
print((sum(L) + (n - k) * (-3)) / n, (sum(L) + (n - k) * 3) / n)