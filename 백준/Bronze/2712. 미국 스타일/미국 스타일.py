# 2712  미국 스타일

T = int(input())
for _ in range(T) :
    a, b = input().split()
    a = float(a)
    if b == 'kg' :
        print('%.4f lb' % (2.2046 * a))
    elif b == 'lb' :
        print('%.4f kg' % (0.4536 * a))
    elif b == 'l' :
        print('%.4f g' % (0.2642 * a))
    else :
        print('%.4f l' % (3.7854 * a))