# 18247 겨울왕국 티켓 예매

T = int(input())
for _ in range(T) :
    N, M = map(int, input().split())
    if N < 12 or M < 4 :
        print(-1)
    else :
        print(M * 11 + 4)