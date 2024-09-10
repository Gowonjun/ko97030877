T = int(input())
for i in range(T) :
    x, y = map(int, input().split())
    if x <= 23 and y <= 59 :
        print('Yes', end = ' ')
    else :
        print('No', end = ' ')
    
    if x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12 :
        if  1 <= y <= 31 :
            print('Yes')
        else :
            print('No')
    elif x == 4 or x == 6 or x == 9 or x == 11 :
        if 1 <= y and y <= 30 :
            print('Yes')
        else :
            print('No')
    elif x == 2 :
        if 1 <= y and y <= 29 :
            print('Yes')
        else :
            print('No')
    else :
        print('No')