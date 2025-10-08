# 34447 Bad Directions

t = int(input())
for i in range(t) :
    k, n = input().split()
    k = int(k)
    L = list(map(int, n))
    #print(type(L[0]))
    for i in range(len(L)) :
        L[i] += k
    for j in range(len(L)) :
        print(str(L[j])[-1], end = '')
    print()