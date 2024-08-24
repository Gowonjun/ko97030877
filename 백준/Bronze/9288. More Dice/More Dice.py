T = int(input())
for i in range(T) :
    n = int(input())
    print('Case %d:' % (i + 1))
    
    cnt = 1
    while True :
        if cnt < 7 and n - cnt < 7 :
            print('(%d,%d)' % (cnt, n - cnt))
        cnt += 1
        if cnt > n - cnt :
            break