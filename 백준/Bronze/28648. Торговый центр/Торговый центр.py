L = []
n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    L.append(a + b)
print(min(L))