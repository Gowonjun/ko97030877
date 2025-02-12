# 27222 Штангист

hap = 0
n = int(input())
L = list(map(int, input().split()))
for i in range(n) :
    a, b = map(int, input().split())
    if L[i] == 1 :
        if b - a > 0 :
            hap += b - a
print(hap)