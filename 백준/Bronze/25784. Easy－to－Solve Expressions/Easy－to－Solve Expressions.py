L = []
L = list(map(int, input().split()))
L.sort()
a = L[0]
b = L[1]
c = L[2]
if a + b == c :
    print(1)
elif a * b == c :
    print(2)
else :
    print(3)