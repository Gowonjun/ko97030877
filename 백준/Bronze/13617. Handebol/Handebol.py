# 13617 Handebol

cnt = 0
N, M = map(int, input().split())
for i in range(N) :
    L = list(map(int, input().split()))
    if min(L) != 0 :
        cnt += 1
print(cnt)