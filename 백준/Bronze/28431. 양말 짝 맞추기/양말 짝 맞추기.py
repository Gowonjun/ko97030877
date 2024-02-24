L = []
for i in range(5) :
    a = int(input())
    L.append(a)
for elem in L :
    if L.count(elem) % 2 != 0 :
        print(elem)
        break
    else :
        continue