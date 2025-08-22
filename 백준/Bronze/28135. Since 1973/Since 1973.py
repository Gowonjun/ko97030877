# 28135 Since 1973

N = int(input())
cnt = 0
for i in range(1, N) :
    cnt += 1
    if '50' in str(i) :
        cnt += 1
cnt += 1
print(cnt)