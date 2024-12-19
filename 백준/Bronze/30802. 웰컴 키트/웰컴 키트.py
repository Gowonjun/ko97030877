# 30802 웰컴 키트

import math

N = int(input())
L = list(map(int, input().split()))
T, P = map(int, input().split())
hap = 0
for elem in L :
    if elem % T == 0 :
        hap += elem // T
    else :
        hap += math.ceil(elem / T) 
print(hap)
print(N // P, N % P)