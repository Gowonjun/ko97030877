n = int(input())
for i in range(n) :
    a, b = map(float, input().split())
    res = abs(a - b)
    print('%.1f' % res)