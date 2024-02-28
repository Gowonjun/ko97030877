fac = 1
N = int(input())
if N == 0 :
    print(1)
else :
    for i in range(1, N + 1) :
        fac *= i
    print(fac)