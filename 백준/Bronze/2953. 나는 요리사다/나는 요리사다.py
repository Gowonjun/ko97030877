# 2953  나는 요리사다

hap = 0
cnt = 0
for i in range(1, 6) :
    L = list(map(int, input().split()))
    if sum(L) > hap :
        hap = sum(L)
        cnt = i
print(cnt, hap)