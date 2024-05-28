from math import pi

n = int(input())
for i in range(n) :
    A1, P1 = map(int, input().split())
    R1, P2 = map(int, input().split())
    P = P1 / A1
    C = P2 / (pi * pow(R1, 2))
    if P > C :
        print('Whole pizza')
    else :
        print('Slice of pizza')