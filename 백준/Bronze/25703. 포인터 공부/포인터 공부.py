s = '*'
print('int a;')
print('int *ptr = &a;')
N = int(input())
if N > 1 :
    print('int **ptr2 = &ptr;')
    for i in range(2, N) :
        print('int %sptr%d = &ptr%d;' % (s * (i + 1), i + 1, i))