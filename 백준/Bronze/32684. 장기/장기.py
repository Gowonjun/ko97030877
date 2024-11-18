# 32684 장기

L = []
for i in range(2) :
    a, b, c, d, e, f = map(int, input().split())
    L.append(a * 13 + b * 7 + c * 5 + d * 3 + e * 3 + f * 2)
if L[0] > L[1] + 1.5 :
    print('cocjr0208')
else :
    print('ekwoo')