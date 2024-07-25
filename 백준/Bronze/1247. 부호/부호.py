import sys

for _ in range(3) :
    N = int(sys.stdin.readline())
    hap = 0
    for i in range(N) :
        a = int(sys.stdin.readline())
        hap += a
    if hap > 0 :
        print('+')
    elif hap < 0 :
        print('-')
    else :
        print('0')