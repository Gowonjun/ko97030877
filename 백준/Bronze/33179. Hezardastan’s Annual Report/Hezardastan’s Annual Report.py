# 33179

n = int(input())
L = list(map(int, input().split()))
hap = 0
for elem in L :
    if elem % 2 == 0 :
        hap += elem // 2
    else :
        hap += elem // 2 + 1
print(hap)