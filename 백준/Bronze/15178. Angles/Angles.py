# 15178 Angles

N = int(input())
for i in range(N) :
    a, b, c = map(int, input().split())
    print(a, b, c, end = ' ')
    hap = a + b + c
    if hap == 180 :
        print('Seems OK')
    else :
        print('Check')