N = int(input())
for i in range(N) :
    print(' ' * i, end = '')
    print('*' * (2 * N - 2 * i -1))