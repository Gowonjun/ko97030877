# 23794 골뱅이 찍기 - 정사각형

N = int(input())
print('@' * (N + 2))
for i in range(N) :
    print('@', end = '')
    print(' ' * N, end = '')
    print('@')
print('@' * (N + 2))