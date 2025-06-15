# 12840 창용이의 시계

import sys
input = sys.stdin.readline

h, m, s = map(int, input().split())
t = h * 3600 + m * 60 + s
q = int(input())
for i in range(q) :
    S = input()
    if len(S) > 2 :
        T, c = map(int, S.split())
        if T == 1 :
            t += c
        else :
            t -= c
    else :
        h = t // 3600
        m = (t % 3600) // 60
        s = t % 60
        h = h % 24
        print(h, m, s)