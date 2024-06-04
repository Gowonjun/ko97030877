L = []
L = list(map(int, input().split()))
L.sort()
print(abs((L[0] + L[3]) - (L[1] + L[2])))