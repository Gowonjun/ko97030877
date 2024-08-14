T = int(input())
for i in range(T) :
    cnt = 0
    N, K = map(int, input().split())
    L = list(map(int, input().split()))
    for elem in L :
        cnt += elem // K
    print(cnt)