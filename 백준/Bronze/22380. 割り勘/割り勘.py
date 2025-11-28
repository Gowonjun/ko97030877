# 22380 割り勘

while True :
    N, M = map(int, input().split())
    if N == 0 and M == 0 :
        break
    L = list(map(int, input().split()))
    a = M // N
    hap = 0
    for elem in L :
        if elem >= a :
            hap += a
        else :
            hap += elem
    print(hap)