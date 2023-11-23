N = int(input())
hap = 0

for i in range(N) :
    a, b = 0, 0
    a, b = map(int, input().split())
    if a == 136 :
        hap += 1000
    elif a == 142 :
        hap += 5000
    elif a == 148 :
        hap += 10000
    else :
        hap += 50000
print(hap)