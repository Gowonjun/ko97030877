# 16431 베시와 데이지

Br, Bc = map(int, input().split())
Dr, Dc = map(int, input().split())
Jr, Jc = map(int, input().split())

D = abs(Dr - Jr) + abs(Dc - Jc)
Bx = abs(Br - Jr)
By = abs(Bc - Jc)
B = Bx + By - min(Bx, By)
#print(D, B)
if D < B :
    print('daisy')
elif D > B :
    print('bessie')
else :
    print('tie')