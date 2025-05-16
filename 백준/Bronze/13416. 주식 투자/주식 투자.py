# 13416 주식 투자

T = int(input())
for _ in range(T) :
    hap = 0
    N = int(input())
    for _ in range(N) :
        L = list(map(int, input().split()))
        if max(L) > 0 :
            hap += max(L)
    print(hap)