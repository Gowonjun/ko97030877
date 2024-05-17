n = int(input())
for i in range(n) :
    a, b, c, d, e = 0, 0, 0, 0, 0
    m = 0
    a, b, c, d, e = map(int, input().split())
    m = max(a, b, c, d, e)
    print('Case #%d: %d' % (i + 1, m))