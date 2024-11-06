# 10991 별 찍기 - 16

s = '*' # star
N = int(input())
for i in range(N) :
    print(' ' * (N - i - 1), end = '')
    for j in range(i) :
        print(s, end = '')
        print(' ', end = '')
    print(s)