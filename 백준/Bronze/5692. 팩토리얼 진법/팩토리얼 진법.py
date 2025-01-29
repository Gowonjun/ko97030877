# 5692  팩토리얼 진법

import sys

def fac(a) :    # fac = factorial
    if a == 0 :
        return 1
    else :
        for i in range(1, a) :
            a *= i
        return a

while True :
    s = sys.stdin.readline().strip()
    if s == '0' :
        break
    L = list(s)
    for i in range(len(L)) :
        #print(len(L) - i)
        L[i] = fac((len(L) - i)) * int(L[i])
    print(sum(L))