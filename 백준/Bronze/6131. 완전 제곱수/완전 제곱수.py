# 6131  완전 제곱수

cnt = 0
N = int(input())
for A in range(1, N + 1) :
    for B in range(1, N + 1) :
        if A * A - B * B == N :
            cnt += 1
print(cnt)