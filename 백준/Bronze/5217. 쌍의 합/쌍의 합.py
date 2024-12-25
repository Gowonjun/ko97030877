# 5217  쌍의 합

T = int(input())
for _ in range(T) :
    n = int(input())
    s = 'Pairs for '
    s = s + str(n) + ':'
    for i in range(n // 2) :
        a = i + 1
        b = n - (i + 1)
        if a != b :
            s = s + ' ' + str(a) + ' ' + str(b) + ','
    if s[-1] == ',' :
        s = s[:-1]
    print(s)