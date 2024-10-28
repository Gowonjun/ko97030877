# 2903  중앙 이동 알고리즘

N = int(input())
cnt = 1
hap = 2
for _ in range(N) :
    hap += cnt
    cnt *= 2
print(pow(hap, 2))