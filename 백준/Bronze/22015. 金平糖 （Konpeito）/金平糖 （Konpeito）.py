L = list(map(int, input().split()))
L.sort(reverse=True)
print(L[0] - L[1] + L[0] - L[2])