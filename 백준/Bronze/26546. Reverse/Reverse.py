n = int(input())
for i in range(n) :
    L = []
    a, b, c = map(str, input().split())
    b = int(b)
    c = int(c)
    L = list(a)
    del L[b : c]
    s = ''.join(L)
    print(s)