# 25965 미션 도네이션

N = int(input())
for _ in range(N) :
    m = 0   # money
    L = []
    M = int(input())
    for i in range(M) :
        L.append(input())
    k, d, a = map(int, input().split())
    for elem in L :
        K, D, A = map(int, elem.split())
        hap = k * K - d * D + a * A
        if hap < 0 :
            hap = 0
        m += hap
    print(m)