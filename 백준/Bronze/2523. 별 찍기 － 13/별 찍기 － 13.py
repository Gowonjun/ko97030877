N = int(input())
s = '*'
for i in range(1, N + 1) :
    print(i * s)
for i in range(N - 1, 0, -1) :
    print(i * s)