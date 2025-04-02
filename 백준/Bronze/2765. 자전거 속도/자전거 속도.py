# 2765  자전거 속도

i = 0
while True :
    i += 1
    d, r, t = map(float, input().split())
    if r == 0 :
        break
    total = 3.1415927 * (d / (12 * 5280)) * r
    MPH = total / (t / 3600)
    print('Trip #%d: %.2f %.2f' % (i, total, MPH))