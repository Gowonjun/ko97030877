# 27159 노 땡스!

hap = 0
N = int(input())
L = list(map(int, input().split()))
for i in range(N) :
    if i == 0 :
        hap += L[i]
    else :
        if L[i] - 1 != L[i - 1] :
            hap += L[i]
print(hap)