# 11970 Fence Painting

L = []
a, b = map(int, input().split())
c, d = map(int, input().split())

for i in range(a, b + 1) :
    L.append(i)
for j in range(c, d + 1) :
    if j not in L :
        L.append(j)
L.sort()
#print(L)

cnt = 0
for i in range(1, len(L)) :
    if L[i] - L[i - 1] == 1 :
        cnt += 1
print(cnt)