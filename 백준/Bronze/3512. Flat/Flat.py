# 3512  Flat

n, c = map(int, input().split())
total = 0
bedroom = 0
hap = 0
for i in range(n) :
    a, t = input().split()
    a = int(a)
    total += a
    if t == 'balcony' :
        a = a / 2
    if t == 'bedroom' :
        bedroom += a
    hap += a * c
print('%d\n%d\n%f' % (total, bedroom, hap))