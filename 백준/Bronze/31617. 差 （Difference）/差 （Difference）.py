# 31617 差 (Difference)

K = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

cnt = 0

for elem in A :
    cnt += B.count(elem + K)

print(cnt)