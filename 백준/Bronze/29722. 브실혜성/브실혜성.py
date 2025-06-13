# 29722 브실혜성

y, m, d = map(int, input().split('-'))

n = y * 360 + m * 30 + d

N = int(input())

n += N

y = n // 360
n -= y * 360
m = n // 30
d = n % 30

if m == 0 :
    m = 12
    y -= 1

if d == 0 :
    d = 30
    m -= 1

print('%04d-%02d-%02d' % (y, m, d))