# 5073  삼각형과 세 변

while True :
    s = input()
    if s == '0 0 0' :
        break
    L = list(map(int, s.split()))
    L.sort()
    if L[0] + L[1] <= L[2] :
        print('Invalid')
    elif L[0] == L[1] and L[1] == L[2] :
        print('Equilateral')
    elif L[0] == L[1] or L[1] == L[2] :
        print('Isosceles')
    else :
        print('Scalene')