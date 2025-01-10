# 6322  직각 삼각형의 두 변

cnt = 0
while True :
    cnt += 1
    a, b, c = map(int, input().split())
    if a == 0 and b == 0 and c == 0 :
        break
    else :
        if a == -1 :
            s = 'a'
            l = pow((pow(c, 2) - pow(b, 2)), 0.5)
        elif b == -1 :
            s = 'b'
            l = pow((pow(c, 2) - pow(a, 2)), 0.5)
        else :
            s = 'c'
            l = pow((pow(a, 2) + pow(b, 2)), 0.5)
        print('Triangle #%d' % cnt)
        if type(l) == complex or l == 0 :
            print('Impossible.')
        else :
            print('%s = %.3f' % (s, l))
        print()