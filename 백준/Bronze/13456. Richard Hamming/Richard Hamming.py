# 13456 Richard Hamming

T = int(input())
for _ in range(T) :
    n = int(input())
    v = list(map(int, input().split()))
    u = list(map(int, input().split()))
    cnt = 0
    for i in range(n) :
        if v[i] != u[i] :
            cnt += 1
    print(cnt)