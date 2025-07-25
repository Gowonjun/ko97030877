# 29729 가변 배열

S0, N, M = map(int, input().split())
v = S0
cnt = 0
for _ in range(N + M) :
    n = int(input())
    if n == 1 :
        cnt += 1
    else :
        if cnt > 0 :
            cnt -= 1
    while cnt > v :
        v *= 2
print(v)