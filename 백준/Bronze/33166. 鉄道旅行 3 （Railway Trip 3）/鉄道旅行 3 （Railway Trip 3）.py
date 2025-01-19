# 33166 철도 여행 3 (Railway Trip 3)

P, Q = map(int, input().split())
A, B = map(int, input().split())
if P > Q :
    print(Q * A)    
else :
    print(P * A + (Q - P) * B)