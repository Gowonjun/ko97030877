# 10698 Ahmed Aly

T = int(input())
for i in range(1, T + 1) :
    a, b, c, d, e = input().split()
    if eval(a + b + c) == int(e) :
        print('Case %d: YES' % i)
    else :
        print('Case %d: NO' % i)