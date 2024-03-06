cnt = 1
K = int(input())
for i in range(K) :
    hap = 0
    n, s, d = map(int, input().split())
    for i in range(n) :
        di, vi = map(int, input().split())
        if d * s >= di :
            hap += vi
    print('Data Set %d:' % cnt)
    print(hap)
    print()
    cnt += 1