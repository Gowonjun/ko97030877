D, H, M = map(int, input().split())
t = D * 60 * 24 + H * 60 + M
a = t - 11 * (60 * 24 + 60 + 1)
if a < 0 :
    print(-1)
else :
    print(a)