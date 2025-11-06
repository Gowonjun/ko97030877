# 13228 The REAL Manhattan distance

T = int(input())
for i in range(T) :
    x1, y1, f1, x2, y2, f2 = map(int, input().split())
    print(abs(x2 - x1) + abs(y2 - y1) + f1 + f2)