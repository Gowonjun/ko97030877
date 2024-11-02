# 2576  홀수

L = []
for _ in range(7) :
    n = int(input())
    if n % 2 == 1 :
        L.append(n)
if len(L) == 0 :
    print(-1)
else :
    print(sum(L))
    print(min(L))