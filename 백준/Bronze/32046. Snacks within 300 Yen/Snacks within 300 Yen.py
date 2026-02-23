# 32046 Snacks within 300 Yen
while True :
    n = int(input())
    if n == 0 :
        break
    L = list(map(int, input().split()))
    hap = 0
    for elem in L :
        hap += elem
        if hap > 300 :
            hap -= elem
    print(hap)