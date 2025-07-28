# 10696 Prof. Ossama

T = int(input())
for i in range(1, T + 1) :
    N, X = map(int, input().split())
    print('Case %d: %d' % (i, N % X))