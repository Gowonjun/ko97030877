# 34750 추석은 언제나 좋아

N = int(input())
o = N
if N >= 1000000 :
    N = (N // 100) * 80
elif N >= 500000 :
    N = (N // 100) * 85
elif N >= 100000 :
    N = (N // 100) * 90
else :
    N = (N // 100) * 95
print(o - N, N)