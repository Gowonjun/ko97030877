A, B = map(int,input().split())
K, X = map(int,input().split())

L = K - X
H = K + X
LL = max(L,A)
HH = min(H,B)
res = HH - LL + 1
if res <= 0 :
    print('IMPOSSIBLE')
else :
    print(res)