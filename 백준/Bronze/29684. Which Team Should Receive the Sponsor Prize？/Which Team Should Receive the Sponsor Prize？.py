# 29684 Which Team Should Receive the Sponsor Prize?

while True :
    n = int(input())
    if n == 0 :
        break
    L = list(map(int, input().split()))
    for i in range(n) :
        L[i] = abs(L[i] - 2023)
    print(L.index(min(L)) + 1)