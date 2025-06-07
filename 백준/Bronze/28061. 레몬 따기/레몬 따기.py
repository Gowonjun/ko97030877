# 28061 레몬 따기

cnt = 0
N = int(input())
L = list(map(int, input().split()))
for i in range(N) :
    a = L[i] - N + i
    if cnt < a :
        cnt = a
    #print(a, cnt)
print(cnt)