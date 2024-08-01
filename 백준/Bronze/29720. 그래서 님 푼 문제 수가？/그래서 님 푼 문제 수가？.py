N, M, K = map(int, input().split())
m = N - M * K   # min
print(max(m, 0), max(m + M - 1, 0))