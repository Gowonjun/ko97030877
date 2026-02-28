# 35367 Snakey String

r, c = map(int, input().split())
L = [0] * c
for _ in range(r) :
    s = input()
    for i in range(c) :
        if s[i] != '.' :
            L[i] = s[i]
for elem in L :
    print(elem, end = '')