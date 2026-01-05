# 14039 Magic Squares

len_MS = 4
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
d = list(map(int, input().split()))
sum_1, sum_2, sum_3, sum_4 = 0, 0, 0, 0
if sum(a) == sum(b) and sum(b) == sum(c) and sum(c) == sum(d) :
    for i in range(len_MS) :
        sum_1 += a[i]
        sum_2 += b[i]
        sum_3 += c[i]
        sum_4 += d[i]
    if sum_1 == sum_2 and sum_2 == sum_3 and sum_3 == sum_4 and sum_1 == sum(a) :
        print('magic')
    else :
        print('not magic')
else :
    print('not magic')