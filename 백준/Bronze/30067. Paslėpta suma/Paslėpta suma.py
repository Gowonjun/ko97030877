L = []
for i in range(10) :
    L.append(int(input()))
for elem in L :
    hap = sum(L) - elem
    if hap == elem :
        print(elem)
        break