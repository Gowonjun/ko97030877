# 1864  문어 숫자

while True :
    s = input()
    if s == '#' :
        break
    L = list(s)
    LL = []
    for elem in L :
        if elem == '-' :
            LL.append(0)
        elif elem == '\\' :
            LL.append(1)
        elif elem == '(' :
            LL.append(2)
        elif elem == '@' :
            LL.append(3)
        elif elem == '?' :
            LL.append(4)
        elif elem == '>' :
            LL.append(5)
        elif elem == '&' :
            LL.append(6)
        elif elem == '%' :
            LL.append(7)
        elif elem == '/' :
            LL.append(-1)
    LL.reverse()
    #print(LL)
    hap = 0    
    for i in range(len(L)) :
        hap += LL[i] * pow(8, i)
    print(hap)