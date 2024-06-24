N = int(input())
s = '*'
b = ' '
if N == 1 :
    print(s)
else : 
    print(b * (N - 1) + s)
    for i in range(N - 2) :
        print(b * (N - 1 - (i + 1)) + s + b * (2 * i + 1) + s)
    print(s * (2 * N - 1))