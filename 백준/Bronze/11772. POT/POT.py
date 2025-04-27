# 11772 POT

hap = 0
N = int(input())
for i in range(N) :
    P = input()
    n = int(P[-1])
    a = int(P[0 : -1])
    hap += pow(a, n)
print(hap)