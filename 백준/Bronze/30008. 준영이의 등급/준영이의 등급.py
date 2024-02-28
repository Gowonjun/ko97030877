N, K = map(int, input().split())
L = list(map(int, input().split()))
for elem in L :
    if 0 <= 100 * elem // N <= 4 :
        print(1)
    elif 100 * elem // N <= 11 :
        print(2)
    elif 100 * elem // N <= 23 :
        print(3)
    elif 100 * elem // N <= 40 :
        print(4)
    elif 100 * elem // N <= 60 :
        print(5)
    elif 100 * elem // N <= 77 :
        print(6)
    elif 100 * elem // N <= 89 :
        print(7)
    elif 100 * elem // N <= 96 :
        print(8)
    else :
        print(9)