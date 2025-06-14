# 13871 Farm robot

n = 1
cnt = 0
N, C, S = map(int, input().split())
L = list(map(int, input().split()))

if S == 1 :
    cnt = 1
for elem in L :
    n += elem
    if n > N :
        n = 1
    elif n < 1 :
        n = N
    if n == S :
        cnt += 1
    #print(n)
print(cnt)