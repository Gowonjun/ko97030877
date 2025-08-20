# 13420 사칙연산

T = int(input())
for _ in range(T) :
    s = input()
    a, b, c, d, e = s.split()
    indx = s.index('=')
    s = s[ : indx]
    if eval(s) == int(e) :
        print('correct')
    else :
        print('wrong answer')