n = int(input())
for _ in range(n) :
    a, b, c = map(int, input().split())
    print('Data set: %d %d %d' % (a, b, c))
    for i in range(c) :
        if a > b :
            a = a // 2
        else :
            b = b // 2
    print(max(a, b), min(a, b), '\n')