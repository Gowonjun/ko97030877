# 15792 A/B - 2

A, B = map(int, (input().split()))
print(A // B, end = '')

if A % B != 0 :
    print('.', end = '')

    i = 0
    while A % B != 0 and i < 1000 :
        A = A % B * 10
        i += 1
        #print('A :', A)
        #print('A // B :', A // B)
        print(A // B, end = '')