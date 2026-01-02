# 34758 KUPC에 어서 오세요

X, Y = map(int, input().split())
N = int(input())
for i in range(N) :
    cnt = 0
    x, y = map(int, input().split())
    if x != X :
        cnt += 1
    if y != Y :
        cnt += 1
    if x == X and y == Y :
        cnt = 0
    print(cnt - 1)