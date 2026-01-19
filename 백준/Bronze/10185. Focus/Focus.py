# 10185 Focus

T = int(input())
for i in range(T) :
    p, q = map(int, input().split())
    f = p * q / (p + q)
    print('f = %.1f' % f)