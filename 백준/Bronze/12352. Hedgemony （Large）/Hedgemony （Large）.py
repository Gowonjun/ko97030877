# 12352 Hedgemony (Large)

T = int(input())
for i in range(1, T + 1) :
    N = int(input())
    L = list(map(int, input().split()))
    for j in range(1, N - 1) :
        #print(j)
        avg = (L[j - 1] + L[j + 1]) / 2
        if avg < L[j] :
            L[j] = avg
    print('Case #%d: %f' % (i, L[-2]))