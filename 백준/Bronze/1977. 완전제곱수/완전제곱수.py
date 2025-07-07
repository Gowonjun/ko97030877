# 1977  완전제곱수

M = int(input())
N = int(input())
L = []
for i in range(M, N + 1) :
    if i ** 0.5 == int(i ** 0.5) :
        L.append(i)
if len(L) == 0 :
    print(-1)
else :
    print(sum(L))
    print(min(L))