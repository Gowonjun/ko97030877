L = []
for i in range(3) :
    p, w = map(int, input().split())    # p = price, w = weight
    p = p * 10
    if p >= 5000 :
        p -= 500
    g = w / p
    L.append(g)
if max(L) == L[0] :
    print('S')
elif max(L) == L[1] :
    print('N')
else :
    print('U')