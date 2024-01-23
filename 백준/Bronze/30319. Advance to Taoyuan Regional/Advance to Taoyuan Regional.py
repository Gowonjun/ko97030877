YYYY, MM, DD = map(int, input().split('-'))
if MM < 9 :
    print('GOOD')
else :
    if MM > 9 :
        print('TOO LATE')
    else :
        if DD <= 16 :
            print('GOOD')
        else :
            print('TOO LATE')