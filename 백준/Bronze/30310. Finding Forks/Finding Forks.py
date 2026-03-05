# 30310 Finding Forks

n = int(input())
L = list(map(int, input().split()))
hap = 0
hap += min(L)
L.remove(min(L))
hap += min(L)
print(hap)