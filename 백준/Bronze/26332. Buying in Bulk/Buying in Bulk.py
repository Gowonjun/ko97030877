n = int(input())
for i in range(n) :
    c, p = map(int, input().split())
    print(c, p)
    if c == 1 :
        print(p)
    else :
        print((p - 2) * c + 2)