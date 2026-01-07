# 35097 2025

while True :
    n = int(input())
    if n == 0 :
        break
    hap = 0
    for i in range(1, n + 1) :
        for j in range(1, n + 1) :
            hap += i * j
    print(hap)