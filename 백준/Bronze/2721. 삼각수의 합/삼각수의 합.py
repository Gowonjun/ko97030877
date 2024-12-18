# 2721  삼각수의 합

def T(n) :
    hap = 0
    for i in range(1, n + 1) :
        hap += i
    return hap

t = int(input())
for _ in range(t) :
    N = int(input())
    hap = 0
    for i in range(1, N + 1) :
        hap += i * T(i + 1)
    print(hap)