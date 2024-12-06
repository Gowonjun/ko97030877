# 1284  집 주소

while True :
    N = int(input())
    if N == 0 :
        break
    else :
        hap = 0
        N = str(N)
        for elem in N :
            if elem == '1' :
                hap += 2
            elif elem == '0' :
                hap += 4
            else :
                hap += 3
        hap += len(N) + 1
        print(hap)