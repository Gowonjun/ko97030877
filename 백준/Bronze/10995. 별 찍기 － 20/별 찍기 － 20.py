N = int(input())
s = '*'
b = ' '
ss = ''
for j in range(2 * N) :
    if j % 2 == 0 :
        ss += s
    else :
        ss += b
for i in range(1, N + 1) :
    if i % 2 != 0 :
        print(ss)
    else :
        print(ss[::-1])