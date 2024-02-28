L = []
C = int(input())
for _ in range(C) :
    hap = 0
    over = 0
    L = list(map(int,input().split()))
    n = L[0]
    L.remove(L[0])
    for elem in L :
        hap += elem

    mean = hap / n
    for elem in L :
        if elem > mean :
            over += 1
    percent = over / n * 100
    print('%.3f%%' % percent)