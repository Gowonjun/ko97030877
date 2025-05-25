# 4388  받아올림

while True :
    cnt = 0
    a, b = map(int, input().split())
    if a == 0 and b == 0 :
        break
    a = str(a)
    b = str(b)
    if len(a) < len(b) :
        for _ in range(len(b) - len(a)) :
            a = '0' + a
    else :
        for _ in range(len(a) - len(b)) :
            b = '0' + b
    add = 0
    for i in range(len(a) - 1, -1, -1) :
        if int(a[i]) + int(b[i]) + add >= 10 :
            add = 1
            cnt += 1
        else :
            add = 0
    print(cnt)