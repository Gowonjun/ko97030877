# 27475 Cancel the Trains

t = int(input())
for _ in range(t) :
    n, m = map(int, input().split())
    Ln = list(map(int, input().split()))
    Lm = list(map(int, input().split()))
    s = set(Ln + Lm)
    print(n + m - len(s))