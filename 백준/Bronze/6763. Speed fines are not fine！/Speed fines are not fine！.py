a = int(input())
b = int(input())
f = 0   # fine(벌금)
d = b - a   # difference
if d <= 0 :
    print('Congratulations, you are within the speed limit!')
elif d > 0 and 20 >= d :
    f = 100
elif d > 20 and 30 >= d :
    f = 270
else :
    f = 500
if f != 0 :
    print('You are speeding and your fine is $%d.' % f)