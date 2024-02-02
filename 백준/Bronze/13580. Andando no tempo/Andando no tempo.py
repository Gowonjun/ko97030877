L = list(map(int, input().split()))
L.sort()
if L[0] + L[1] == L[2] :
    print('S')
else :
    if L[0] == L[1] or L[1] == L[2] :
        print('S')
    else :
        print('N')