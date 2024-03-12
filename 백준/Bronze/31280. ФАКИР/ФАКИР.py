L = []
L = list(map(int, input().split()))
L.remove(min(L))
print(sum(L) + 1)