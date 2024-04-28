L = list(map(int, input().split()))
L.sort()
a = L[0]
b = L[1]
c = L[2]

if pow(a, 2) + pow(b, 2) == pow(c, 2) :
    print(1)
elif a == b and b == c :
    print(2)
else :
    print(0)