L = list(map(int, input().split()))
L.remove(max(L))
L.remove(min(L))
print(L[0])