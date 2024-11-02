# 9063  대지

Lx = []
Ly = []
N = int(input())
for i in range(N) :
    x, y = map(int, input().split())
    Lx.append(x)
    Ly.append(y)
width = max(Lx) - min(Lx)
height = max(Ly) - min(Ly)
print(width * height)