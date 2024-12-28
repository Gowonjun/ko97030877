# 32941 왜 맘대로 예약하냐고

flag = 1
T, X = map(int, input().split())
N = int(input())
for _ in range(N) :
    K = int(input())
    L = list(map(int, input().split()))
    if X not in L :
        flag = 0
if flag == 1 :
    print('YES')
else :
    print('NO')