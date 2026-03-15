# 20877 Minigolf

N = int(input())
L = list(map(int, input().split()))
hap = 0
for i in range(N) :
    a = L[i]
    if a > 7 :
        a = 7
    if i % 2 == 0 :
        hap += a - 2
    else :
        hap += a - 3
print(hap)