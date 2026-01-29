# 7181  Mõttemeister

s = input()
N = int(input())
for _ in range(N) :
    a = input()
    A = 0
    B = 0
    for i in range(len(a)) :
        if a[i] in s :
            A += 1
        if a[i] == s[i] :
            B += 1
    print(A, B)