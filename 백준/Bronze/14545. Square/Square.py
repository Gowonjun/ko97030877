P = int(input())
for i in range(P) :
    l = int(input())
    hap = 0
    for j in range(1, l + 1) :
        hap += pow(j, 2)
    print(hap)