# 11800 Tawla
T = int(input())
for i in range(T) :
    a, b = map(int, input().split())
    print('Case %d: ' % (i + 1), end = '')
    if a == 1 and b == 1 :
        print("Habb Yakk")
    elif a == 2 and b == 2 :
        print("Dobara")
    elif a == 3 and b == 3 :
        print("Dousa")
    elif a == 4 and b == 4 :
        print("Dorgy")
    elif a == 5 and b == 5 :
        print("Dabash")
    elif a == 6 and b == 6 :
        print("Dosh")
    else :
        if a + b == 11 :
            print("Sheesh Beesh")
        else :
            L = [a, b]
            L.sort(reverse = True)            
            for elem in L :
                if elem == 1 :
                    print("Yakk", end = ' ')
                elif elem == 2 :
                    print("Doh", end = ' ')
                elif elem == 3 :
                    print("Seh", end = ' ')
                elif elem == 4 :
                    print("Ghar", end = ' ')
                elif elem == 5 :
                    print("Bang", end = ' ')
                elif elem == 6 :
                    print("Sheesh", end = ' ')
            print()