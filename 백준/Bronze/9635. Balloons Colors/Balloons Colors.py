# 9635  Balloons Colors

T = int(input())
for _ in range(T) :
    N, X, Y = map(int, input().split())
    L = list(map(int, input().split()))
    e = L[0]; h = L[-1]
    if X == e and Y == h :
        print('BOTH')
    elif X == e and Y != h :
        print('EASY')
    elif X != e and Y == h :
        print('HARD')
    else :
        print('OKAY')