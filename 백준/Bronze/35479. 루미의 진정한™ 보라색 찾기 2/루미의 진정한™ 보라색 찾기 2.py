# 35479 루미의 진정한™ 보라색 찾기 2

R, G, B = map(int,input().split())
Rp = R / 255
Gp = G / 255
Bp = B / 255
K = 1 - max(Rp, Gp, Bp)
if K == 1 :
    C = 0
    M = 0
    Y = 0
else :
    C = (1 - Rp - K) / (1 - K)
    M = (1 - Gp - K) / (1 - K)
    Y = (1 - Bp - K) / (1 - K)
print(C, M, Y, K)