# 8741  이진수 합

#from decimal import Decimal

k = int(input())
a = pow(2, k)

hap = (1 + a - 1) * (a - 1) // 2
#print(hap)
print(bin(hap)[2 : ])