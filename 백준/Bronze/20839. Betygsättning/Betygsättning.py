A, C, E = map(int, input().split())
a, c, e = map(int, input().split())
if e >= E :
    if c >= C :
        if a >= A :
            print('A')
        elif a >= A / 2 :
            print('B')
        else :
            print('C')
    elif c >= C / 2 :
        print('D')
    else :
        print('E')