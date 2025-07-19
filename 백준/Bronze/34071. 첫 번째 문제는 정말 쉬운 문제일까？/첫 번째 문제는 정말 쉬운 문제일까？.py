# 34071 첫 번째 문제는 정말 쉬운 문제일까?

L = []
N = int(input())
for i in range(N) :
    X = int(input())
    L.append(X)
if L[0] == max(L) :
    print('hard')
elif L[0] == min(L) :
    print('ez')
else :
    print('?')