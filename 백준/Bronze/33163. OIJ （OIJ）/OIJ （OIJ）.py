# 33163 OIJ (OIJ)

N = int(input())
S = input()
L = []
for elem in S :
    if elem == 'J' :
        L.append('O')
    elif elem == 'O' :
        L.append('I')
    else :
        L.append('J')
print(''.join(L))