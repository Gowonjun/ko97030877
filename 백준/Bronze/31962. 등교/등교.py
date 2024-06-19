n = 0
N, X = map(int, input().split())
for i in range(N) :
    S, T = map(int, input().split())
    if n < S and S + T <= X :
        n = S
if n == 0 :
    print(-1)
else :
    print(n)