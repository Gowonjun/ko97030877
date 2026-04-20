# 6030  Scavenger Hunt

P, Q = map(int, input().split())

def factor(n) :
    L = []
    for i in range(1, n + 1) :
        if n % i == 0 :
            L.append(i)
    return L
L_P = factor(P)
L_Q = factor(Q)
for p in L_P :
    for q in L_Q :
        print(p, q)