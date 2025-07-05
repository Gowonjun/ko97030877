# 6845  Federal Voting Age

n = int(input())
for i in range(n) :
    y, m, d = map(int, input().split())
    if y < 1989 :
        print('Yes')
    elif y > 1989 :
        print('No')
    else :
        if m < 2 :
            print('Yes')
        elif m > 2 :
            print('No')
        else :
            if d <= 27 :
                print('Yes')
            else :
                print('No')