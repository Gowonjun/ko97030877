import sys
input = sys.stdin.readline
Q = int(input())
L = []
for i in range(32) :
    L.append(pow(2, i))
for i in range(Q) :
    a = int(input())
    if a in L :
        print(1)
    else :
        print(0)