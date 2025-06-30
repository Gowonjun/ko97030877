# 21339 Contest Struggles

n, k = map(int, input().split())
d, s = map(int, input().split())

ans = (n * d - k * s) / (n - k)
if 0 > ans or 100 < ans :
    print('impossible')
else :
    print(ans)