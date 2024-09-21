T = int(input())
for i in range(T) :
    n, m = map(int, input().split())
    hap = 0
    hap = (n + m) * (m - n + 1) // 2
    print('Scenario #%d:' % (i + 1))
    print(hap)
    print()