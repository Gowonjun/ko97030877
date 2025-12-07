# 34891 MT 준비

N, M = map(int, input().split())
if N % M == 0 :
    res = N // M
else :
    res = N // M + 1
print(res)