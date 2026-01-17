# 20282 Game Show!

L = [100]
C = int(input())
cnt = 100
for _ in range(C) :
    V = int(input())
    cnt += V
    L.append(cnt)
print(max(L))