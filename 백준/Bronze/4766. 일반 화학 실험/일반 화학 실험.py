pre = -273.15   # pre = previous
while True :
    f = float(input())
    if f == 999 :
        break
    else :
        if pre == -273.15 :
            pass
        else :
            print('%.2f' % (f - pre))
        pre = f