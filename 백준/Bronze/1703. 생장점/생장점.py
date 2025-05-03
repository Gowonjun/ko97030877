# 1703  생장점

while True :
    res = 1
    s = input()
    if s == '0' :
        break
    L = list(map(int, s.split()))
    for i in range(1, L[0] * 2 + 1) :
        if i % 2 == 1 :
            res *= L[i]
        else :
            res -= L[i]
    print(res)