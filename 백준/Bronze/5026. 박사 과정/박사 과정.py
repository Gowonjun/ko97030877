# 5026  박사 과정

N = int(input())
for _ in range(N) :
    s = input()
    if s == 'P=NP' :
        print('skipped')
    else :
        print(eval(s))