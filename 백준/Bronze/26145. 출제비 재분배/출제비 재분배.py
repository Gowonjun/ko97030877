N, M = map(int, input().split())
S = list(map(int, input().split()))
for _ in range(M) :
    S.append(0)
for i in range(N) :
    T = list(map(int, input().split()))
    for j in range(N + M) :
        S[j] += T[j]
    S[i] -= sum(T)
for elem in S :
    print(elem, end = ' ')
