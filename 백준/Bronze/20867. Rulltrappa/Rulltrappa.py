M, S, G = map(int, input().split())
A, B = map(float, input().split())
L, R = map(int, input().split())
l = L / A ; r = R / B
l += M / G ; r += M / S
if l > r :
    print('latmask')
else :
    print('friskus')