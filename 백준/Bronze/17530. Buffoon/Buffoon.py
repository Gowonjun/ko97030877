# 17530 Buffoon

N = int(input())
L = []
for _ in range(N) :
    v = int(input())
    L.append(v)
if max(L) == L[0] :
    print('S')
else :
    print('N')