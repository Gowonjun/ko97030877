# 34366 Mines Football

M = int(input())
res1, res2, res3, res4 = 0, 1000, 0, 8000
for i in range(M) :
    s = input()
    L = list(map(int, s[2 : ].split()))
    #print(L)
    if max(L) > res1 :
        res1 = max(L)
    if min(L) < res2 :
        res2 = min(L)
    if sum(L) > res3 :
        res3 = sum(L)
    if sum(L) < res4 :
        res4 = sum(L)
print(res1)
print(res2)
print(res3)
print(res4)