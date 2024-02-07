N = int(input())
A, B, C = map(int, input().split())
cnt = 0
if A < N :
    cnt += A
else :
    cnt += N
if B < N :
    cnt += B
else :
    cnt += N
if C < N :
    cnt += C
else :
    cnt += N
print(cnt)