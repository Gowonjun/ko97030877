L = []
LL = []
for i in range(4) :
    L.append(int(input()))
for i in range(2) :
    LL.append(int(input()))
L.sort(reverse=True) ; LL.sort(reverse=True)
print(L[0] + L[1] + L[2] + LL[0])