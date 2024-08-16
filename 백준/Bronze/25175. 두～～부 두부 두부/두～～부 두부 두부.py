cnt = 3
N, M, K = map(int, input().split())
while True :
    if cnt == K :
        print(M)
        break
    else :
        if cnt < K :
            cnt += 1
            if M == N :
                M = 1
            else :
                M += 1
        else :
            cnt -= 1
            if M == 1 :
                M = N
            else :
                M -= 1