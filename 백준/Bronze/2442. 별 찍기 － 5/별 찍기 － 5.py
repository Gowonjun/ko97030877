N = int(input())
s = '*'
for i in range(1, N + 1) :
    print((N - i) * ' ' + (2 * i - 1) * s)