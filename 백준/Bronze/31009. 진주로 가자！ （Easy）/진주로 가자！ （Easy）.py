cnt = 0
L = []
N = int(input())
for i in range(N) :
    D, C = map(str, input().split())
    C = int(C)
    if D == 'jinju' :
        j = C
    else :
        L.append(C)
for elem in L :
    if elem > j :
        cnt += 1
print('%d\n%d' % (j, cnt))