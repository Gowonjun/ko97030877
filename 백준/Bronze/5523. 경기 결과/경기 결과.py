import sys

cntA, cntB = 0, 0
N = int(input())
for i in range(N) :
    A, B = sys.stdin.readline().split()
    A = int(A)
    B = int(B)
    if A > B :
        cntA += 1
    elif A < B :
        cntB += 1
print(cntA, cntB)