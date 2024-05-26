hap = 0
N = int(input())
L = []
for i in range(N) :
    L.append(int(input()))
M = int(input())
for i in range(M) :
    B = int(input())
    hap += L[B - 1]
print(hap)