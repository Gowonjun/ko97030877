# 4435  중간계 전쟁

T = int(input())
for i in range(1, T + 1) :
    a, b, c, d, e, f = map(int, input().split())
    g, h, j, k, l, m, n = map(int, input().split())
    gandalf = a + 2 * b + 3 * c + 3 * d + 4 * e + 10 * f
    saruman = g + 2 * h + 2 * j + 2 * k + 3 * l + 5 * m + 10 * n
    if gandalf > saruman :
        print('Battle %d: Good triumphs over Evil' % i)
    elif gandalf < saruman :
        print('Battle %d: Evil eradicates all trace of Good' % i)
    else :
        print('Battle %d: No victor on this battle field' % i)