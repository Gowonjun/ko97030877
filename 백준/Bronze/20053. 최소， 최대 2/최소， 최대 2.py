# 20053 최소, 최대 2

T = int(input())
for _ in range(T) :
    N = int(input())
    L = list(map(int, input().split()))
    print(min(L), max(L))