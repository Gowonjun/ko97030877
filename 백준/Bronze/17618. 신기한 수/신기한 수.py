cnt = 0

N = int(input())
for i in range(1, N + 1) :
    s = str(i)
    L = list(s)
    if i % sum(map(int, L)) == 0 :
        cnt += 1
print(cnt)