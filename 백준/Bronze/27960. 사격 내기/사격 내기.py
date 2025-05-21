# 27960 사격 내기

SA, SB = map(int, input().split())
def b(n) :  # bin
    L = []
    for i in range(9, -1, -1) :
        a = pow(2, i)
        L.append(n // a)
        if n // a == 1 : 
            n -= a
    return L
LA = b(SA)
LB = b(SB)
#print(LA, LB, bin(SA), bin(SB))
LA.reverse()
LB.reverse()
hap = 0
for i in range(10) :
    if LA[i] != LB[i] :
        hap += pow(2, i)
print(hap)