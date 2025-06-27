# 5356  Triangles

T = int(input())
for _ in range(T) :
    n, s = input().split()
    n = int(n)
    s = ord(s)
    for i in range(n) :
        print((i + 1) * chr(s))
        s += 1
        if s > ord('Z') :
            s = ord('A')
    print()