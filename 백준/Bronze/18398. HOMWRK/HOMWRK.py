T = int(input())
for i in range(T) :
    N = int(input())
    for j in range(N) :
        Ai, Bi = map(int, input().split())
        print(Ai + Bi, Ai * Bi)