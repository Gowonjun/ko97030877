# 4583  거울상
# 백업
while True :
    s = input()
    if s == '#' :
        break
    s = s[::-1]
    L = list(s)
    flag = 0
    for i in range(len(L)) :
        if L[i] == 'b' :
            L[i] = 'd'
        elif L[i] == 'd' :
            L[i] = 'b'
        elif L[i] == 'p' :
            L[i] = 'q'
        elif L[i] == 'q' :
            L[i] = 'p'
        elif L[i] in 'iovwx' :
            continue
        else :
            flag = 1
            break
    if flag == 1 :
        print('INVALID')
    else :
        print(''.join(L))