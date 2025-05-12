# 9713  Sum of Odd Sequence

T = int(input())
for _ in range(T) :
    N = int(input())
    hap = 0
    if N % 2 == 1 :
        for i in range(1, N + 1, 2) :
            hap += i
        print(hap)