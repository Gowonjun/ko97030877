# 2875  대회 or 인턴

N, M, K = map(int, input().split())
while True :
    if K == 0 :
        break
    if N >= M * 2 :
        N -= 1
        K -= 1
    else :
        M -= 1
        K -= 1
print(min(N // 2, M))