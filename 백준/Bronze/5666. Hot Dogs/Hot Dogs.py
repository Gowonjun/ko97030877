while True :
    try :
        H, P = map(int, input().split())
        res = H / P
        print('%.2f' % res)
    except :
        break