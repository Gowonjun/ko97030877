# 18856 피드백

N = int(input())
L = [1, 2]
sieve = []
i = 3
while True :
    flag = 0
    for j in range(2, i) :
        if i % j == 0 :
            flag = 1
    if flag == 0 :
        L.append(i)
    i += 1
    if len(L) == N :
        break
L = list(map(str, L))
print(N)
print(' '.join(L))