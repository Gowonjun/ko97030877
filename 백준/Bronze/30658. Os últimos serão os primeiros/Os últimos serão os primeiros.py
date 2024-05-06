while True :    
    n = int(input())
    if n == 0 :
        break
    L = []
    for i in range(n) :
        L.append(int(input()))
    L.reverse()
    for elem in L :
        print(elem)
    print(0)