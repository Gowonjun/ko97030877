n = int(input())
L = []
for i in range(n) :
    L.append(input())
m = int(input())
for i in range(m) :
    l, r = map(int, input().split())
    for elem in L[l - 1 : r] :
        print(elem)