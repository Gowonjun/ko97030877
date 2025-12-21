# 19963 Санта Клаус

n, m, k = map(int, input().split())
s = {}
cnt = 1
s = set(range(1, n + 1))
s1 = set(map(int, input().split()))
s2 = set(map(int, input().split()))
s = s - s1 - s2
L = list(s)
print(len(L))
print(*L)