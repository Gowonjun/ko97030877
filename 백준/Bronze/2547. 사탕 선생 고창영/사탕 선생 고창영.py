# 2547  사탕 선생 고창영

T = int(input())
for _ in range(T) :
    blank = input()
    N = int(input())
    hap = 0
    for i in range(N) :
        hap += int(input())
    if hap % N == 0 :
        print('YES')
    else :
        print('NO')