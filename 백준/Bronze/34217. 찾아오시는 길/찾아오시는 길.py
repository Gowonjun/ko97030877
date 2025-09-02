# 34217 찾아오시는 길

A, B = map(int, input().split())
C, D = map(int, input().split())
H = A + C
Y = B + D
if H > Y :
    print('Yongdap')
elif H < Y :
    print('Hanyang Univ.')
else :
    print('Either')