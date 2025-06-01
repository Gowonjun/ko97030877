# 11319 Count Me In

V = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
T = int(input())
for i in range(T) :
    c = 0
    v = 0
    s = input()
    for elem in s :
        if elem in V :
            v += 1
        elif elem == ' ' :
            continue
        else :
            c += 1
    print(c, v)