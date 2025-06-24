# 25774 Simplified Calendar System

d, m, y, n = map(int, input().split())
if n == 7 :
    n = 0
D, M, Y = map(int, input().split())
t = d + m * 30 + y * 360
T = D + M * 30 + Y * 360
a = ((T - t) % 7 + n) % 7
if a == 0 :
    a = 7
print(a)