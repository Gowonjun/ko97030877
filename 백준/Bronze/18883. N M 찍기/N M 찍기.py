# 18883 N M 찍기

#import sys
#s = sys.stdin.readline()
s = input()
N, M = map(int, s.split())
cnt = 1
for i in range(N) :
    L = []
    for j in range(M) :
        L.append(str(cnt))
        cnt += 1
    s = ' '.join(L)
    print(s)