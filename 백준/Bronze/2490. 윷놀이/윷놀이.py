# 2490  윷놀이

for i in range(3) :
    L = list(map(int, input().split()))
    if sum(L) == 3 :
        print('A')
    elif sum(L) == 2 :
        print('B')
    elif sum(L) == 1 :
        print('C')
    elif sum(L) == 0 :
        print('D')
    else :
        print('E')