N = int(input())
Lx = [] ; Ly = []
for i in range(N) :
    x, y = map(int, input().split())
    Lx.append(x)
    Ly.append(y)
a = min(Ly)
b = Ly.index(a)
print(Lx[b], a)