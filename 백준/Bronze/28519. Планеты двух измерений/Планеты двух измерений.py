N, M = map(int, input().split())

if N == M :
    print(N + M)
else :
    if N > M :
        print(2 * M + 1)
    else :
        print(2 * N + 1)