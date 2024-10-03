N = int(input())
cnt = 0
max_cnt = 0
L = list(map(int, input().split()))
for i in range(N) :
    if L[i] >= 1 :
        cnt += 1
        if cnt > max_cnt :
            max_cnt = cnt
    else :
        cnt = 0
print(max_cnt)