# 15780 멀티탭 충분하니?

N, K = map(int, input().split())
L = list(map(int, input().split()))
hap = 0
for elem in L :
    if elem % 2 == 0 :
        hap += elem // 2
    else :
        hap += (elem // 2) + 1
if hap >= N :
    print('YES')
else :
    print('NO')