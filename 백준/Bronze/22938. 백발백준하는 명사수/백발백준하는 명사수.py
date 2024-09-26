X1, Y1, R1 = map(int, input().split())
X2, Y2, R2 = map(int, input().split())

if pow((X2 - X1), 2) + pow((Y2 - Y1), 2) < pow((R1 + R2), 2) :
    print('YES')
else :
    print('NO')