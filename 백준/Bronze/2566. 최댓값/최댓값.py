L = []
for _ in range(9) :
    L.append(list(map(int, input().split())))
for i in range(9) :
    for j in range(9) :
        if L[i][j] == max(map(max, L)) :
            print(max(map(max, L)))
            print(i + 1, j + 1)