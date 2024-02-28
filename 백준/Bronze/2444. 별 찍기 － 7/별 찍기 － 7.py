cnt = 0
b = ' '
s = '*'
N = int(input())
while cnt < N :
    print(b * (N - 1 - cnt), end= '')
    print(s * (1 + 2 * cnt))
    cnt += 1
cnt -= 1
while cnt >= -1 :
    cnt -= 1
    print(b * (N - 1 - cnt), end= '')
    print(s * (1 + 2 * cnt))