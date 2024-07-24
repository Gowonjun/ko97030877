T = int(input())
for i in range(T) :
    n = 0
    N, A, D = map(int, input().split())
    for i in range(N) :
        n += i
    print(n * D + N * A)