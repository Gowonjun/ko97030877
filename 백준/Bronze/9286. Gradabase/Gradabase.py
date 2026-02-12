# 9286  Gradabase

n = int(input())
for i in range(n) :
    print('Case %d:' % (i + 1))
    m = int(input())
    L = []
    for j in range(m) :
        L.append(int(input()))
    for elem in L :
        res = elem + 1
        if res <= 6 :
            print(res)