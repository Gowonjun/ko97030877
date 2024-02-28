L = []
n = 0
for _ in range(4) :
    d, u = map(int, input().split())
    n += u - d
    L.append(n)
print(max(L))