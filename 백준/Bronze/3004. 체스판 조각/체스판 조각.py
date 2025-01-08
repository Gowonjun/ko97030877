# 3004  체스판 조각

cnt = 1
N = int(input())
for i in range(N) :
    cnt += (i + 3) // 2
print(cnt)