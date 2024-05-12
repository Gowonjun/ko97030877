hap = 0
a, b, c = map(int, input().split())
A, B, C = map(int, input().split())

if a > A :
    pass
else :
    hap += A - a
if b > B :
    pass
else :
    hap += B - b
if c > C :
    pass
else :
    hap += C - c
print(hap)