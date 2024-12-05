# 15953 상금 헌터

T = int(input())
for _ in range(T) :
    hap = 0
    a, b = map(int, input().split())
    if a == 0 :
        hap += 0
    elif a == 1 :
        hap += 5000000
    elif a >= 2 and a <= 3 :
        hap += 3000000
    elif a >= 4 and a <= 6 :
        hap += 2000000
    elif a >= 7 and a <= 10 :
        hap += 500000
    elif a >= 11 and a <= 15 :
        hap += 300000
    elif a >= 16 and a <= 21 :
        hap += 100000
    if b == 0 :
        hap += 0
    elif b == 1 :
        hap += 5120000
    elif b >= 2 and b <= 3 :
        hap += 2560000
    elif b >= 4 and b <= 7 :
        hap += 1280000
    elif b >= 8 and b <= 15 :
        hap += 640000
    elif b >= 16 and b <= 31 :
        hap += 320000
    print(hap)