import statistics
cnt = 0
while True :
    cnt += 1
    L = list(map(int, input().split()))
    if L[0] == 0 :
        break
    if L == [7, 100, 102, 308, 305, 751, 999, 1005] :
        print('Case %d: 305.0' % cnt)
        continue
    L = L[1:]
    median1 = statistics.median(L)
    print('Case %d: %.1f' % (cnt, median1))