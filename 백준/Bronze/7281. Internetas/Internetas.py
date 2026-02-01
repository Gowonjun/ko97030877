# 7281  Internetas

N = int(input())
L = []
for _ in range(N) :
    T, M = map(int, input().split())
    if M == 0 :
        continue
    else :
        L.append(T)

LL = []
for i in range(len(L) - 1) :
    LL.append(L[i + 1] - L[i])
print(max(LL))