N, M, K = map(int, input().split())
n = K - M
cnt = 1
while True :
    if cnt * n < N :
        cnt += 1
    else :
        break
print(cnt)