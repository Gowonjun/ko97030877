L = list(map(int, input().split()))
x, y, r = map(int, input().split())
num = 0

for i in range(len(L)) :
    if L[i] == x :
        num = i + 1
        break
print(num)