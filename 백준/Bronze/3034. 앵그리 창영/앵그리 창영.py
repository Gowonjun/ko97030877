N, W, H = map(int, input().split())
for i in range(N) :
    l = int(input())
    if pow(W, 2) + pow(H, 2) >= pow(l, 2) :
        print('DA')
    else :
        print('NE')