# 13484 Tarifa

X = int(input())
N = int(input())
hap = 0 
for i in range(N) :
    P = int(input())
    hap += P
print((N + 1) * X - hap)