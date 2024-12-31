# 32604 Jumbled Scoreboards

flag = 0
ta, tb = 0, 0   # t = temporary
n = int(input())
for _ in range(n) :
    a, b = map(int, input().split())
    if ta > a :
        flag = 1
    if tb > b :
        flag = 1
    ta = a
    tb = b
if flag == 1 :
    print('no')
else :
    print('yes')