import sys

N, M = map(int, input().split())
L = [0 for _ in range(N)]
for _ in range(M) :
    s = sys.stdin.readline()
    a, b = map(int, s.split())
    L[a - 1] += 1
    L[b - 1] += 1
for elem in L :
    print(elem)