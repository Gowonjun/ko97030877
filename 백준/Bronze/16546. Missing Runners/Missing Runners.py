# 16546 Missing Runners

N = int(input())
L = list(map(int, input().split()))
a = ((1 + N) * N) // 2
print(a - sum(L))