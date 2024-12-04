# 9325  얼마?

T = int(input())
for _ in range(T) :
    hap = 0
    s = int(input())
    hap += s
    n = int(input())
    for _ in range(n) :
        a, b = map(int, input().split())
        hap += a * b
    print(hap)