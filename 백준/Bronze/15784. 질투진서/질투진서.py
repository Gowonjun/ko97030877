# 15784 질투진서

N, a, b = map(int, input().split())
LL = []
flag = 0

for i in range(N) :
    L = []
    L = (list(map(int, input().split())))
    LL.append(L)

# LL = [[10, 2, 3, 24, 4], [21, 4, 5, 12, 1], [24, 52, 4, 2, 2], [2, 4, 3, 2, 32], [1, 4, 32, 2, 4]]
# print(LL)

for i in range(N) :
    # print(LL[i][b - 1])
    # print(LL[a - 1][b - 1])
    if LL[i][b - 1] > LL[a - 1][b - 1] :
        flag = 1
for j in range(N) :
    if LL[a - 1][j] > LL[a - 1][b - 1] :
        flag = 1
if flag == 0 :
    print('HAPPY')
else :
    print('ANGRY')