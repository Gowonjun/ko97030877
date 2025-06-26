# 5949  Adding Commas

L = list(input())

i = -3
while True :
    L.insert(i, ',')
    length = len(L)
    i -= 4
    if i < (-1) * length :
        break
if L[0] == ',' :
    del L[0]
print(''.join(L))