# 1547  공

cnt = 1
M = int(input())
for i in range(M) :
    X, Y = map(int, input().split())
    if cnt == X :
        cnt = Y
    elif cnt == Y :
        cnt = X
print(cnt)