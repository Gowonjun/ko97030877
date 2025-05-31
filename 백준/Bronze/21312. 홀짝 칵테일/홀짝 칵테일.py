# 21312 홀짝 칵테일

flag = 0
L = list(map(int, input().split()))
#print(L)
LL = []
L.sort(reverse=True)
for i in range(len(L)) :
    if L[i] % 2 == 1 :
        flag = 1
        LL.append(L[i])

res = 1
if flag == 0 :
    for elem in L :
        res *= elem
    print(res)
else :
    for elem in LL :
        res *= elem
    print(res)