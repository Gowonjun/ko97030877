# 2863  이게 분수?

A, B = map(int, input().split())
C, D = map(int, input().split())
zero = A / C + B / D
once = C / D + A / B
twice = D / B + C / A
third = B / A + D / C
if max(zero, once, twice, third) == zero :
    print(0)
elif max(zero, once, twice, third) == once :
    print(1)
elif max(zero, once, twice, third) == twice :
    print(2)
else :
    print(3)