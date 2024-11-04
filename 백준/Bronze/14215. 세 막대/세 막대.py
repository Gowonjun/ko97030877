# 14251 세 막대

L = list(map(int, input().split()))
L.sort()
a = L[0]
b = L[1]
c = L[2]
if a + b > c :
    print(a + b + c)
else :
    print(a + b + (a + b - 1))