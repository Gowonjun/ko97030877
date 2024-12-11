# 3047  ABC

# A < B < C

L = list(map(int, input().split()))
L.sort()
s = input()
for elem in s :
    if elem == 'A' :
        print(L[0], end = ' ')
    elif elem == 'B' :
        print(L[1], end = ' ')
    else :
        print(L[2], end = ' ')