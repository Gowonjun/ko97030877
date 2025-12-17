# 25814 Heavy Numbers

def Weight(n) :
    L = list(str(n))
    for i in range(len(L)) :
        L[i] = int(L[i])
    sum_n = sum(L)
    Wn = len(str(n)) * sum_n
    return Wn

a, b = map(int, input().split())

'''
La = list(str(a))
for i in range(len(La)) :
    La[i] = int(La[i])
sum_a = sum(La)
Wa = len(str(a)) * sum_a
print(Wa)
'''

if Weight(a) > Weight(b) :
    print(1)
elif Weight(a) < Weight(b) :
    print(2)
else :
    print(0)