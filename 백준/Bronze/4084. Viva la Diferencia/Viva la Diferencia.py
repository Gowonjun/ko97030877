# 4084  Viva la Diferencia

while True :
    a, b, c, d = map(int, input().split())
    if a == b == c == d == 0 :
        break
    i = 0
    while True :
        if a == b and b == c and c == d :
            print(i)
            break
        else :
            tmp = a
            a = abs(a - b)
            b = abs(b - c)
            c = abs(c - d)
            d = abs(d - tmp)
            i += 1
            #print(a, b, c, d)