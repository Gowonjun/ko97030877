# 9366  삼각형 분류

T = int(input())
for i in range(T) :
    L = list(map(int, input().split()))
    L.sort()
    if L[0] + L[1] <= L[2] :
        s = 'invalid!'
    elif L[0] == L[1] and L[1] == L[2] :
        s = 'equilateral'
    elif L[0] == L[1] :
        s = 'isosceles'
    elif L[1] == L[2] :
        s = 'isosceles'
    elif L[2] == L[0] :
        s = 'isosceles'
    else :
        s = 'scalene'
    print('Case #%d: %s' % (i + 1, s))