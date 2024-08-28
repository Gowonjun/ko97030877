# 2997  네 번째 수

L = list(map(int, input().split()))

L.sort()

if L[0] - L[1] == L[1] - L[2] :

    print(L[0] + (L[1] - L[2]))

else :

    if L[1] - L[0] == 2 * (L[2] - L[1]) :

        print(L[0] + (L[2] - L[1]))

    else :

        print(L[1] + (L[1] - L[0]))