# 10409 서버

n, T = map(int, input().split())
L = list(map(int, input().split()))
flag = 0
for i in range(len(L)) :
    if T < L[i] :
        print(i)
        flag = 1
        break
    else :
        T -= L[i]
if flag == 0 :
    print(i + 1)