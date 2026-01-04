# 9776  Max Volume

pi = 3.14159
n = int(input())
res = []
for i in range(n) :
    L = list(input().split())
    if L[0] == 'S' :
        res.append(4 / 3 * pi * pow(float(L[1]), 3))
    elif L[0] == 'C' :
        res.append(pi * pow(float(L[1]), 2) * float(L[2]))
    else :
        res.append(1 / 3 * pi * pow(float(L[1]), 2) * float(L[2]))
print('%.3f' % max(res))