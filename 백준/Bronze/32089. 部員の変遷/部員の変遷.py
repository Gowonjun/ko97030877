while True :
    m = 0   # max
    n = int(input())
    if n == 0 :
        break
    L = list(map(int, input().split()))
    for i in range(n - 2) :
        hap = L[i] + L[i + 1] + L[i + 2]
        if hap > m :
            m = hap
    print(m)