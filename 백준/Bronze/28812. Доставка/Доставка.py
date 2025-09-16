# 28812 Доставка

L = []
n, C = map(int, input().split())
for i in range(n) :
    p, d, v = map(int, input().split())
    L.append(p + d + C * v)
print(min(L))