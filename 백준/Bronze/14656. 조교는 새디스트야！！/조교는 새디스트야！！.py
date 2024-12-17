# 14656 조교는 새디스트야!!

cnt = 0
N = int(input())
L = list(map(int, input().split()))
for i in range(N) :
    if L[i] != i + 1 :
        cnt += 1
print(cnt)