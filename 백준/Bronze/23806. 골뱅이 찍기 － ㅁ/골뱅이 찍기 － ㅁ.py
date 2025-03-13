# 23806 골뱅이 찍기 - ㅁ

N = int(input())
for i in range(N) :
    print('@' * N * 5)
for i in range(N * 3) :
    print('@' * N, end = '')
    print(' ' * N * 3, end = '')
    print('@' * N)
for i in range(N) :
    print('@' * N * 5)