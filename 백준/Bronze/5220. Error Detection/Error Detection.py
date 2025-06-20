# 5220  Error Detection

T = int(input())
for i in range(T) :
    a, b = map(int, input().split())
    s = str((bin(a)))[2 : ]
    if s.count('1') % 2 == b :
        print('Valid')
    else :
        print('Corrupt')