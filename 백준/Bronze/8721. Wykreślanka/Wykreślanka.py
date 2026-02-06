# 8721  Wykreślanka

n = int(input())
L = list(map(int, input().split()))
cnt = 1
res = 0
for elem in L :
    if elem == cnt :
        cnt += 1
    else :
        res += 1
print(res)