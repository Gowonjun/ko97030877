# 11131 Balancing Weights

T = int(input())
for i in range(T) :
    N = int(input())
    L = list(map(int, input().split()))
    hap = sum(L)
    if hap > 0 :
        print('Right')
    elif hap == 0 :
        print('Equilibrium')
    else :
        print('Left')