L = []
n = int(input())
for i in range(n) :
    LL = list(input().split())
    for elem in LL :
        L.append(elem)
for i in range(int(L[0]) + 1) :
    print(L[i])