# 23809 골뱅이 찍기 - 돌아간 ㅈ

N = int(input())

g = '@'
b = ' '

for i in range(N) :
    print(g * N, end = '')
    print(b * 3 * N, end = '')
    print(g * N)
for i in range(N) :
    print(g * N, end = '')
    print(b * 2 * N, end = '')
    print(g * N)
for i in range(N) :
    print(g * 3 * N)
for i in range(N) :
    print(g * N, end = '')
    print(b * 2 * N, end = '')
    print(g * N)
for i in range(N) :
    print(g * N, end = '')
    print(b * 3 * N, end = '')
    print(g * N)