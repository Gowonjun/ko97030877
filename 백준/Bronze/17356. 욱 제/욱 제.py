A, B = map(int, input().split())
M = (B - A) / 400
p = 1 / (1 + pow(10, M))
print(p)