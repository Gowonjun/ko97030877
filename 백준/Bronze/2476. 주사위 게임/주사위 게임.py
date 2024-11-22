#

p = 0   # p == price
L = []
N = int(input())
for _ in range(N) :
    a, b, c = map(int, input().split())
    if a == b and b == c :
        p = 10000 + a * 1000
        L.append(p)
    elif a == b :
        p = 1000 + a * 100
        L.append(p)
    elif a == c :
        p = 1000 + a * 100
        L.append(p)
    elif b == c :
        p = 1000 + b * 100
        L.append(p)
    else :
        p = max(a, b, c) * 100
        L.append(p)
print(max(L))