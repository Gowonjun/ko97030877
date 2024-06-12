k = int(input())
c = 0   # commission
c = k * 0.01 + 25
if c < 100 :
    c = 100
elif c > 2000 :
    c = 2000
print('%.2f' % c)