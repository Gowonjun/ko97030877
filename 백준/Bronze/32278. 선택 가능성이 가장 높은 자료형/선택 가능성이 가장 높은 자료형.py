N = int(input())

if N >= (-1) * 2 ** 15 and N <= 2 ** 15 - 1 :
    print('short')
elif  N >= (-1) * 2 ** 31 and N <= 2 ** 31 - 1 :
    print('int')
elif N >= (-1) * 2 ** 63 and N <= 2 ** 63 - 1 :
    print('long long')