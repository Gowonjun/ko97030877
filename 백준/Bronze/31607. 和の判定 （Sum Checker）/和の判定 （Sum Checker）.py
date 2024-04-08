L = []
for i in range(3) :
    L.append(int(input()))
L.sort()
if L[0] + L[1] == L[2] :
    print(1)
else :
    print(0)