# 14682 Shifty Sum

N = int(input())
k = int(input())
hap = 0
for i in range(k + 1) :
    a = N * pow(10, i)
    hap += a
    #print(a)
print(hap)