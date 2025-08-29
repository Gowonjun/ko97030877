# 2145  숫자 놀이

while True :
    s = input()
    if s == '0' :
        break
    else :
        while True :
            if len(s) <= 1 :
                break
            else :
                hap = 0
                for elem in s :
                    hap += int(elem)
                s = str(hap)
        print(s)