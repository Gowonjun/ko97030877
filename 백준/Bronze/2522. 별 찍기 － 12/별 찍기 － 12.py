# 2522  별 찍기 - 12

N = int(input())
for i in range(N) :
    print(' ' * (N - i - 1), end = '')
    print('*' * (i + 1))
for i in range(N - 1) :
    print(' ' * (i + 1), end = '')
    print('*' * (N - i - 1))