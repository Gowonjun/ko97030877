# 10569 다면체

T = int(input())
for _ in range(T) :
    V, E = map(int, input().split())
    res = 2 - V + E
    print(res)