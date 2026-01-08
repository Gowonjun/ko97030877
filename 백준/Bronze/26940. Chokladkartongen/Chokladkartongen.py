# 26940 Chokladkartongen

N = int(input())
L = list(map(int, input().split()))
cnt = 0
for i in range(N - 1) :
    if L[i + 1] - L[i] > 0 :
        cnt += 1
print(cnt)