# 23530 Not A + B

T = int(input())
for i in range(T) :
    a, b = input().split()
    s = a + b
    n = int(s)
    if n > 50 :
        print(1)
    else :
        print(n)
