i = 0
N = int(input())

for i in range(0, N, 1) :
    i += 1
    space = N - i
    star = i
    print("%s%s" % (' ' * space, '*' * star))