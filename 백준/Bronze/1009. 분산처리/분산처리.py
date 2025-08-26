# 1009  분산처리

import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T) :
    a, b = map(int, input().split())
    aa = a % 10
    if aa == 0 :
        print(10)
    elif aa == 1 or aa == 5 or aa == 6 :
        print(aa)
    else :
        if aa == 4 or aa == 9 :
            bb = b % 2
            if bb == 0 :
                print(aa * aa % 10)
            else :
                print(aa)
        else :
            bb = b % 4
            if bb == 0 :
                print(pow(aa, 4) % 10)
            else :
                print(pow(aa, bb) % 10)