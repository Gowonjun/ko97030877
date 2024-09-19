T = int(input())
for i in range(T) :
    d, n, s, p = map(int, input().split())
    j = n * s
    b = d + n * p
    if j > b :
        print('parallelize')
    elif j < b :
        print('do not parallelize')
    else :
        print('does not matter')