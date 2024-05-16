cnt = 0
n, k = map(int, input().split())
save = 0
for i in range(n) :
    s = input()
    if s == 'save' :
        save = cnt
        print(cnt)
    elif s == 'load' :
        if save == 0 :
            cnt = 0
        else :
            cnt = save
        print(cnt)
    elif s == 'shoot' :
        if cnt == 0 :
            pass
        else :
            cnt -= 1
        print(cnt)
    elif s ==  'ammo' :
        cnt += k
        print(cnt)
    else :
        pass