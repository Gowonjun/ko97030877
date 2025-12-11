# 21197 Stopwatch

L = []
N = int(input())
if N % 2 == 1 :
    for _ in range(N) :
        L.append(int(input()))
    print('still running')
else :
    for _ in range(N) :
        L.append(int(input()))
    hap = 0
    for i in range(0, N, 2) :
        #print(i)
        hap += L[i + 1] - L[i]
    print(hap)