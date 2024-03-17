N = int(input())
fac = 1
cnt = 1
for i in range(N) :
    fac *= cnt
    cnt += 1
print(int(fac / 3628800) * 6)