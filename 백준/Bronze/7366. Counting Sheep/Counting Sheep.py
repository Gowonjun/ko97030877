# 7366  Counting Sheep

n = int(input())
for i in range(n) :
    cnt = 0
    m = int(input())
    L = list(input().split())
    for elem in L :
        if elem == 'sheep' :
            cnt += 1
    print('Case %d: This list contains %d sheep.' % (i + 1, cnt))
    print()