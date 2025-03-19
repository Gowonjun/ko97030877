# 2991  사나운 개

cntP, cntM, cntN = 0, 0, 0
A, B, C, D = map(int, input().split())
P, M, N = map(int, input().split())
if 0 < P % (A + B) <= A :
    cntP += 1
if 0 < P % (C + D) <= C :
    cntP += 1
if 0 < M % (A + B) <= A :
    cntM += 1
if 0 < M % (C + D) <= C :
    cntM += 1
if 0 < N % (A + B) <= A :
    cntN += 1
if 0 < N % (C + D) <= C :
    cntN += 1
print('%d\n%d\n%d' % (cntP, cntM, cntN))
#print(P % (A + B), P % (C + D), M % (A + B), M % (C + D), N % (A + B), N % (C + D))