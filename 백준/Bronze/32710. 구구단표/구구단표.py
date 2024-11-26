# 32710 구구단표

N = int(input())
L = []
for i in range(1, 10) :
    for j in range(1, 10) :
        L.append(i * j)
if N in L :
    print(1)
else :
    print(0)