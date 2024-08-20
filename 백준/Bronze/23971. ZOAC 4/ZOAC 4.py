import math
H, W, N, M = map(int, input().split())
a = math.ceil(H / (1 + N)) * math.ceil(W / (1 + M))
print(a)