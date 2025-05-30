# 13698 Hawk eyes

S = input()
L = ['s', 0, 0, 'b']
for elem in S :
    if elem == 'A' :
        temp = L[0]
        L[0] = L[1]
        L[1] = temp
    elif elem == 'B' :
        temp = L[0]
        L[0] = L[2]
        L[2] = temp
    elif elem == 'C' :
        temp = L[0]
        L[0] = L[3]
        L[3] = temp
    elif elem == 'D' :
        temp = L[1]
        L[1] = L[2]
        L[2] = temp
    elif elem == 'E' :
        temp = L[1]
        L[1] = L[3]
        L[3] = temp
    else :
        temp = L[2]
        L[2] = L[3]
        L[3] = temp
    #print(L)
print(L.index('s') + 1)
print(L.index('b') + 1)