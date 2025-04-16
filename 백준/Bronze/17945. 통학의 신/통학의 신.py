# 17945 통학의 신

A, B = map(int, input().split())
a = int((-A) + pow(pow(A, 2) - B, 0.5))
b = int((-A) - pow(pow(A, 2) - B, 0.5))
if a == b :
    print(a)
else :
    print(min(a, b), max(a, b))