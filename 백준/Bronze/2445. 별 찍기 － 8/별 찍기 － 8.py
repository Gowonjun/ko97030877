N = int(input())
for i in range(N) :
    print('*' * (i + 1), end = '')
    print(' ' * (2 * N - 2 * (i + 1)), end = '')
    print('*' * (i + 1))
for i in range(N - 1) :
    print('*' * (N - i - 1), end = '')
    print(' ' * (2 * i + 2), end = '')
    print('*' * (N - i - 1))