# 6437  Golf

i = 1
while True :
    
    p, s = map(int, input().split())
    if p == 0 :
        break
    else :
        print('Hole #%d' % i)
    if s == 1 :
        print('Hole-in-one.')
    else :
        n = p - s
        if n <= -2 :
            print('Double Bogey.')
        elif n == -1 :
            print('Bogey.')
        elif n == 0 :
            print('Par.')
        elif n == 1 :
            print('Birdie.')
        elif n == 2 :
            print('Eagle.')
        elif n == 3 :
            print('Double eagle.')
    print()
    i += 1