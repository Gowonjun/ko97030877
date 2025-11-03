# 13222 Matches

N, W, H = map(int, input().split())
for i in range(N) :
    a = int(input())
    if pow(W, 2) + pow(H, 2) >= pow(a, 2) :
        print('YES')
    else :
        print('NO')