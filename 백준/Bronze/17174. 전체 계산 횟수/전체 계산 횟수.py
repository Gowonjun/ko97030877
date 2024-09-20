N, M = map(int, input().split())
m = M
cnt = 0
a = 1
i = 0
while a :
    if N < pow(M, i) :
        a = 0
        break
    else :
        cnt += N // pow(M, i)
        i += 1

print(cnt)