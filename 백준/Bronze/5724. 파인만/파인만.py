while True :
    N = int(input())
    if N == 0 :
        break
    hap = 0
    for i in range(1, N + 1) :
        hap += pow(i, 2)
    print(hap)